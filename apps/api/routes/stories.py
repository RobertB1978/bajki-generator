"""Story endpoints."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from ..schemas import StoryRequest, StoryResponse
from ..services.story import StoryGenerator, build_story_generator

router = APIRouter(prefix="/stories", tags=["stories"])


@router.post("", response_model=StoryResponse)
def create_story(
    payload: StoryRequest,
    generator: StoryGenerator = Depends(build_story_generator),
) -> StoryResponse:
    """Generate a fresh bedtime story."""

    return generator.create_story(payload)
