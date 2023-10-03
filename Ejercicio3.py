import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

mi_circulo = Circulo(3)

# Calculamos y mostramos el área del círculo
area_del_circulo = mi_circulo.calcular_area()
print(f"El área del círculo con radio {mi_circulo.radio} es: {area_del_circulo}")
