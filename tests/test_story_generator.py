from __future__ import annotations

from bajki_generator.generator import StoryGenerator


def test_generate_story_with_custom_hero_and_theme() -> None:
    generator = StoryGenerator(random_seed=42)
    story = generator.generate_story(length="short", hero_name="Zosia", theme="przyjaźń")

    assert story.hero == "Zosia"
    assert story.theme == "przyjaźń"
    assert len(story.paragraphs) >= 3
    assert any("przyjaźń" in paragraph.lower() for paragraph in story.paragraphs)
    assert story.moral is not None
    text = story.as_text()
    assert text.startswith(story.title)
    assert "Puenta:" in text


def test_story_length_variants() -> None:
    generator = StoryGenerator(random_seed=101)
    short_story = generator.generate_story(length="short", include_moral=False)
    medium_story = generator.generate_story(length="medium", include_moral=False)
    long_story = generator.generate_story(length="long", include_moral=False)

    assert len(short_story.paragraphs) < len(medium_story.paragraphs) <= len(long_story.paragraphs)


def test_invalid_length_raises() -> None:
    generator = StoryGenerator()
    with pytest.raises(ValueError):  # type: ignore[name-defined]
        generator.generate_story(length="gigantic")


def test_story_as_text_has_blank_lines() -> None:
    generator = StoryGenerator(random_seed=7)
    story = generator.generate_story(length="medium", hero_name="Leo", include_moral=True)
    text = story.as_text()

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    assert paragraphs[0] == story.title
    assert any("Puenta:" in chunk for chunk in paragraphs)


# pytest is imported lazily to zachować minimalne zależności podczas działania CLI
import pytest  # noqa: E402  pylint: disable=wrong-import-position
