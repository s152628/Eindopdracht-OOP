class Chipkaart:
    def __init__(self):
        self.code = None

    def initialisatie(self, code):
        self.code = code
        print("De chipkaart heeft een code")

    def chipkaart_gebruikt(self):
        self.code = None
        print("De chipkaart is gebruikt geweest en de code is verwijdert")
