import random
from chipkaart import Chipkaart

voornamen = [
    "Olivia",
    "Emma",
    "Louise",
    "Mila",
    "Lina",
    "Alice",
    "Anna",
    "Mia",
    "Nora",
    "Lucie",
    "Noah",
    "Arthur",
    "Liam",
    "Louis",
    "Adam",
    "Jules",
    "Lucas",
    "Gabriël",
    "Victor",
    "Finn",
]
achternamen = [
    "Peeters",
    "Janssens",
    "Maes",
    "Jacobs",
    "Mertens",
    "Willems",
    "Claes",
    "Goossens",
    "Wouters",
    "De Smet",
    "De Jong",
    "De Vries",
    "Van De Berg",
    "Bakker",
    "Van Dijk",
    "Visser",
    "Smit",
    "De Boer",
    "Van Dongen",
    "Decoster",
]


class Kiezer:
    def __init__(self, voornamen, achternamen):
        self.voornaam = random.choice(voornamen)
        self.achternaam = random.choice(achternamen)
        self.leeftijd = random.randint(18, 90)
        self.magstemmen = False

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"

    def geefChipkaart(self, Chipkaart, code):
        if Chipkaart.code == code:
            self.magstemmen = True


Kiezers = []
for i in range(1200):
    kiezer = Kiezer(voornamen, achternamen)
    Kiezers.append(kiezer)
chipkaart = Chipkaart()
chipkaart.initialisatie(1234)
for kiezer in Kiezers:
    kiezer.geefChipkaart(chipkaart, 1234)
