from Electrodomestico import Electrodomestrico

class Nevera():
    def __init__(self, codigo, precio, marca, color, inc_congelador, compartimientos):
        Electrodomestrico.__init__(self, codigo, precio, marca, color)
        self.inc_congelador = bool(inc_congelador)
        self.compartimientos = int(compartimientos)