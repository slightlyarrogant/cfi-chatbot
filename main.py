from flask import Flask, request, jsonify, render_template
import requests
import uuid
import json
from flask_cors import CORS
import logging
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)

WEBHOOK_URL = "https://vendoerp.app.n8n.cloud/webhook-test/ff77dedf-f609-4cd3-ba0a-8e3300831c99"
TOPIC_SEPARATOR = '|'

chat_histories = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    session_id = data.get('session_id', f"test-{str(uuid.uuid4())}")

    # Log incoming request
    logger.info(f"Incoming request - Session ID: {session_id}, User Input: {user_input}")

    if session_id not in chat_histories:
        chat_histories[session_id] = []

    chat_histories[session_id].append({"type": "user", "message": user_input})

    payload = json.dumps([{
        "sessionId": session_id,
        "action": "sendMessage",
        "chatInput": user_input
    }])

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Log outgoing request to webhook
        logger.info(f"Outgoing request to webhook - Payload: {payload}")

        response = requests.get(WEBHOOK_URL, data=payload, headers=headers)
        response.raise_for_status()

        # Log webhook response
        logger.info(f"Webhook response - Status: {response.status_code}, Content: {response.text}")

        response_data = response.json()
        bot_response = response_data.get('response', {}).get('text', 'No response text')

        related_topics = []
        if "RELATED_TOPICS" in bot_response:
            parts = bot_response.split("RELATED_TOPICS")
            bot_response = parts[0].strip()
            if len(parts) > 1:
                related_topics = [topic.strip() for topic in parts[1].split(TOPIC_SEPARATOR) if topic.strip()]

        chat_histories[session_id].append({"type": "bot", "message": bot_response})

        # Prepare response to client
        response_to_client = {
            "response": bot_response,
            "related_topics": related_topics,
            "session_id": session_id, 
            "history": chat_histories[session_id]
        }

        # Log outgoing response to client
        logger.info(f"Outgoing response to client - {json.dumps(response_to_client)}")

        return jsonify(response_to_client)

    except requests.exceptions.RequestException as e:
        error_message = f"Failed to get response from webhook: {str(e)}"
        logger.error(f"Error in processing request: {error_message}")
        chat_histories[session_id].append({"type": "error", "message": error_message})
        error_response = {
            "error": error_message, 
            "session_id": session_id, 
            "history": chat_histories[session_id]
        }
        logger.info(f"Error response to client - {json.dumps(error_response)}")
        return jsonify(error_response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
