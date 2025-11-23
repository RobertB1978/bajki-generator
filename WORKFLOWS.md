# WORKFLOWS

Aplikacja nie posiada jeszcze silnika workflow. Poniżej opis wdrożenia zgodnego z wymaganiami.

## Wymagane komponenty
- Kolejka Redis do asynchronicznych zadań, worker oparty o `RQ`/`Arq`/`Celery`.
- Polityka retry z backoffem wykładniczym i bezpieczne limity czasu.
- Circuit breaker dla zawodnych narzędzi (np. integracje z LLM/API zewnętrznymi).
- Audit trail każdego zadania (statusy, wejście/wyjście, czas, tenant).
- Runtime policies: `max_tokens`, `frequency_limiter`, `tenant_overhead_cap`.

## API
- `POST /api/workflows/run` – uruchomienie zadania, zwraca `workflow_id`.
- `GET /api/workflows/{id}` – status i dziennik zdarzeń.
- Webhook/WS do streamu statusów dla konsoli operatorskiej.

## Testy
- Sukces, porażka, retry, breaker open/close, limit częstotliwości, cap per tenant.
