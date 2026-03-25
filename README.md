# Sprawozdanie 3
Wiktoria Cendrowska-Kociuga

Zadanie 2 
Dla { "x": 7 }
Odpowiedź 
{
    "input": 7,
    "prediction": 14.0
}

Zadanie 3
Po wysłaniu {} 
Odpowiedź 
{
    "error": "Brak danych JSON"
}
Po {
  "x": "abc"
}

Odpowiedź
{
    "error": "Pole 'x' musi być liczbą"
}

Laboratorium nr 4 dalej jest wykonywane tutaj
testowane w postamanie

Zadanie 5

Uruchamianie aplikacji ML API
1. Lokalnie 
Wejdź do folderu projektu:
cd C:\Users\Asus\PycharmProjects\NTPD_lab3
Aktywuj virtualenv:
venv\Scripts\activate
Zainstaluj wymagane biblioteki:
pip install -r requirements.txt
Uruchom aplikację w trybie developerskim:
python main.py
Test endpointów:
/health http://127.0.0.1:5000/health
/info  http://127.0.0.1:5000/info
/predict  POST JSON: {"x": 7}

2. Za pomocą Dockera
Zbuduj obraz:
docker build -t apka .
Uruchom kontener w trybie produkcyjnym:
docker run -p 5000:5000 apka
Test endpointów:
/health → http://127.0.0.1:5000/health
/info → http://127.0.0.1:5000/info
/predict → POST JSON: {"x": 7}


3. Za pomocą Docker Compose
Zbuduj i uruchom wszystkie serwisy:
docker-compose up --build
Sprawdź logi w terminalu
Test endpointów:
/health → http://127.0.0.1:5000/health
/predict → POST JSON: {"x": 7}

Serwisy w tej samej sieci Docker Compose mogą się komunikować po nazwie serwisu, np. redis:6379.

4. Konfiguracja parametrów i zasoby
Zmienne środowiskowe
Można je ustawić w Dockerfile, Docker Compose lub lokalnie w terminalu.
Przykład w Docker Compose:
environment:
  - PORT=5000
W Pythonie można je odczytać:
import os
port = int(os.environ.get("PORT", 5000))
