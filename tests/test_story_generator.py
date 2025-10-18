import pytest

from bajki_generator.story_generator import StoryGenerator


def test_story_is_deterministic_with_seed():
    generator = StoryGenerator(seed=7)
    story = generator.generate_story(paragraphs=4)

    assert story.title == "Zosia i znikające kolory"
    assert story.paragraphs == [
        "Zosia mieszka w miasteczku utkanym z drewnianych mostków i wiatraków, w którym gwiazdy odbijały się w każdym oknie. Towarzyszem przygód jest kotka Iskra, potrafiąca rozświetlić najciemniejszy zakamarek swoim uśmiechem.",
        "Pewnego dnia z ulubionej łąki zaczęły znikać kolory, jakby ktoś wycierał je gumką. Drzewa poszarzały, a śmiech dzieci ucichł od smutku. Zosia nie może na to patrzeć i postanawia działać.",
        "Zosia wraz z ciekawską kotką Iskrą proszą o radę sowy Jagny, mądrej strażniczki leśnych opowieści. Podarowała im mapę z zaznaczoną ścieżką prowadzącą do źródła światła.",
        "Zosia i Iskra zatańczyli taniec odwagi, a jego rytm obudził każdy kolor w dolinie.",
    ]
    assert story.moral == "Morał: dobro powraca, jeśli wysyłamy je w świat z uśmiechem."


def test_additional_events_extend_story():
    generator = StoryGenerator(seed=11)
    story = generator.generate_story(paragraphs=6)

    assert len(story.paragraphs) == 6
    # Spodziewamy się dwóch dodatkowych akapitów ze zdarzeniami pobocznymi.
    assert story.paragraphs[2:4] == [
        "Po drodze Leo zauważa, że nawet kamienie wzdychają z tęsknoty za śmiechem dzieci.",
        "Iskra znajduje na ścieżce iskrę, która cichutko szepcze drogę do celu.",
    ]


def test_rejects_too_short_story():
    generator = StoryGenerator(seed=5)
    with pytest.raises(ValueError):
        generator.generate_story(paragraphs=2)
