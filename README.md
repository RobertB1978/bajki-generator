# Bajki Generator

Aplikacja do generowania bajek z frontendem Vite/React oraz funkcjami Python hostowanymi na Vercel.

## Run locally

1. **Zainstaluj zależności frontendowe.**
   ```bash
   npm install --prefix web
   ```
2. **(Opcjonalnie) Przygotuj wirtualne środowisko Pythona do testów.**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install pytest
   ```
3. **Przygotuj zmienne środowiskowe Supabase.** Skopiuj `web/.env.example` do `web/.env` i uzupełnij wartości (`VITE_SUPABASE_URL`, `VITE_SUPABASE_KEY`). Brak wartości oznacza, że Supabase nie będzie inicjowane, ale aplikacja nadal działa.
4. **Uruchom środowisko developerskie.** Najwygodniej przez Vercel Dev, który obsługuje funkcje Pythona i frontend.
   ```bash
   npm run build --prefix web
   vercel dev
   ```
   Alternatywnie możesz zbudować frontend i uruchomić statyczny podgląd:
   ```bash
   npm run build --prefix web
   npm run preview --prefix web
   # funkcje /api działają po wdrożeniu na Vercel
   ```
5. **Testy i smoke:**
   ```bash
   npm run test --prefix web     # Vitest
   pytest -q                     # Pytest dla funkcji Python
   npm run smoke --prefix web    # Smoke test (wymaga działającego hosta pod SMOKE_BASE)
   ```

## Deploy

1. Zaloguj się do Vercel i wskaż repozytorium. W projekcie ustaw katalog główny na root repozytorium (plik `vercel.json` zarządza buildem).
2. W sekcji *Environment Variables* dodaj `VITE_SUPABASE_URL` oraz `VITE_SUPABASE_KEY` dla wszystkich środowisk. Frontend pobiera je z `import.meta.env`.
3. Wdrażaj jak zwykle – Vercel użyje `vercel.json`, aby zbudować aplikację (`web/`) i wystawić funkcje serverless (`api/`).
4. Po wdrożeniu sprawdź:
   ```bash
   curl -s https://<twoja-domena>.vercel.app/api/health
   curl -s -X POST https://<twoja-domena>.vercel.app/api/stories \
     -H 'Content-Type: application/json' \
     -d '{"hero":"Ala","mood":"pogodny"}'
   ```

## Struktura

```
vercel.json        # Konfiguracja Vercel (frontend + Python functions)
api/                # Funkcje serverless (health, stories)
web/                # Frontend Vite/React (dist jako output)
  scripts/smoke.mjs # Smoke test endpointów w środowisku Vercel/local
  .env.example      # Placeholdery zmiennych Supabase
``` 
