"""Story generation endpoint tailored for Vercel serverless."""

from __future__ import annotations

from fastapi import FastAPI

from apps.api.schemas import StoryRequest, StoryResponse
from apps.api.services.story import StoryGenerator, build_story_generator

app = FastAPI(title="Bajki Generator API - Stories")
_generator: StoryGenerator | None = None


def _get_generator() -> StoryGenerator:
    """Return a cached instance of :class:`StoryGenerator`."""

    global _generator
    if _generator is None:
        _generator = build_story_generator()
    return _generator


@app.post("/")
def create_story(payload: StoryRequest) -> StoryResponse:
    """Generate a bedtime story using the shared generator instance."""

    generator = _get_generator()
    return generator.create_story(payload)
