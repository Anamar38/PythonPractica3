import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

class Rectangulo:
    def __init__(self, largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
