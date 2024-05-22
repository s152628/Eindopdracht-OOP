import random
from kiezers import Kiezers


partij_A = []
while len(partij_A) <= 9:
    kandidaat = random.choice(Kiezers)
    partij_A.append(kandidaat)
partij_B = []
while len(partij_B) <= 9:
    kandidaat = random.choice(Kiezers)
    partij_B.append(kandidaat)
partij_C = []
while len(partij_C) <= 9:
    kandidaat = random.choice(Kiezers)
    partij_C.append(kandidaat)
partij_D = []
while len(partij_D) <= 9:
    kandidaat = random.choice(Kiezers)
    partij_D.append(kandidaat)
partij_E = []
while len(partij_E) <= 9:
    kandidaat = random.choice(Kiezers)
    partij_E.append(kandidaat)


class Lijst:
    def __init__(self, naam, kandidaten):
        self.naam = naam
        self.kandidaten = kandidaten
        self.stemmen = 0
        self.kandidaat_1 = 0
        self.kandidaat_2 = 0
        self.kandidaat_3 = 0
        self.kandidaat_4 = 0
        self.kandidaat_5 = 0
        self.kandidaat_6 = 0
        self.kandidaat_7 = 0
        self.kandidaat_8 = 0
        self.kandidaat_9 = 0
        self.kandidaat_10 = 0

    def Lijst_stemmen(self):
        self.stemmen += 1

    def Voorkeur_stemmen(self):
        self.stemmen += 1
        aantal_stemmen = random.randint(1, 10)
        kandidaten = list(range(1, 11))
        random.shuffle(kandidaten)

        for i in range(aantal_stemmen):
            kandidaat_keuze = kandidaten[i]
            match kandidaat_keuze:
                case 1:
                    self.kandidaat_1 += 1
                case 2:
                    self.kandidaat_2 += 1
                case 3:
                    self.kandidaat_3 += 1
                case 4:
                    self.kandidaat_4 += 1
                case 5:
                    self.kandidaat_5 += 1
                case 6:
                    self.kandidaat_6 += 1
                case 7:
                    self.kandidaat_7 += 1
                case 8:
                    self.kandidaat_8 += 1
                case 9:
                    self.kandidaat_9 += 1
                case 10:
                    self.kandidaat_10 += 1


partij_A_lijst = Lijst("The Companions", partij_A)
partij_B_lijst = Lijst("The Dark Brotherhood", partij_B)
partij_C_lijst = Lijst("The Thieves Guild", partij_C)
partij_D_lijst = Lijst("The Imperials", partij_D)
partij_E_lijst = Lijst("The Stormcloaks", partij_E)

Lijsten = [
    partij_A_lijst,
    partij_B_lijst,
    partij_C_lijst,
    partij_D_lijst,
    partij_E_lijst,
]
