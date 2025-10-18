# Bajki Generator

Nowoczesna aplikacja do tworzenia i czytania bajek audio po polsku. Projekt składa się z:

- **FastAPI** (`apps/`) odpowiadającego za generowanie opowieści,
- **Vite + React** (`web/`) zapewniającego interaktywny interfejs webowy,
- **skryptów developerskich** (`scripts/`) ułatwiających start projektu oraz szybką prezentację API.

## Wymagania

- Python 3.11+
- Node.js 18+
- npm lub pnpm (w przykładach używamy `npm`)

## Uruchomienie lokalne

```bash
# 1. Skonfiguruj zmienne środowiskowe
cp .env.example .env              # backend (FastAPI)
cp .env.example web/.env.local    # frontend (Vite)

# 2. Zainstaluj zależności backendu
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# 3. Zainstaluj zależności frontendowe
cd web
npm install
cd ..

# 4. Uruchom środowisko developerskie (backend + frontend)
./scripts/dev.sh
```

Backend domyślnie udostępnia API pod `http://localhost:8000/api`, natomiast frontend pod `http://localhost:5173`. Wartość `VITE_API_BASE_URL` z pliku `web/.env.local` pozwala zmienić adres używany przez frontend do komunikacji z API (domyślnie `/api`).

## Endpointy API

- `GET /health` – prosty health check,
- `POST /api/stories` – generowanie bajki na podstawie danych wejściowych:
  ```json
  {
    "hero": "Mila",
    "age": 6,
    "topic": "zaczarowany las",
    "mood": "pogodny",
    "length": "short"
  }
  ```

Przykładowe użycie z CLI:

```bash
python scripts/story_cli.py generate Mila --topic "zaczarowany las"
```

## Struktura katalogów

```
apps/           # Kod FastAPI
  api/
    main.py     # Punkt wejścia aplikacji
    routes/     # Routery API
    services/   # Warstwa logiki biznesowej
scripts/
  dev.sh        # Uruchamia backend + frontend w trybie developerskim
  story_cli.py  # Prostą interakcja z API z linii komend
web/            # Aplikacja React + Vite
```

## Licencja

Projekt jest dostępny na licencji MIT.
