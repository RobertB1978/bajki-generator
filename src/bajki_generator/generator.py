"""Logika generowania bajek tekstowych."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional
import random


@dataclass
class Story:
    """Struktura przechowująca wygenerowaną bajkę."""

    title: str
    paragraphs: List[str]
    hero: str
    theme: Optional[str] = None
    moral: Optional[str] = None

    def as_text(self) -> str:
        """Zwraca pełną treść bajki jako jeden ciąg tekstu."""

        parts: List[str] = [self.title, ""]
        parts.extend(self.paragraphs)
        if self.moral:
            if parts and parts[-1].strip():
                parts.append("")
            parts.append(f"Puenta: {self.moral}")
        return "\n".join(parts).strip()

    def __str__(self) -> str:  # pragma: no cover - prosty wrapper
        return self.as_text()


class StoryGenerator:
    """Generator bajek inspirowany klasyczną strukturą opowieści."""

    _length_to_paragraphs: Dict[str, int] = {
        "short": 3,
        "medium": 4,
        "long": 5,
    }

    def __init__(self, random_seed: Optional[int] = None) -> None:
        self._random = random.Random(random_seed)
        self._characters_by_age: Dict[str, List[str]] = {
            "3-5": ["Tosia", "Jaś", "Lila", "Antek", "Fela"],
            "6-8": ["Nela", "Kajtek", "Mila", "Filip", "Hania"],
            "9-12": ["Maja", "Oskar", "Lidka", "Iwo", "Karina"],
        }
        self._universal_characters: List[str] = [
            "Kornelia",
            "Tymek",
            "Lucek",
            "Ada",
            "Mania",
        ]
        self._settings: List[str] = [
            "bajkowym lesie, gdzie liście świeciły jak gwiazdy",
            "pływającym miasteczku unoszącym się na miękkich chmurach",
            "małej górskiej wiosce otoczonej tęczowymi wodospadami",
            "tajemniczej bibliotece ukrytej w korzeniach starego dębu",
            "słonecznej dolinie, w której śpiewały kamienie",
        ]
        self._companions: List[str] = [
            "mówiący jeżyk Tuptuś",
            "odważna sówka Pola",
            "zwinny kotek Migotek",
            "śpiewająca rybka Falka",
            "tańczący smok Błyskotek",
        ]
        self._magical_items: List[str] = [
            "bursztynowy kompas marzeń",
            "plecak pełen światełek odwagi",
            "kryształowy dzwoneczek przyjaźni",
            "zaczarowana mapa szeptów",
            "notatnik, w którym słowa same układały się w piosenki",
        ]
        self._item_powers: List[str] = [
            "potrafił wskazać serca potrzebujące radości",
            "rozświetlał najciemniejsze zakamarki dobrymi wspomnieniami",
            "przywoływał wspierające głosy przyjaciół",
            "umiał zatrzymać czas na chwilę czułości",
            "szeptał najlepsze pomysły, kiedy ktoś tracił nadzieję",
        ]
        self._goals: List[str] = [
            "odnaleźć melodię zaginionej kołysanki",
            "zobaczyć, jak wygląda świt widziany z grzbietu tęczy",
            "nauczyć się języka, którym rozmawiają gwiazdy",
            "oddać uśmiech, który kiedyś spadł z księżyca",
            "zbudować most z opowieści między dwoma sercami",
        ]
        self._problems: List[str] = [
            "nad krainę nadciągnęła smutna, szara mgła",
            "dzieci w miasteczku zapomniały, jak się uśmiechać",
            "wiatr porwał wszystkie kołysanki i nikt nie mógł zasnąć",
            "wielki zegar snów stanął i noc nie chciała odejść",
            "szeptana rzeka przestała opowiadać historie",
        ]
        self._actions: List[str] = [
            "odwiedził mądrą skrzypaczkę mieszkającą w wydrążonym drzewie",
            "zamienił zwykłe kamyki w iskierki odwagi",
            "zorganizował ciche słuchanie serc mieszkańców",
            "narysował w powietrzu mapę dobrych myśli",
            "poprosił wiatr o podpowiedź i złapał ją w dłonie",
        ]
        self._discoveries: List[str] = [
            "każda historia ma ukrytą nutę, którą trzeba odnaleźć",
            "wspólne śmiechy potrafią obudzić śpiące gwiazdy",
            "najważniejsze słowa słychać dopiero wtedy, gdy zapada cisza",
            "przytulenie potrafi naprawić popękane sny",
            "małe gesty uruchamiają wielkie cuda",
        ]
        self._supporters: List[str] = [
            "świetlista ważka Melodia",
            "wesoły promyk światła z gwiazdozbioru Życzliwości",
            "dobrotliwy smok Ogniś o pastelowych skrzydłach",
            "tajemniczy błękitny kamień, który pulsował ciepłem",
            "gromadka figlarnych świetlików prowadzących w rytmie walca",
        ]
        self._details: List[str] = [
            "zachęcał, aby wsłuchać się w bicie serca lasu",
            "pokazał drogę przez wirujące barwy radości",
            "rozpalił na niebie drogowskaz z gwiazd",
            "narysował w wodzie most z delikatnych słów",
            "rozkołysał liście tak, by szeptały odwagę",
        ]
        self._progresses: List[str] = [
            "odnalazł w sobie odwagę, by zrobić kolejny krok",
            "poczuł, że jego marzenie jest na wyciągnięcie ręki",
            "zrozumiał, że wspólna praca dodaje skrzydeł",
            "odkrył, że cisza potrafi opowiedzieć najwięcej",
            "przypomniał wszystkim, jak smakuje serdeczny śmiech",
        ]
        self._virtues: List[str] = [
            "nie bał się poprosić o pomoc",
            "cierpliwie słuchał każdego spotkanego stworzenia",
            "dzielił się dobrym słowem i ciepłym uśmiechem",
            "odważnie zrobił pierwszy krok w nieznane",
            "pamiętał, że razem można więcej",
        ]
        self._resolutions: List[str] = [
            "mgła rozpłynęła się, a niebo roztańczyło kolorowe zorze",
            "miasteczko znów wypełniło się śmiechem i śpiewem",
            "kołysanki wróciły, kołysząc wszystkich do spokojnego snu",
            "zegar snów znów tykał w rytmie spokojnych serc",
            "rzeka ponownie zaczęła snuć historie pełne ciepła",
        ]
        self._celebrations: List[str] = [
            "wieczornym piknikiem przy świetlikach",
            "tańcem na miękkich chmurach",
            "wspólnym pieczeniem pachnących rogalików",
            "koncertem cykających świerszczy",
            "składaniem kolorowych liści wdzięczności",
        ]
        self._morals: List[str] = [
            "Współpraca i ciepłe słowa leczą nawet największy smutek.",
            "Najbardziej magiczna jest odwaga, by być życzliwym.",
            "Marzenia rosną wtedy, gdy dzielimy je z innymi.",
            "Serce, które słucha, znajduje rozwiązanie każdej zagadki.",
            "Dobro wraca szybciej, niż potrafi polecieć strach.",
        ]
        self._theme_messages: Dict[str, str] = {
            "przyjaźń": "Historia przypominała wszystkim, że prawdziwa przyjaźń potrafi rozświetlić najciemniejszą noc.",
            "odwaga": "Każdy, kto usłyszał tę opowieść, poczuł, jak w sercu zapala się płomień odwagi.",
            "wyobraźnia": "Bohaterowie zrozumieli, że wyobraźnia jest skrzydłem, na którym można polecieć gdzie tylko się zapragnie.",
            "rodzina": "Opowieść niosła wieść, że rodzinne ciepło to miękki koc chroniący przed troskami.",
        }
        self._title_templates: List[str] = [
            "{hero} i tajemnica {keyword}",
            "Jak {hero} ocalił {keyword}",
            "Opowieść o tym, jak {hero} odnalazł {keyword}",
            "{hero} oraz niezwykłe {keyword}",
        ]

    def generate_story(
        self,
        *,
        length: str = "medium",
        hero_name: Optional[str] = None,
        age_group: str = "6-8",
        theme: Optional[str] = None,
        include_moral: bool = True,
    ) -> Story:
        """Generuje nową bajkę na podstawie zadanych parametrów."""

        normalized_length = length.lower()
        if normalized_length not in self._length_to_paragraphs:
            valid = ", ".join(self._length_to_paragraphs)
            raise ValueError(f"Nieznana długość bajki: {length!r}. Dostępne wartości: {valid}")

        hero = self._normalise_hero(hero_name, age_group)
        companion = self._choice(self._companions)
        setting = self._choice(self._settings)
        magical_item = self._choice(self._magical_items)
        item_power = self._choice(self._item_powers)
        goal = self._choice(self._goals)
        problem = self._choice(self._problems)
        resolution = self._choice(self._resolutions)
        celebration = self._choice(self._celebrations)

        theme_message = self._prepare_theme_message(theme)
        title_keyword = (theme or magical_item).lower()
        title_template = self._choice(self._title_templates)
        title = title_template.format(hero=hero, keyword=title_keyword)

        paragraphs: List[str] = []
        paragraphs.append(
            (
                f"W {setting} mieszkało sobie dziecko o imieniu {hero}. "
                f"{hero} od dawna marzył, aby {goal}. "
                f"Ulubionym towarzyszem wypraw był {companion}. "
                f"Pewnego poranka bohater znalazł {magical_item}, który {item_power}."
            )
        )

        paragraphs.append(
            (
                f"Niedługo później pojawił się kłopot: {problem}. "
                f"{hero} wziął głęboki oddech i {self._choice(self._actions)}. "
                f"Dzięki temu odkrył, że {self._choice(self._discoveries)}."
            )
        )

        middle_paragraphs_needed = self._length_to_paragraphs[normalized_length] - 2
        for _ in range(max(middle_paragraphs_needed - 1, 0)):
            supporter = self._choice(self._supporters)
            detail = self._choice(self._details)
            progress = self._choice(self._progresses)
            paragraphs.append(
                (
                    f"Na drodze pojawił się {supporter}, który {detail}. "
                    f"Razem z {hero} {progress}."
                )
            )

        paragraphs.append(
            (
                f"W finale {hero} {self._choice(self._virtues)}, co sprawiło, że {resolution}. "
                f"Cała kraina świętowała {celebration}."
            )
        )

        if theme_message:
            paragraphs.append(theme_message)

        moral = self._choice(self._morals) if include_moral else None
        return Story(title=title, paragraphs=paragraphs, hero=hero, theme=theme, moral=moral)

    # region helpers
    def _normalise_hero(self, hero_name: Optional[str], age_group: str) -> str:
        if hero_name:
            cleaned = hero_name.strip()
            if cleaned:
                return cleaned
        return self._choice(self._characters_for_age(age_group))

    def _characters_for_age(self, age_group: str) -> List[str]:
        return self._characters_by_age.get(age_group, []) + self._universal_characters

    def _choice(self, values: Iterable[str]) -> str:
        values_list = list(values)
        if not values_list:
            raise ValueError("Lista elementów do losowania jest pusta.")
        return self._random.choice(values_list)

    def _prepare_theme_message(self, theme: Optional[str]) -> Optional[str]:
        if not theme:
            return None
        normalized = theme.lower()
        if normalized in self._theme_messages:
            return self._theme_messages[normalized]
        return (
            f"Opowieść była przesycona motywem \"{theme}\", który dodawał bohaterom skrzydeł."
        )

    # endregion


__all__ = ["StoryGenerator", "Story"]
