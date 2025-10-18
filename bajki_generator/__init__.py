"""Generator bajek po polsku.

Moduł udostępnia główną klasę :class:`StoryGenerator`, która potrafi tworzyć
krótkie opowieści z gotowych elementów fabularnych. Dane słownikowe znajdują
się w module :mod:`story_data`.
"""

from .story_generator import Story, StoryGenerator

__all__ = ["Story", "StoryGenerator"]
