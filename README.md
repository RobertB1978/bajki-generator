# bajki-generator

Aplikacja AI do tworzenia i czytania bajek audio po polsku.

## Funkcje

- generowanie krótkich bajek na podstawie listy bohaterów oraz miejsca akcji,
- możliwość dodania morału kończącego opowieść,
- deterministyczne wyniki przy użyciu parametru `seed`.

## Użycie

```python
from bajki_generator import generate_story

story = generate_story(
    ["Ala", "Olek"],
    "Zaczarowany las",
    moral="Przyjaźń sprawia, że wszystko staje się łatwiejsze",
    paragraphs=3,
    seed=42,
)
print(story)
```
