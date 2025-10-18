"""Interfejs wiersza poleceń dla generatora bajek."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from .generator import StoryGenerator
from .narrator import NarrationError, SimpleNarrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generowanie bajki i opcjonalnej narracji audio")
    parser.add_argument("--length", choices=["short", "medium", "long"], default="medium", help="Długość bajki")
    parser.add_argument("--hero", dest="hero_name", help="Imię głównego bohatera", default=None)
    parser.add_argument(
        "--age-group",
        dest="age_group",
        default="6-8",
        help="Przedział wiekowy słuchaczy (np. 3-5, 6-8, 9-12)",
    )
    parser.add_argument("--theme", help="Motyw przewodni bajki", default=None)
    parser.add_argument("--no-moral", action="store_true", help="Wyłącz dodawanie puenty")
    parser.add_argument("--seed", type=int, default=None, help="Ustal ziarno generatora losowego")
    parser.add_argument(
        "--audio",
        dest="audio_path",
        help="Ścieżka zapisu pliku WAV z narracją (opcjonalnie)",
        default=None,
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    generator = StoryGenerator(random_seed=args.seed)
    story = generator.generate_story(
        length=args.length,
        hero_name=args.hero_name,
        age_group=args.age_group,
        theme=args.theme,
        include_moral=not args.no_moral,
    )

    print(story.as_text())

    if args.audio_path:
        narrator = SimpleNarrator()
        try:
            audio_file = narrator.synthesize_to_file(story.as_text(), Path(args.audio_path))
        except NarrationError as exc:  # pragma: no cover - komunikat dla użytkownika CLI
            parser.error(str(exc))
        else:
            print(f"\nZapisano narrację do pliku: {audio_file}")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
