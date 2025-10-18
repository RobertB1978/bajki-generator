# bajki-generator

Aplikacja AI do tworzenia i czytania bajek audio po polsku.

## Cel projektu

Repozytorium dokumentuje prace nad narzędziem, które łączy modele językowe i syntezę mowy, aby w kilka sekund przygotować spersonalizowaną bajkę w formie nagrania audio. Projekt jest na wczesnym etapie, dlatego na razie skupia się na planowaniu architektury i wymagań.

## Planowane funkcjonalności

- Generowanie historii na podstawie krótkiego opisu bohatera, miejsca i tonu opowieści.
- Konwersja wygenerowanego tekstu na naturalnie brzmiące nagranie lektora.
- Możliwość wyboru spośród kilku głosów oraz szybkości czytania.
- Zapisywanie bajek w prywatnej bibliotece użytkownika wraz z metadanymi (tagi, wiek, długość).
- Tryb „na dobranoc” z automatycznym przyciemnianiem ekranu i miękką muzyką w tle.

## Architektura (robocza)

1. **Warstwa generowania treści** – model językowy (np. GPT-4o) przygotowuje scenariusz bajki w oparciu o dane wejściowe użytkownika.
2. **Warstwa audio** – usługa TTS (np. ElevenLabs lub Azure TTS) konwertuje tekst na plik audio WAV/MP3.
3. **Backend** – lekka aplikacja Python (FastAPI) orkiestrująca przepływ, przechowująca metadane w bazie (PostgreSQL lub Supabase).
4. **Frontend** – responsywna aplikacja React/Next.js umożliwiająca konfigurację bajki oraz odsłuch gotowych nagrań.
5. **Integracje** – webhooki pozwalające wysyłać bajki np. do aplikacji mobilnej czy inteligentnych głośników.

## Środowisko deweloperskie

Poniższe kroki opisują tymczasowy, przykładowy przepływ pracy. Wraz z rozwojem projektu instrukcje będą aktualizowane.

```
# 1. Klon repozytorium
git clone https://github.com/<twoja-organizacja>/bajki-generator.git
cd bajki-generator

# 2. Tworzenie i aktywacja środowiska
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instalacja zależności (plik requirements.txt pojawi się w kolejnych iteracjach)
pip install -r requirements.txt

# 4. Uruchomienie backendu deweloperskiego
uvicorn app.main:app --reload

# 5. Uruchomienie frontendu
npm install
npm run dev
```

> **Uwaga:** Powyższe polecenia mają charakter orientacyjny. Docelowy stos technologiczny i struktura katalogów zostaną doprecyzowane wraz z implementacją pierwszych modułów.

## Roadmapa

- [ ] Opracowanie szczegółowych wymagań funkcjonalnych i niefunkcjonalnych.
- [ ] Przygotowanie modułu generowania treści w Pythonie.
- [ ] Integracja z usługą TTS i konfiguracja presetów głosowych.
- [ ] Stworzenie panelu webowego do konfiguracji i odsłuchu bajek.
- [ ] Automatyzacja publikacji bajek w kanałach RSS/podcast.

## Wkład w projekt

Zachęcamy do dzielenia się pomysłami oraz otwierania zgłoszeń (issues) z propozycjami funkcji. W przyszłości dodamy standardowy plik `CONTRIBUTING.md` opisujący proces zgłaszania zmian.

## Licencja

Projekt jest dostępny na licencji MIT – szczegóły znajdują się w pliku [LICENSE](LICENSE).
