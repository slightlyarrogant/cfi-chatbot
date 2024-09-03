# CFI Chatbot

CFI Chatbot to interaktywna aplikacja webowa służąca do udzielania informacji o systemie Vendo.ERP i jego funkcjonalnościach. Chatbot wykorzystuje zaawansowane przetwarzanie języka naturalnego do interpretacji pytań użytkowników i udzielania odpowiedzi na temat różnych aspektów systemu ERP.

## Funkcje

- Interfejs chatbota z możliwością wprowadzania pytań przez użytkownika
- Przetwarzanie zapytań w języku naturalnym
- Generowanie odpowiedzi na podstawie bazy wiedzy o systemie Vendo.ERP
- Wyświetlanie powiązanych tematów jako sugestii dalszych pytań
- Obsługa formatowania Markdown w odpowiedziach
- Logowanie interakcji dla celów debugowania i analizy

## Technologie

- Python 3.8+
- Flask (backend)
- HTML/CSS/JavaScript (frontend)
- Markdown (formatowanie odpowiedzi)

## Instalacja

1. Sklonuj repozytorium:
   ```
   git clone https://github.com/slightlyarrogant/cfi-chatbot.git
   cd cfi-chatbot
   ```

2. Zainstaluj wymagane zależności:
   ```
   pip install -r requirements.txt
   ```

3. Uruchom aplikację:
   ```
   python main.py
   ```

4. Otwórz przeglądarkę i przejdź pod adres `http://localhost:8080`

## Konfiguracja

- W pliku `main.py` możesz dostosować URL webhooka oraz inne parametry konfiguracyjne.
- Plik `templates/index.html` zawiera frontend aplikacji, który można dostosować wedle potrzeb.

## Rozwiązywanie problemów

- Sprawdź plik `app.log` w celu uzyskania szczegółowych informacji o błędach i interakcjach.
- Upewnij się, że masz odpowiednie uprawnienia do zapisu w katalogu projektu dla plików logów.

## Wkład i rozwój

Zachęcamy do zgłaszania problemów i propozycji ulepszeń poprzez system Issues na GitHubie. Pull requesty są mile widziane!

## Licencja

Brak
