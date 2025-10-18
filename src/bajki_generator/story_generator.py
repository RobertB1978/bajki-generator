"""Narzędzia do generowania krótkich bajek."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random
from typing import Iterable, Sequence


@dataclass(frozen=True)
class StoryConfig:
    """Parametry służące do stworzenia bajki.

    Parametry są walidowane i porządkowane już na etapie tworzenia instancji,
    dzięki czemu funkcja :func:`generate_story` może działać na pewnych
    założeniach. Wartości tekstowe są przycinane i pozbawiane nadmiarowych
    spacji, a lista bohaterów jest odfiltrowywana z duplikatów (z zachowaniem
    kolejności)."""

    characters: Sequence[str]
    setting: str
    moral: str | None = None
    paragraphs: int = 3
    seed: int | None = None

    def __post_init__(self) -> None:  # noqa: D401 - dokumentacja w klasie
        cleaned_characters = _prepare_characters(self.characters)
        object.__setattr__(self, "characters", cleaned_characters)

        cleaned_setting = _normalise_text(self.setting)
        if not cleaned_setting:
            raise ValueError("setting must contain at least one non-space character")
        object.__setattr__(self, "setting", cleaned_setting)

        if self.moral is not None:
            cleaned_moral = _normalise_sentence(self.moral)
            if not cleaned_moral:
                raise ValueError("moral must contain text if provided")
            object.__setattr__(self, "moral", cleaned_moral)
        else:
            object.__setattr__(self, "moral", None)

        if self.paragraphs < 1:
            raise ValueError("paragraphs must be greater than or equal to 1")


def generate_story(
    characters: Iterable[str],
    setting: str,
    *,
    moral: str | None = None,
    paragraphs: int = 3,
    seed: int | None = None,
) -> str:
    """Zbuduj bajkę na podstawie przekazanych informacji.

    Funkcja jest deterministyczna przy ustawieniu parametru ``seed``. Zwracana
    bajka składa się z określonej liczby akapitów oddzielonych pustą linią.

    Parameters
    ----------
    characters:
        Kolekcja nazw bohaterów bajki. Nazwy są czyszczone z nadmiarowych
        spacji i duplikatów, a puste pozycje są ignorowane. Po czyszczeniu
        lista nie może być pusta.
    setting:
        Nazwa świata, miejsca lub kontekstu w którym rozgrywa się akcja.
    moral:
        Opcjonalny morał kończący bajkę. Jeśli zostanie przekazany, ma
        zostać dołączony w ostatnim akapicie.
    paragraphs:
        Liczba akapitów w wygenerowanej bajce. Minimalna wartość to 1.
    seed:
        Ziarno generatora liczb losowych.
    """

    if isinstance(characters, str):
        raise TypeError("characters must be an iterable of strings, not a single string")

    config = StoryConfig(
        characters=tuple(characters),
        setting=setting,
        moral=moral,
        paragraphs=paragraphs,
        seed=seed,
    )
    rng = Random(config.seed)
    context = _build_context(config)

    intro = _render_template(rng.choice(_INTRO_TEMPLATES), context)
    if config.paragraphs == 1:
        closing = _render_closing(config, rng, context)
        return intro + " " + closing

    body: list[str] = [intro]
    for _ in range(config.paragraphs - 2):
        body.append(_render_template(rng.choice(_EVENT_TEMPLATES), context))

    body.append(_render_closing(config, rng, context))
    return "\n\n".join(body)


# -- Pomocnicze struktury -----------------------------------------------------------------


@dataclass(frozen=True)
class _Template:
    singular: str
    plural: str

    def render(self, context: dict[str, object]) -> str:
        text = self.singular if context["count"] == 1 else self.plural
        return text.format(**context)


_INTRO_TEMPLATES: tuple[_Template, ...] = (
    _Template(
        singular="Pewnego dnia {characters} odkrył tajemnicze zakamarki miejsca znanego jako {setting}.",
        plural="Pewnego dnia {characters} odkryli tajemnicze zakamarki miejsca znanego jako {setting}.",
    ),
    _Template(
        singular="{characters} od dawna marzył, aby zobaczyć {setting}, dlatego z bijącym sercem wyruszył w drogę.",
        plural="{characters} od dawna marzyli, aby zobaczyć {setting}, dlatego z bijącymi sercami wyruszyli w drogę.",
    ),
    _Template(
        singular="{setting} skrywało legendy, które rozpalały wyobraźnię bohatera o imieniu {first_character}.",
        plural="{setting} skrywało legendy, które rozpalały wyobraźnię bohaterów takich jak {characters}.",
    ),
)

_EVENT_TEMPLATES: tuple[_Template, ...] = (
    _Template(
        singular="Pośród migoczących świateł {setting} pojawiła się świetlista brama, przez którą bohater przeszedł bez wahania.",
        plural="Pośród migoczących świateł {setting} pojawiła się świetlista brama, przez którą bohaterowie przeszli bez wahania.",
    ),
    _Template(
        singular="Na leśnej polanie {characters} spotkał mądrą sowę, która podarowała mu wskazówki zapisane na liściu.",
        plural="Na leśnej polanie {characters} spotkali mądrą sowę, która podarowała im wskazówki zapisane na liściu.",
    ),
    _Template(
        singular="Górski potok zagrał melodię odwagi i skierował bohatera ku temu, co najważniejsze w {setting}.",
        plural="Górski potok zagrał melodię odwagi i skierował bohaterów ku temu, co najważniejsze w {setting}.",
    ),
    _Template(
        singular="Życzliwy smok wręczył {characters} zagadkowy klucz i poprosił, by chronił on {setting} przed zapomnieniem.",
        plural="Życzliwy smok wręczył {characters} zagadkowy klucz i poprosił, by chronili oni {setting} przed zapomnieniem.",
    ),
    _Template(
        singular="W cieniu starego dębu bohater usłyszał szept dawnych historii i zrozumiał, że trzeba je dalej przekazywać.",
        plural="W cieniu starego dębu bohaterowie usłyszeli szept dawnych historii i zrozumieli, że trzeba je dalej przekazywać.",
    ),
)

_RESOLUTION_TEMPLATES: tuple[_Template, ...] = (
    _Template(
        singular="Dzięki odwadze {characters} mieszkańcy {setting} odzyskali spokój i obiecali pamiętać jego imię.",
        plural="Dzięki odwadze {characters} mieszkańcy {setting} odzyskali spokój i obiecali pamiętać ich imiona.",
    ),
    _Template(
        singular="W nagrodę za dobre serce bohater otrzymał gwiezdny pył, który rozświetlał {possessive} drogę w każdą noc.",
        plural="W nagrodę za dobre serce bohaterowie otrzymali gwiezdny pył, który rozświetlał ich drogę w każdą noc.",
    ),
    _Template(
        singular="Wieczorem {setting} rozbrzmiało pieśnią wdzięczności, a {characters} wiedział, że dokonał czegoś wielkiego.",
        plural="Wieczorem {setting} rozbrzmiało pieśnią wdzięczności, a {characters} wiedzieli, że dokonali czegoś wielkiego.",
    ),
)


def _prepare_characters(characters: Sequence[str]) -> tuple[str, ...]:
    if isinstance(characters, str):
        raise TypeError("characters must be an iterable of strings, not a single string")

    cleaned: list[str] = []
    seen: set[str] = set()
    for raw in characters:
        if raw is None:
            raise TypeError("character names cannot be None")
        text = _normalise_text(str(raw))
        if not text:
            continue
        key = text.casefold()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(text)

    if not cleaned:
        raise ValueError("characters must contain at least one non-empty name")
    return tuple(cleaned)


def _normalise_text(value: str) -> str:
    return " ".join(value.strip().split())


def _normalise_sentence(value: str) -> str:
    text = _normalise_text(value)
    if not text:
        return ""
    return text[0].upper() + text[1:]


def _build_context(config: StoryConfig) -> dict[str, object]:
    count = len(config.characters)
    possessive, dative, accusative = _pronoun_forms(count)
    return {
        "characters": _format_character_list(config.characters),
        "characters_raw": config.characters,
        "first_character": config.characters[0],
        "setting": config.setting,
        "count": count,
        "possessive": possessive,
        "dative": dative,
        "accusative": accusative,
    }


def _pronoun_forms(count: int) -> tuple[str, str, str]:
    if count == 1:
        return "jego", "mu", "go"
    return "ich", "im", "ich"


def _format_character_list(characters: Sequence[str]) -> str:
    if len(characters) == 1:
        return characters[0]
    if len(characters) == 2:
        return f"{characters[0]} i {characters[1]}"
    return ", ".join((*characters[:-1], f"i {characters[-1]}"))


def _render_template(template: _Template, context: dict[str, object]) -> str:
    return template.render(context)


def _render_closing(config: StoryConfig, rng: Random, context: dict[str, object]) -> str:
    resolution = _render_template(rng.choice(_RESOLUTION_TEMPLATES), context)
    if config.moral:
        resolution = f"{resolution} {_format_moral(config.moral)}"
    return resolution


def _format_moral(moral: str) -> str:
    text = moral.strip()
    if not text:
        raise ValueError("moral must contain text")
    if text[-1] not in ".!?":
        text += "."
    return f"Morał z tej opowieści jest prosty: {text}"
