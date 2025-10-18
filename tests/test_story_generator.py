import pytest

from bajki_generator import generate_story


def test_generate_story_paragraphs_and_content():
    story = generate_story(["Ala", "Olek"], "Zaczarowany las", paragraphs=3, seed=42)
    paragraphs = story.split("\n\n")
    assert len(paragraphs) == 3
    for name in ("Ala", "Olek"):
        assert name in story
    assert "Zaczarowany las" in story


def test_generate_story_with_single_paragraph_and_moral():
    moral = "Przyjaźń zwycięża"
    story = generate_story(["Basia"], "Szklana góra", moral=moral, paragraphs=1, seed=0)
    assert "\n\n" not in story
    assert "Morał z tej opowieści jest prosty" in story
    assert moral in story


def test_seed_reproducibility():
    story_a = generate_story(["Antek"], "Podniebne miasto", seed=7)
    story_b = generate_story(["Antek"], "Podniebne miasto", seed=7)
    story_c = generate_story(["Antek"], "Podniebne miasto", seed=8)
    assert story_a == story_b
    assert story_a != story_c


def test_invalid_characters_raise():
    with pytest.raises(ValueError):
        generate_story([], "Morskie głębiny")
    with pytest.raises(TypeError):
        generate_story("Ala", "Morskie głębiny")


def test_duplicate_names_are_removed():
    story = generate_story(["Ala", "ala", "Ola", "Ala"], "Miasteczko marzeń", seed=3)
    assert "Ala i Ola" in story
