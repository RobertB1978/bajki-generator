# Bajki Generator

Nowoczesna aplikacja do tworzenia i czytania bajek audio po polsku. Projekt składa się z:

- **FastAPI** (`apps/`) odpowiadającego za generowanie opowieści,
- **Vite + React** (`web/`) zapewniającego interaktywny interfejs webowy,
- **skryptów developerskich** (`scripts/`) ułatwiających start projektu oraz szybką prezentację API.

## Wymagania

- Python 3.11+
- Node.js 18+
- npm lub pnpm (w przykładach używamy `npm`)

## Szybki start

```bash
# Zainstaluj zależności backendu
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# Zainstaluj zależności frontendowe
cd web
npm install
cd ..

# Uruchom środowisko developerskie (backend + frontend)
./scripts/dev.sh
```

Backend domyślnie udostępnia API pod `http://localhost:8000/api`, natomiast frontend pod `http://localhost:5173`.

## Uruchomienie lokalne

1. **Skonfiguruj zmienne środowiskowe.** Skopiuj plik `.env.example` do `.env` (backend) oraz do `web/.env.local` (frontend) i w razie potrzeby zaktualizuj wartości:
   ```bash
   cp .env.example .env
   cp .env.example web/.env.local
   ```
   Backend korzysta z prefiksu `BAJKI_`, a frontend z `VITE_`. Dzięki temu konfiguracja API jest spójna dla wszystkich usług.
2. **Utwórz i aktywuj wirtualne środowisko Pythona, a następnie zainstaluj zależności backendu:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```
3. **Zainstaluj zależności frontendowe:**
   ```bash
   cd web
   npm install
   cd ..
   ```
4. **Uruchom oba serwisy w trybie developerskim:**
   ```bash
   ./scripts/dev.sh
   ```
   Skrypt startuje backend FastAPI na porcie `8000` oraz frontend Vite na porcie `5173` z proxy na `/api`.
5. **Opcjonalnie:** sprawdź API bezpośrednio z CLI – np. `python scripts/story_cli.py generate Mila --topic "zaczarowany las"`.

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
