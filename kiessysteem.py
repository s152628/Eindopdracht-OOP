from stemcomputers import (
    initaliseer_stemcomputers,
    stem_simulatie,
)
from lijsten import Lijsten


def stemsimulatie():
    initaliseer_stemcomputers()
    stem_simulatie()
    print("Kiezers hebben gestemd!")


stemsimulatie()


kandidatenlijst1 = []
kandidatenlijst2 = []
kandidatenlijst3 = []
kandidatenlijst4 = []
kandidatenlijst5 = []
for lijst in Lijsten:
    if len(kandidatenlijst1) <= 9:
        kandidatenlijst1.append(lijst.kandidaat_1)
        kandidatenlijst1.append(lijst.kandidaat_2)
        kandidatenlijst1.append(lijst.kandidaat_3)
        kandidatenlijst1.append(lijst.kandidaat_4)
        kandidatenlijst1.append(lijst.kandidaat_5)
        kandidatenlijst1.append(lijst.kandidaat_6)
        kandidatenlijst1.append(lijst.kandidaat_7)
        kandidatenlijst1.append(lijst.kandidaat_8)
        kandidatenlijst1.append(lijst.kandidaat_9)
        kandidatenlijst1.append(lijst.kandidaat_10)
    elif len(kandidatenlijst2) <= 9:
        kandidatenlijst2.append(lijst.kandidaat_1)
        kandidatenlijst2.append(lijst.kandidaat_2)
        kandidatenlijst2.append(lijst.kandidaat_3)
        kandidatenlijst2.append(lijst.kandidaat_4)
        kandidatenlijst2.append(lijst.kandidaat_5)
        kandidatenlijst2.append(lijst.kandidaat_6)
        kandidatenlijst2.append(lijst.kandidaat_7)
        kandidatenlijst2.append(lijst.kandidaat_8)
        kandidatenlijst2.append(lijst.kandidaat_9)
        kandidatenlijst2.append(lijst.kandidaat_10)
    elif len(kandidatenlijst3) <= 9:
        kandidatenlijst3.append(lijst.kandidaat_1)
        kandidatenlijst3.append(lijst.kandidaat_2)
        kandidatenlijst3.append(lijst.kandidaat_3)
        kandidatenlijst3.append(lijst.kandidaat_4)
        kandidatenlijst3.append(lijst.kandidaat_5)
        kandidatenlijst3.append(lijst.kandidaat_6)
        kandidatenlijst3.append(lijst.kandidaat_7)
        kandidatenlijst3.append(lijst.kandidaat_8)
        kandidatenlijst3.append(lijst.kandidaat_9)
        kandidatenlijst3.append(lijst.kandidaat_10)
    elif len(kandidatenlijst4) <= 9:
        kandidatenlijst4.append(lijst.kandidaat_1)
        kandidatenlijst4.append(lijst.kandidaat_2)
        kandidatenlijst4.append(lijst.kandidaat_3)
        kandidatenlijst4.append(lijst.kandidaat_4)
        kandidatenlijst4.append(lijst.kandidaat_5)
        kandidatenlijst4.append(lijst.kandidaat_6)
        kandidatenlijst4.append(lijst.kandidaat_7)
        kandidatenlijst4.append(lijst.kandidaat_8)
        kandidatenlijst4.append(lijst.kandidaat_9)
        kandidatenlijst4.append(lijst.kandidaat_10)
    elif len(kandidatenlijst5) <= 9:
        kandidatenlijst5.append(lijst.kandidaat_1)
        kandidatenlijst5.append(lijst.kandidaat_2)
        kandidatenlijst5.append(lijst.kandidaat_3)
        kandidatenlijst5.append(lijst.kandidaat_4)
        kandidatenlijst5.append(lijst.kandidaat_5)
        kandidatenlijst5.append(lijst.kandidaat_6)
        kandidatenlijst5.append(lijst.kandidaat_7)
        kandidatenlijst5.append(lijst.kandidaat_8)
        kandidatenlijst5.append(lijst.kandidaat_9)
        kandidatenlijst5.append(lijst.kandidaat_10)
