"""Data structures shared across the API."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List


class StoryLength(str, Enum):
    """Available story lengths."""

    short = "short"
    medium = "medium"
    long = "long"


@dataclass(slots=True)
class StoryRequest:
    """Payload describing a story request."""

    hero: str
    age: int
    topic: str
    mood: str = "pogodny"
    length: StoryLength = StoryLength.short

    def __post_init__(self) -> None:
        self.hero = str(self.hero)
        self.topic = str(self.topic)
        self.mood = str(self.mood)

        if isinstance(self.length, str):
            self.length = StoryLength(self.length)

        if not (1 <= int(self.age) <= 12):
            raise ValueError("age must be between 1 and 12")
        self.age = int(self.age)


@dataclass(slots=True)
class StorySegment:
    """Single paragraph of the generated story."""

    title: str
    text: str

    def __post_init__(self) -> None:
        self.title = str(self.title)
        self.text = str(self.text)


@dataclass(slots=True)
class StoryResponse:
    """Response returned after generating a story."""

    title: str
    hero: str
    mood: str
    topic: str
    language: str
    length: StoryLength
    summary: str
    story: List[StorySegment]
    created_at: datetime
    estimated_read_time: int

    def __post_init__(self) -> None:
        self.title = str(self.title)
        self.hero = str(self.hero)
        self.mood = str(self.mood)
        self.topic = str(self.topic)
        self.language = str(self.language)
        self.summary = str(self.summary)

        if isinstance(self.length, str):
            self.length = StoryLength(self.length)

        self.story = [segment if isinstance(segment, StorySegment) else StorySegment(**segment) for segment in self.story]

        if isinstance(self.created_at, str):
            self.created_at = datetime.fromisoformat(self.created_at)

        self.estimated_read_time = int(self.estimated_read_time)
        if self.estimated_read_time < 0:
            raise ValueError("estimated_read_time must be non-negative")


@dataclass(slots=True)
class HealthResponse:
    """Schema for the health check endpoint."""

    status: str
    version: str
