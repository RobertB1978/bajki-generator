# bajki-generator

Aplikacja AI do tworzenia i czytania bajek audio po polsku.

## Generator tekstu

Repozytorium zawiera prosty skrypt `story_generator.py`, który pozwala
szybko przygotować szkic bajki do dalszego nagrania audio. Generator
łączy przygotowane wcześniej fragmenty narracji z danymi podanymi przez
użytkownika, dzięki czemu każda bajka może zostać spersonalizowana.

### Uruchomienie

```bash
python story_generator.py Basia Kacper "Zaczarowany Las" przyjaźń --tone pogodny
```

Opcjonalny parametr `--seed` pozwala na powtarzalne generowanie tej
samej historii, co ułatwia eksperymenty ze ścieżkami audio.

### Integracja z innymi aplikacjami

Skrypt udostępnia funkcję `build_story`, która przyjmuje strukturę
`StoryContext` oraz opcjonalne ziarno losowości. Dzięki temu logikę
budowania bajki można wykorzystać w większym projekcie – np. w usłudze,
która tworzy pliki audio na podstawie tekstu.
