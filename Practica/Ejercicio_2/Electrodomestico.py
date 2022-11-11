class Electrodomestrico():
    electrodomestricos = []
    def __init__(self, codigo, precio, marca, color):
        self.codigo = codigo
        self.precio= precio
        self.marca= marca
        self.color= color
        
    def mostrar(self):
        print(f"Id: {self.codigo}")
        print(f"Precio: {self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")

