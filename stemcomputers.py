from USBStick import usbstick
from lijsten import Lijsten
from kiezers import Kiezers
from stembus import stembus
import random


class Stemcomputer:
    def __init__(self, code, usbstick, stembus):
        self.initialisatiecode = code
        self.actief = False
        self.usbstick = usbstick
        self.stembus = stembus

    def initialiseer(self):
        if self.stembus.actief == True:
            if self.initialisatiecode == self.usbstick.opstartcode2:
                self.actief = True
                print("Stemcomputer 1 is geïnitialiseerd")
            elif self.initialisatiecode == self.usbstick.opstartcode3:
                self.actief = True
                print("Stemcomputer 2 is geïnitialiseerd")
            elif self.initialisatiecode == self.usbstick.opstartcode4:
                self.actief = True
                print("Stemcomputer 3 is geïnitialiseerd")

    def stemmen(self):
        for kiezer in Kiezers:
            if kiezer.magstemmen == True:
                partij = random.choice(Lijsten)
                type_stem = random.randint(1, 2)
                if type_stem == 1:
                    partij.Lijst_stemmen()
                elif type_stem == 2:
                    partij.Voorkeur_stemmen()

    def maak_stembiljet(self):
        pass

    def deinitialiseer(self):
        self.actief = False
        print("Stemcomputer gedeïnitialiseerd")


stemcomputer1 = Stemcomputer(usbstick.opstartcode2, usbstick, stembus)
stemcomputer2 = Stemcomputer(usbstick.opstartcode3, usbstick, stembus)
stemcomputer3 = Stemcomputer(usbstick.opstartcode4, usbstick, stembus)


def initaliseer_stemcomputers():
    stemcomputer1.initialiseer()
    stemcomputer2.initialiseer()
    stemcomputer3.initialiseer()


def stem_simulatie():
    random_keuze = random.randint(1, 3)
    if random_keuze == 1:
        stemcomputer1.stemmen()
    elif random_keuze == 2:
        stemcomputer2.stemmen()
    elif random_keuze == 3:
        stemcomputer3.stemmen()


def deinitialiseer_stemcomputers():
    stemcomputer1.deinitialiseer()
    stemcomputer2.deinitialiseer()
    stemcomputer3.deinitialiseer()
