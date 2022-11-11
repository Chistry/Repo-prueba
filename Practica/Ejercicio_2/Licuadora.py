from Electrodomestico import Electrodomestrico

class Licuadora():
    def __init__(self, codigo, precio, marca, color, material_vaso, velocidades):
        Electrodomestrico.__init__(self, codigo, precio, marca, color)
        self.material_vaso = str(material_vaso)
        self.velocidades = int(velocidades)