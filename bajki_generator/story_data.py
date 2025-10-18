"""Zestaw gotowych elementów fabularnych wykorzystywanych przez generator.

Dane zostały podzielone na kilka małych struktur, aby można było w prosty
sposób rozszerzać repertuar opowieści. Każdy element jest zapisany w formie
krótkich zdań po polsku, tak by bez dodatkowych przekształceń tworzył poprawną
gramatycznie historię.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Setting:
    """Opis miejsca, w którym rozpoczyna się bajka."""

    place: str
    atmosphere: str


@dataclass(frozen=True)
class Companion:
    """Towarzysz bohatera wraz z krótkimi opisami w różnych kontekstach."""

    introduction: str
    travel_form: str
    short_name: str


@dataclass(frozen=True)
class Problem:
    """Problem lub tajemnica, z którą musi zmierzyć się bohater."""

    title: str
    description: str
    consequence: str


@dataclass(frozen=True)
class Helper:
    """Postać udzielająca bohaterowi wskazówki."""

    meeting: str
    description: str
    advice: str


@dataclass(frozen=True)
class StoryData:
    """Zbiór wszystkich możliwych elementów wykorzystywanych do generowania."""

    settings: Sequence[Setting]
    companions: Sequence[Companion]
    problems: Sequence[Problem]
    helpers: Sequence[Helper]
    resolutions: Sequence[str]
    morals: Sequence[str]
    additional_events: Sequence[str]


DEFAULT_DATA = StoryData(
    settings=[
        Setting(
            place="małej wiosce ukrytej między jeziorami",
            atmosphere="gdzie poranki pachniały cynamonem i miodem",
        ),
        Setting(
            place="miasteczku utkanym z drewnianych mostków i wiatraków",
            atmosphere="w którym gwiazdy odbijały się w każdym oknie",
        ),
        Setting(
            place="nadmorskiej osadzie pełnej szumiących muszelek",
            atmosphere="której strzegły łagodne mewy i przyjazne foki",
        ),
        Setting(
            place="krainie pachnących sadów i wysokich traw",
            atmosphere="gdzie nocą świerszcze grały melodie jak z harfy",
        ),
    ],
    companions=[
        Companion(
            introduction="wierny pies Puszek, który umiał wyczuwać tęsknotę w sercach dzieci",
            travel_form="wiernym psem Puszkiem",
            short_name="Puszek",
        ),
        Companion(
            introduction="energiczna wiewiórka Migotka, skacząca po gałązkach szybciej niż wiatr",
            travel_form="sprytną wiewiórką Migotką",
            short_name="Migotka",
        ),
        Companion(
            introduction="sówka Nutka, nucąca melodie, które potrafiły uspokoić nawet burzę",
            travel_form="mądrą sówką Nutką",
            short_name="Nutka",
        ),
        Companion(
            introduction="kotka Iskra, potrafiąca rozświetlić najciemniejszy zakamarek swoim uśmiechem",
            travel_form="ciekawską kotką Iskrą",
            short_name="Iskra",
        ),
    ],
    problems=[
        Problem(
            title="znikające kolory",
            description="z ulubionej łąki zaczęły znikać kolory, jakby ktoś wycierał je gumką",
            consequence="Drzewa poszarzały, a śmiech dzieci ucichł od smutku.",
        ),
        Problem(
            title="senną mgłę",
            description="nad okolicą rozlała się senna mgła, która usypiała nawet pszczoły w połowie lotu",
            consequence="Gdy tylko ktoś próbował się uśmiechnąć, mgła otulała go ciężkim ziewnięciem.",
        ),
        Problem(
            title="zapomnianą melodię",
            description="miasteczko zapomniało swojej porannej melodii, a koguty przestały pieć",
            consequence="Bez pieśni mieszkańcy nie mogli odnaleźć drogi do swoich marzeń.",
        ),
        Problem(
            title="rozsypane gwiazdy",
            description="nocne niebo zaczęło gubić gwiazdy, które spadały na ziemię bez blasku",
            consequence="Wędrowcy gubili ścieżki, a dzieci śniły już tylko o szarych chmurach.",
        ),
    ],
    helpers=[
        Helper(
            meeting="sowy Jagny",
            description="mądrej strażniczki leśnych opowieści",
            advice="Podarowała im mapę z zaznaczoną ścieżką prowadzącą do źródła światła.",
        ),
        Helper(
            meeting="pani Zorzy",
            description="artystki malującej poranki na różowo",
            advice="Przekazała bohaterom garść iskier, które trzeba było rozdmuchać śmiechem.",
        ),
        Helper(
            meeting="dziadka Szmeru",
            description="opiekuna szepczących strumieni",
            advice="Nauczył ich, jak wsłuchać się w wodę i odnaleźć ukryte w niej odpowiedzi.",
        ),
        Helper(
            meeting="wróżki Kaliny",
            description="plecącej opowieści z cieni i promieni słońca",
            advice="Dała im szkatułkę, która otwierała się tylko, gdy serca biły jednym rytmem.",
        ),
    ],
    resolutions=[
        "{hero} i {companion} zatańczyli taniec odwagi, a jego rytm obudził każdy kolor w dolinie.",
        "{hero} z {companion} rozśmieszyli mgłę, która rozpłynęła się w ciepłym blasku świtu.",
        "Wspólnie zaśpiewali melodię, którą pamiętały tylko stare wiatraki, przywracając mieszkańcom marzenia.",
        "Gdy wypuścili iskry z otrzymanej szkatułki, niebo rozbłysło tysiącem nowych gwiazd.",
    ],
    morals=[
        "Morał: najjaśniej świeci odwaga dzielona z przyjaciółmi.",
        "Morał: kiedy słuchamy siebie nawzajem, nawet cisza zaczyna śpiewać.",
        "Morał: dobro powraca, jeśli wysyłamy je w świat z uśmiechem.",
        "Morał: każdy dzień nabiera barw, gdy dzielimy się nimi z innymi.",
    ],
    additional_events=[
        "Po drodze {hero} zauważa, że nawet kamienie wzdychają z tęsknoty za śmiechem dzieci.",
        "{companion} znajduje na ścieżce iskrę, która cichutko szepcze drogę do celu.",
        "Nad ich głowami przelatuje klucz żurawi układających się w kształt serca, dodając otuchy bohaterom.",
        "W pobliskim sadzie spotykają babcię Malwę, która przypomina im kołysankę o odwadze.",
    ],
)
