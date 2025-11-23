# OPERATIONS

Instrukcja eksploatacji Bajki Generator w obecnym kształcie.

## Środowiska
- **Dev**: uruchamiany przez `./scripts/dev.sh` (FastAPI na :8000, Vite na :5173).
- **Env**: konfiguracja w `.env` (backend) oraz `web/.env.local` (frontend). Prefiksy `BAJKI_` i `VITE_` zapobiegają konfliktom zmiennych.

## Uruchomienie lokalne
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -e .[dev]`
3. `cd web && npm install && cd ..`
4. `./scripts/dev.sh`

## Podstawowe komendy
- **Backend tests**: `pytest`
- **Frontend tests**: `cd web && npm test`
- **Lint/format (frontend)**: `cd web && npm run lint && npm run format`

## Deploy (prosty wariant)
- Build frontendu: `cd web && npm run build` – artefakty w `web/dist`.
- Backend jako kontener: `uvicorn apps.api.main:app --host 0.0.0.0 --port 8000`.

## Monitorowanie i logi
Obecnie minimalne – należy zintegrować stack obserwowalności (Prometheus/Grafana/Tempo/Loki) zgodnie z wymaganiami enterprise.

## Backup i retencja
Aplikacja nie utrzymuje trwałego stanu. Przed rozbudową o bazę danych (Postgres, Redis) należy dodać polityki backupu i retencji zgodnie z wymaganiami 30/90/365.
