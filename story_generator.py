"""Simple fairy tale generator for Polish audio stories.

The module exposes :func:`build_story` which can be reused by other
applications and a small CLI for interactive use.
"""
from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from typing import Iterable, List


def _choice(options: Iterable[str], rng: random.Random) -> str:
    """Return a random element from *options* using the provided RNG."""

    options_list: List[str] = list(options)
    if not options_list:
        msg = "options must not be empty"
        raise ValueError(msg)
    return rng.choice(options_list)


@dataclass
class StoryContext:
    """Container for the configurable parts of a story."""

    child: str
    friend: str
    place: str
    moral: str
    tone: str


INTRODUCTIONS = [
    "W {place} mieszkało rodzeństwo {child} i {friend}, które potrafiło śmiać się z każdego poranka.",
    "Pewnego dnia {child} i najlepsza przyjaciółka {friend} wyruszyli, aby odkryć sekret, który skrywał {place}.",
    "Gdy księżyc wschodził nad {place}, {child} wraz z {friend} szykowali się na niezwykłą przygodę.",
]


CONFLICTS = [
    "Na swojej drodze spotkali płaczącą wiewiórkę, której magiczne orzechy przestały świecić.",
    "W oddali usłyszeli szept, który prosił o pomoc w odnalezieniu zagubionej melodii lasu.",
    "Przed nimi stanął zaczarowany most, który nie przepuścił nikogo bez odważnej opowieści.",
]


RESOLUTIONS = [
    "Dzięki temu, że {child} słuchała sercem, a {friend} dodawała otuchy, przyjaciele odkryli, że najmocniejsza magia kryje się w życzliwości.",
    "Wspólnym śmiechem i cierpliwością nauczyli mieszkańców, że każdy głos jest potrzebny, aby powstała harmonia.",
    "Ich serdeczność odmieniła los {place}, przypominając, że prawdziwa odwaga to pomaganie innym.",
]


OUTROS = [
    "Od tej pory w {place} rozbrzmiewał śmiech, a {child} z {friend} pamiętali, że {moral} to najlepsza ścieżka do szczęścia.",
    "Wieść o ich czynach niosła się daleko, przypominając wszystkim, że {moral} potrafi zmienić świat na lepsze.",
    "Wspomnienia z tej wyprawy opowiadano przy ogniskach, ucząc dzieci, że {moral} jest siłą, której nic nie zatrzyma.",
]


TONES = {
    "pogodny": "opowieść pełna uśmiechu i jasnych kolorów",
    "przygodowy": "historia o odwadze, odkrywaniu i współpracy",
    "uspokajający": "łagodna bajka do słuchania przed snem",
}


def build_story(ctx: StoryContext, *, seed: int | None = None) -> str:
    """Compose a short fairy tale based on the provided context."""

    rng = random.Random(seed)

    tone_description = TONES.get(ctx.tone, ctx.tone)

    parts = [
        _choice(INTRODUCTIONS, rng).format(child=ctx.child, friend=ctx.friend, place=ctx.place),
        _choice(CONFLICTS, rng),
        _choice(RESOLUTIONS, rng).format(child=ctx.child, friend=ctx.friend, place=ctx.place),
        _choice(OUTROS, rng).format(child=ctx.child, friend=ctx.friend, place=ctx.place, moral=ctx.moral),
        f"Tak kończy się {tone_description}.",
    ]
    return "\n\n".join(parts)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generator bajek po polsku")
    parser.add_argument("child", help="imię głównej bohaterki lub bohatera")
    parser.add_argument("friend", help="imię przyjaciela lub przyjaciółki")
    parser.add_argument("place", help="miejsce, w którym toczy się akcja")
    parser.add_argument("moral", help="myśl przewodnia bajki, np. 'przyjaźń'")
    parser.add_argument(
        "--tone",
        default="pogodny",
        choices=sorted(TONES.keys()),
        help="nastrojowa wersja bajki",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="wartość losowania zapewniająca powtarzalny wynik",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    ctx = StoryContext(
        child=args.child,
        friend=args.friend,
        place=args.place,
        moral=args.moral,
        tone=args.tone,
    )
    story = build_story(ctx, seed=args.seed)
    print(story)


if __name__ == "__main__":
    main()
