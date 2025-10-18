"""Pydantic schemas shared across the API."""
from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class StoryLength(str, Enum):
    """Available story lengths."""

    short = "short"
    medium = "medium"
    long = "long"


class StoryRequest(BaseModel):
    """Payload describing a story request."""

    hero: str = Field(..., description="Imię głównego bohatera")
    age: int = Field(..., ge=1, le=12, description="Wiek słuchacza")
    topic: str = Field(..., description="Główny motyw bajki")
    mood: str = Field("pogodny", description="Ton opowieści")
    length: StoryLength = Field(
        default=StoryLength.short,
        description="Preferowana długość bajki",
    )


class StorySegment(BaseModel):
    """Single paragraph of the generated story."""

    title: str
    text: str


class StoryResponse(BaseModel):
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
    estimated_read_time: int = Field(
        ..., description="Szacowany czas czytania w sekundach"
    )


class HealthResponse(BaseModel):
    """Schema for the health check endpoint."""

    status: str
    version: str
