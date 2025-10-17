# bajki-generator

Aplikacja AI do tworzenia i czytania bajek audio po polsku.

## Funkcje
- Generowanie unikalnych opowiadań na podstawie krótkiego opisu.
- Synteza mowy umożliwiająca odsłuchanie historii.
- Biblioteka zapisanych bajek dla powracających użytkowników.

## Wymagania wstępne
- Node.js w wersji 20 LTS lub nowszej.
- Dostęp do usług TTS oraz LLM zgodnych z wymaganiami projektu (konfiguracja przez zmienne środowiskowe).

## Uruchomienie lokalne
1. Zainstaluj zależności:
   ```bash
   npm install
   ```
2. Skonfiguruj plik `.env` na podstawie wzorca `.env.example`.
3. Uruchom aplikację developerską:
   ```bash
   npm run dev
   ```

## Testy
```bash
npm test
```

## Licencja
Projekt udostępniany jest na licencji MIT.
