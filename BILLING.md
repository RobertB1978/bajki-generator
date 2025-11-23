# BILLING & SUBSCRIPTIONS

Repozytorium nie zawiera jeszcze modułu rozliczeń. Poniższy plan opisuje zgodny z wymaganiami kierunek wdrożenia Stripe.

## Założenia
- Modele subskrypcji per tenant z oknem 30/90 dni (miękkie i twarde limity na API, RAG, workflow, storage).
- Webhooki Stripe z weryfikacją podpisu i historią faktur.
- Grace period przy zmianie planu i metadane okna limitów w odpowiedziach API.

## Plan implementacji
1. **Modele**: `Tenant`, `Subscription`, `Invoice`, `UsageWindow` z polami `soft_limit`, `hard_limit`, `window_start`, `window_end`.
2. **Webhook**: endpoint `/api/billing/stripe/webhook` z weryfikacją `Stripe-Signature` i obsługą zdarzeń `invoice.paid`, `invoice.payment_failed`, `customer.subscription.updated`.
3. **Limity**: middleware FastAPI weryfikujący zużycie i zwracający 429 przy twardym limicie; nagłówki/metadane z informacją o oknie limitów.
4. **Panel**: API dla frontendu zwracające historię faktur i bieżące wykorzystanie per tenant.
5. **Testy**: scenariusze soft/hard limit, okna 30/90 dni, grace period, walidacja podpisu webhooks.
