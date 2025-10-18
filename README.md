# bajki-generator

Aplikacja AI do tworzenia i czytania bajek audio po polsku.

## Funkcje

- generowanie bajek o różnej długości dopasowanych do wieku odbiorców,
- możliwość ustawienia imienia bohatera i motywu przewodniego,
- prosty narrator tworzący plik WAV jako placeholder nagrania,
- interfejs CLI z obsługą parametrów i opcjonalnym zapisem audio.

## Wymagania

- Python 3.10+

## Instalacja w trybie deweloperskim

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Uruchomienie

Wygenerowanie bajki w terminalu:

```bash
python -m bajki_generator --length medium --hero "Ania" --theme przyjaźń
```

Zapis bajki wraz z plikiem WAV:

```bash
python -m bajki_generator --audio output.wav
```

Plik audio ma charakter poglądowy i przedstawia muzyczną interpretację tekstu.

## Testy

```bash
pytest
```
