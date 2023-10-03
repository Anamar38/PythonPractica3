
class Rectangulo:
    def __init__(self, largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

mi_rectangulo = Rectangulo(3,5)

# Calculamos y mostramos el área del rectangulo
area_del_rectangulo = mi_rectangulo.calcular_area()
print(f"El área del rectangulo con largo {mi_rectangulo.largo} y ancho {mi_rectangulo.ancho} es: {area_del_rectangulo}")
