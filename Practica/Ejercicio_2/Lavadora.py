from Electrodomestico import Electrodomestrico

class Lavadora():
    def __init__(self, codigo, precio, marca, color, capacidad):
        Electrodomestrico.__init__(self, codigo, precio, marca, color)
        self.capacidad = capacidad

    def __str__(self):
        return(f'Codigo: {self.codigo}\nPrecio: {self.precio}\nMarca: {self.marca}\nColor: {self.color}\nCapacidad: {self.capacidad}')