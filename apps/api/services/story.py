"""Story generation helpers."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from random import choice
from textwrap import fill
from typing import Iterable, List

from ..config import get_settings
from ..schemas import StoryLength, StoryRequest, StoryResponse, StorySegment


@dataclass(slots=True)
class StoryTemplate:
    """Structure used to assemble a story."""

    introduction: str
    challenges: Iterable[str]
    resolution: str


class StoryGenerator:
    """Deterministic yet playful story generator.

    The implementation is intentionally lightweight so the project can be run
    completely offline while still returning varied narratives.
    """

    def __init__(self) -> None:
        self._settings = get_settings()
        self._templates: List[StoryTemplate] = [
            StoryTemplate(
                introduction="{hero} wyrusza na wyprawę, aby odkryć tajemnicę związaną z {topic}.",
                challenges=[
                    "Po drodze spotyka {companion}, który dołącza do przygody.",
                    "Muszą wspólnie rozwiązać zagadkę ukrytą w {place}.",
                ],
                resolution="Dzięki odwadze i uśmiechowi {hero} odkrywa, że {lesson}.",
            ),
            StoryTemplate(
                introduction="W miasteczku niedaleko lasu mieszkał {hero}, marzący o niezwykłej przygodzie z {topic}.",
                challenges=[
                    "Niespodziewanie pojawia się wiadomość od tajemniczego przyjaciela.",
                    "Razem przygotowują magiczny plan, aby odmienić los mieszkańców miasteczka.",
                ],
                resolution="Wieczorem wszyscy świętują, a {hero} obiecuje dzielić się radością każdego dnia.",
            ),
        ]
        self._lessons = [
            "przyjaźń jest największą siłą",
            "wystarczy wiara w siebie, aby osiągnąć niemożliwe",
            "każdy dzień może być początkiem niezwykłej historii",
        ]
        self._companions = ["wesoły smok", "mądra sowa", "śpiewający robot", "szalony wynalazca"]
        self._places = [
            "zaczarowanej bibliotece",
            "świetlistej jaskini",
            "podniebnej wieży",
            "słonecznym porcie",
        ]
        self._twists = [
            "Magiczny kompas zaczyna świecić i pokazuje sekretną ścieżkę ukrytą pod tęczą.",
            "Pojawia się zagadkowa mapa, na której litery układają się w piosenkę.",
            "Na nocnym niebie rysuje się gwiezdny znak prowadzący bohaterów do ukrytego ogrodu.",
            "Z kieszeni {companion} wypada stary list z zachętą, aby zaufać własnym marzeniom.",
        ]

    def _pick_template(self) -> StoryTemplate:
        return choice(self._templates)

    def _estimate_read_time(self, paragraphs: Iterable[str]) -> int:
        words = sum(len(paragraph.split()) for paragraph in paragraphs)
        words_per_minute = 120  # typical pace for bedtime stories
        return max(60, int(words / words_per_minute * 60))

    def create_story(self, payload: StoryRequest) -> StoryResponse:
        template = self._pick_template()
        companion = choice(self._companions)
        place = choice(self._places)
        lesson = choice(self._lessons)

        paragraphs: List[StorySegment] = []
        introduction = template.introduction.format(hero=payload.hero, topic=payload.topic)
        paragraphs.append(
            StorySegment(title="Początek przygody", text=fill(introduction, 100))
        )

        for idx, challenge in enumerate(template.challenges, start=1):
            paragraphs.append(
                StorySegment(
                    title=f"Próba {idx}",
                    text=fill(
                        challenge.format(
                            hero=payload.hero,
                            topic=payload.topic,
                            companion=companion,
                            place=place,
                        ),
                        100,
                    ),
                )
            )

        if payload.length in {StoryLength.medium, StoryLength.long}:
            twist = choice(self._twists)
            paragraphs.append(
                StorySegment(
                    title="Magiczny zwrot akcji",
                    text=fill(twist.format(companion=companion), 100),
                )
            )

        if payload.length == StoryLength.long:
            bonus = (
                f"{payload.hero} odkrywa w sobie nowy talent i dzieli się nim z przyjaciółmi,"
                " ucząc wszystkich, że dobro wraca z potrojoną mocą."
            )
            paragraphs.append(StorySegment(title="Wielki finał", text=fill(bonus, 100)))

        resolution = template.resolution.format(hero=payload.hero, lesson=lesson)
        paragraphs.append(StorySegment(title="Szczęśliwe zakończenie", text=fill(resolution, 100)))

        summary = (
            f"{payload.hero} mierzy się z wyzwaniem związanym z {payload.topic} i odkrywa, że {lesson}."
        )
        estimated_time = self._estimate_read_time(segment.text for segment in paragraphs)

        return StoryResponse(
            title=f"{payload.hero} i tajemnica {payload.topic}",
            hero=payload.hero,
            mood=payload.mood,
            topic=payload.topic,
            language=self._settings.default_language,
            length=payload.length,
            summary=summary,
            story=paragraphs,
            created_at=datetime.utcnow(),
            estimated_read_time=estimated_time,
        )


def build_story_generator() -> StoryGenerator:
    """Factory function used for dependency injection."""

    return StoryGenerator()
