# TENANCY

Aplikacja musi wspierać wielu najemców z izolacją zasobów. Poniżej rekomendacje architektoniczne.

## Modele
- `Tenant` z limitami: `api_req`, `rag_queries`, `workflows`, `storage_bytes`.
- `User` z rolami (Admin, Editor, Viewer, Operator, ReadOnly Auditor) i atrybutami ABAC (np. `department`, `sensitivity_clearance`).

## Izolacja
- Kontekst tenanta przekazywany w nagłówku/ JWT; każda operacja w bazie przefiltrowana po `tenant_id`.
- Rate limiting i metryki per tenant.
- Dashboard SLO per tenant (latencja, błędy, wykorzystanie limitów).

## Testy izolacji
- Scenariusze blokujące wycieki danych między tenantami w API i w warstwie storage.
- Sprawdzenie limitów (twarde/miękkie) i poprawnego resetu okna rozliczeniowego.
