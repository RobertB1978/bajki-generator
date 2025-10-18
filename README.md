# bajki-generator

Aplikacja AI do tworzenia i czytania bajek audio po polsku.

## O projekcie

Repozytorium zawiera prosty generator bajek tekstowych napisany w Pythonie.
Wykorzystuje on zestaw przygotowanych elementów fabuły i losuje z nich spójną
opowieść z morałem. Generator może działać jako biblioteka Python oraz jako
narzędzie CLI.

## Wymagania

* Python 3.11+

## Instalacja w trybie deweloperskim

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Użycie CLI

```bash
python -m bajki_generator --seed 7 --akapitów 5 --markdown
```

Dostępne opcje:

* `--seed` – ustawia ziarno generatora liczb losowych, dzięki czemu historia
  będzie deterministyczna.
* `--bohater` – pozwala narzucić imię głównego bohatera.
* `--akapitów` – określa liczbę akapitów w opowieści (minimum 3).
* `--morał` – umożliwia podanie własnego morału.
* `--markdown` – wypisuje wynik w formacie Markdown.

## API Pythona

```python
from bajki_generator import StoryGenerator

story = StoryGenerator(seed=123).generate_story(paragraphs=4)
print(story.to_text())
```

## Testy

```bash
pytest
```
