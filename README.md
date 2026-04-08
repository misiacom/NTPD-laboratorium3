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

# Sprawozdanie 5

https://ml-api-service-902861812719.europe-west1.run.app - publiczny endpoint
Wdrożenia serverless 
Zalety:
-Brak konieczności zarządzania serwerem — infrastruktura jest utrzymywana przez dostawcę chmury
-Automatyczne skalowanie — aplikacja dostosowuje się do ruchu
-Płatność za użycie — płacisz tylko za czas działania aplikacji
-Łatwe wdrożenie — szybkie uruchomienie aplikacji z kontenera
-Wysoka dostępność — dostawca zapewnia niezawodność
Wady:
-Cold start — opóźnienie przy pierwszym uruchomieniu aplikacji
-Ograniczona kontrola nad środowiskiem i konfiguracją
-Limity zasobów (CPU, RAM, czas działania)
-Zależność od dostawcy (vendor lock-in)
-Koszty mogą rosnąć przy dużym ruchu
-Własny serwer (on-premise / VPS)
Zalety:
-Pełna kontrola nad środowiskiem i konfiguracją
-Brak ograniczeń platformy (można dostosować system według potrzeb)
-Stałe koszty (np. VPS) niezależnie od ruchu
-Brak cold startów — aplikacja działa cały czas
Wady:
-Konieczność zarządzania serwerem (aktualizacje, bezpieczeństwo)
-Większa odpowiedzialność za stabilność i dostępność
-Skalowanie wymaga ręcznej konfiguracji
-Wyższy próg wejścia (konfiguracja infrastruktury)
-Koszty utrzymania nawet przy braku ruchu

### Konfiguracja zmiennych środowiskowych w Google Cloud Run

Zmienne środowiskowe zostały skonfigurowane w usłudze Cloud Run
w sekcji "Variables & Secrets", gdzie dodano zmienną:
- Name: API_KEY  
- Value: 12345-secret-key  