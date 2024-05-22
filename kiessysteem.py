from stemcomputers import (
    initaliseer_stemcomputers,
    stemcomputer1,
    stemcomputer2,
    stemcomputer3,
)
import random

initaliseer_stemcomputers()

random_keuze = random.randint(1, 3)

if random_keuze == 1:
    stemcomputer1.stemmen()
elif random_keuze == 2:
    stemcomputer2.stemmen()
elif random_keuze == 3:
    stemcomputer3.stemmen()
