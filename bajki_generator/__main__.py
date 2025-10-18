"""Prosty interfejs CLI do generowania bajek."""

from __future__ import annotations

import argparse
from typing import Optional

from .story_generator import StoryGenerator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generuj bajki po polsku.")
    parser.add_argument("--seed", type=int, default=None, help="Ziarno generatora liczb losowych")
    parser.add_argument("--bohater", type=str, default=None, help="Imię głównego bohatera")
    parser.add_argument(
        "--akapitów",
        type=int,
        default=4,
        help="Liczba akapitów historii (minimum 3)",
    )
    parser.add_argument("--morał", type=str, default=None, help="Własny morał kończący bajkę")
    parser.add_argument(
        "--markdown",
        action="store_true",
        help="Zwróć wynik w formacie Markdown",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    generator = StoryGenerator(seed=args.seed)
    story = generator.generate_story(
        hero=args.bohater,
        paragraphs=args.akapitów,
        moral=args.morał,
    )

    if args.markdown:
        print(story.to_markdown())
    else:
        print(story.to_text())


if __name__ == "__main__":
    main()
