# DEVELOPER GUIDE

Krótki przewodnik dla kontrybutorów.

## Wymagania
- Python 3.11+, Node 18+.
- Zalecane: wirtualne środowisko Pythona oraz `npm`/`pnpm` dla frontendu.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cd web && npm install && cd ..
```

## Uruchamianie
- Dev: `./scripts/dev.sh`
- Backend solo: `uvicorn apps.api.main:app --reload`
- Frontend solo: `cd web && npm run dev`

## Testy
- `pytest` dla backendu.
- `cd web && npm test` dla frontendu.

## Styl kodu
- Backend: PEP8/ruff (należy dodać konfig w kolejnych iteracjach).
- Frontend: ESLint + Prettier (konfiguracja w `web/.eslintrc.cjs`).

## Co dalej
Repozytorium wymaga rozbudowy do pakietu enterprise (billing, RAG, workflow, ABAC/RBAC, compliance). Prosimy o utrzymanie czystych warstw, pełnego pokrycia testami i izolacji tenantów przy kolejnych zmianach.
