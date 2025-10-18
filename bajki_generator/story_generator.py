"""Logika odpowiedzialna za tworzenie bajek tekstowych."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence
import random

from .story_data import Companion, DEFAULT_DATA, Helper, Problem, Setting, StoryData


@dataclass(frozen=True)
class Story:
    """Reprezentacja wygenerowanej historii."""

    title: str
    paragraphs: Sequence[str]
    moral: str

    def to_text(self) -> str:
        """Zwraca historię w formacie gotowym do wyświetlenia w konsoli."""

        blocks: List[str] = [self.title, ""]
        blocks.extend(self.paragraphs)
        blocks.append("")
        blocks.append(self.moral)
        return "\n".join(blocks)

    def to_markdown(self) -> str:
        """Zwraca historię sformatowaną jako prosty dokument Markdown."""

        lines: List[str] = [f"# {self.title}", ""]
        lines.extend(self.paragraphs)
        lines.append("")
        lines.append(f"**{self.moral}**")
        return "\n".join(lines)


class StoryGenerator:
    """Generator bajek wykorzystujący gotowe elementy fabularne."""

    def __init__(self, data: StoryData | None = None, *, seed: Optional[int] = None) -> None:
        self._data = data or DEFAULT_DATA
        self._rng = random.Random(seed)

    def generate_story(
        self,
        *,
        hero: Optional[str] = None,
        paragraphs: int = 4,
        moral: Optional[str] = None,
    ) -> Story:
        """Tworzy nową bajkę.

        Args:
            hero: Imię głównego bohatera. Jeśli ``None`` zostanie wylosowane.
            paragraphs: Liczba akapitów (minimum 3). Większe wartości powodują
                dodanie dodatkowych wydarzeń w środku historii.
            moral: Własny morał historii. Jeśli ``None`` zostanie wylosowany z
                dostępnych opcji.
        """

        if paragraphs < 3:
            raise ValueError("Bajka musi składać się co najmniej z trzech akapitów.")

        chosen_hero = hero or self._pick_name()
        setting = self._rng.choice(self._data.settings)
        companion = self._rng.choice(self._data.companions)
        problem = self._rng.choice(self._data.problems)
        helper = self._rng.choice(self._data.helpers)
        resolution_template = self._rng.choice(self._data.resolutions)
        chosen_moral = moral or self._rng.choice(self._data.morals)

        paragraphs_text = self._compose_paragraphs(
            chosen_hero,
            setting,
            companion,
            problem,
            helper,
            resolution_template,
            paragraphs,
        )

        title = f"{chosen_hero} i {problem.title}"
        return Story(title=title, paragraphs=paragraphs_text, moral=chosen_moral)

    def _compose_paragraphs(
        self,
        hero: str,
        setting: Setting,
        companion: Companion,
        problem: Problem,
        helper: Helper,
        resolution_template: str,
        desired_paragraphs: int,
    ) -> Sequence[str]:
        intro = (
            f"{hero} mieszka w {setting.place}, {setting.atmosphere}. "
            f"Towarzyszem przygód jest {companion.introduction}."
        )
        conflict = (
            f"Pewnego dnia {problem.description}. {problem.consequence} "
            f"{hero} nie może na to patrzeć i postanawia działać."
        )

        additional = self._generate_additional_events(hero, companion, desired_paragraphs - 4)

        helper_paragraph = (
            f"{hero} wraz z {companion.travel_form} proszą o radę {helper.meeting}, "
            f"{helper.description}. {helper.advice}"
        )
        resolution = self._format_resolution(resolution_template, hero, companion)

        paragraphs: List[str] = [intro, conflict]
        paragraphs.extend(additional)
        paragraphs.append(helper_paragraph)
        paragraphs.append(resolution)

        return paragraphs

    def _generate_additional_events(
        self, hero: str, companion: Companion, to_generate: int
    ) -> Sequence[str]:
        if to_generate <= 0:
            return []

        pool = list(self._data.additional_events)
        if not pool:
            return []

        if to_generate >= len(pool):
            selected = [event.format(hero=hero, companion=companion.short_name) for event in pool]
            remaining = to_generate - len(pool)
            if remaining > 0:
                selected.extend(
                    self._rng.choice(pool).format(hero=hero, companion=companion.short_name)
                    for _ in range(remaining)
                )
            return selected

        chosen = self._rng.sample(pool, k=to_generate)
        return [event.format(hero=hero, companion=companion.short_name) for event in chosen]

    def _format_resolution(self, template: str, hero: str, companion: Companion) -> str:
        return template.format(hero=hero, companion=companion.short_name)

    def _pick_name(self) -> str:
        """Losuje imię bohatera z niewielkiej puli neutralnych propozycji."""

        candidates = ("Hania", "Jaś", "Zosia", "Leo", "Mila", "Antek", "Lila")
        return self._rng.choice(candidates)


__all__ = ["Story", "StoryGenerator"]
