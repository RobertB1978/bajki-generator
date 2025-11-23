# Architecture Overview

Bajki Generator składa się z lekkiego backendu FastAPI oraz frontendowej aplikacji React budowanej przez Vite. Projekt jest gotowy do rozszerzania o komponenty enterprise, ale obecna architektura zachowuje prostotę i jasny podział na warstwy.

## Backend (FastAPI)
- **apps/api/main.py** – punkt wejścia serwisu, konfiguracja CORS i routerów.
- **apps/api/routes** – moduł z trasami HTTP odpowiadającymi za generowanie bajek.
- **apps/api/services** – miejsce na logikę biznesową (przygotowane do rozbudowy o billing, RAG, workflow, ABAC/RBAC).

API korzysta z wzorca rozdzielenia konfiguracji (`get_settings`) oraz schematów Pydantic w katalogu `apps/api/schemas`. Dzięki temu można bezpiecznie dodawać kolejne moduły (np. subskrypcje, audyt, wielodostępność) bez dotykania warstwy prezentacji.

## Frontend (Vite + React)
- **web/src** – komponenty UI korzystające z TypeScript, React i TailwindCSS.
- **web/vite.config.ts** – konfiguracja proxy na `/api`, co upraszcza integrację lokalną z backendem.

Interfejs jest modularny i przygotowany do wprowadzania nowych paneli (audit, billing, RAG), a warstwa stylów korzysta z Tailwinda, co umożliwia spójną personalizację motywu.

## Dev & Ops
- **scripts/dev.sh** uruchamia jednocześnie backend i frontend w trybie developerskim.
- Środowisko konfiguruje się przez `.env` oraz `web/.env.local` z prefiksami `BAJKI_` i `VITE_`.

## Droga do funkcji enterprise
Aby dojść do pełnego pakietu enterprise, architektura przewiduje dopisanie modułów:
- warstwa persystencji (PostgreSQL + Redis),
- zarządzanie najemcami i limitami (ABAC/RBAC),
- rozliczenia (Stripe),
- RAG z pgvector i hybrydowym wyszukiwaniem,
- audyt i zgodność (hash chain, retencja),
- orkiestracja workflowów na kolejce Redis.

Każdy z tych modułów powinien być implementowany jako odrębne pakiety z własnymi testami integracyjnymi, tak aby rdzeń aplikacji pozostał prosty i łatwy do utrzymania.
