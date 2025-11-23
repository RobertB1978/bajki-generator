# RAG

Obecny kod nie implementuje RAG. Poniższy szkic opisuje podejście produkcyjne.

## Infrastruktura
- Postgres + rozszerzenie `pgvector` (cosine similarity) oraz indeksy `ivfflat`.
- Hybrydowe wyszukiwanie: BM25 (full-text) + wektory; ranking łączony.

## Ingestion
- Pipeline do plików PDF/DOCX/TXT z ekstrakcją tekstu, segmentacją i wzbogaceniem o metadane: `sensitivity`, `retention_days`, `compliance_tags`.
- Walidacja rozmiaru i sanitacja wejścia.

## API
- `POST /api/rag/documents` – ingest + metadane.
- `POST /api/rag/query` – wyszukiwanie hybrydowe, scoring, explain.
- Wynik zawiera scoring, źródła i informacje o ograniczeniach dostępu (ABAC/RBAC).

## Testy
- Ingest/metadata, wyszukiwanie wektorowe i BM25, ranking hybrydowy, polityki retencji i czułości.
