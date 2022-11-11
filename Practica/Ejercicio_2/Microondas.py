from Electrodomestico import Electrodomestrico

class Microondas():
    def __init__(self, codigo, precio, marca, color, control):
        Electrodomestrico.__init__(self, codigo, precio, marca, color)
        self.control = bool(control)