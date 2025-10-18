"""Pakiet z prostym generatorem bajek i syntetyzatorem audio."""

from .generator import StoryGenerator, Story
from .narrator import SimpleNarrator, NarrationError

__all__ = [
    "StoryGenerator",
    "Story",
    "SimpleNarrator",
    "NarrationError",
]
