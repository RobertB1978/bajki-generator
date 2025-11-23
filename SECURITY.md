# SECURITY

Projekt jest w fazie lekkiej wersji MVP. Poniższe zasady stanowią bazę do dalszego utwardzania zgodnie z "Secure by Default".

## Minimalne zabezpieczenia
- Wymuszaj HTTPS w środowiskach produkcyjnych (terminacja TLS na reverse proxy).
- Ustaw poprawne nagłówki CORS w `apps/api/main.py` – domyślnie tylko pochodzenia lokalne.
- Przechowuj sekrety w zmiennych środowiskowych, nigdy w repozytorium.

## To-do przed wersją enterprise
- Dodać JWT (access + refresh) z listą jti w Redis.
- Dodać RBAC/ABAC oparty o role i czułość zasobu.
- Dołożyć limity per tenant (rate limiting, zużycie RAG/workflow, storage).
- Włączyć audit log z podpisem kryptograficznym (hash chain) i retencją 30/90/365.
- Wdrożyć SSO/OAuth (Google, Microsoft) oraz magic links.

## Zgłaszanie incydentów
- W trybie produkcyjnym skonfiguruj kanał alertów (Slack/webhook) dla błędów krytycznych i zdarzeń bezpieczeństwa.
