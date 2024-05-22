from USBStick import usbstick


class Stembus:
    def __init__(self, usbstick):
        self.actief = False
        self.USB = usbstick

    def inialisatie(self):
        if self.USB.opstartcode1 == "START":
            self.actief = True
            if self.actief == True:
                print("Stembus is geinitialiseerd")

    def deinitialisatie(self):
        self.actief = False


stembus = Stembus(usbstick)
stembus.inialisatie()
