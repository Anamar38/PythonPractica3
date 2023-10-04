class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        else:
            return "Sobre los ejes"

    def vector(self, segundo_punto):
        distancia_x = segundo_punto.x - self.x
        distancia_y = segundo_punto.y - self.y
        return Punto(distancia_x, distancia_y)

    def distancia(self, segundo_punto):
        distancia_x = self.x -segundo_punto.x
        distancia_y = self.y - segundo_punto.y
        return (distancia_x**2 + distancia_y**2)/2

punto_A = Punto(2, 3)
punto_B = Punto(8, 5)
punto_C = Punto(-6, -4)
punto_D = Punto(0, 0)

print("Punto A:", punto_A)
print("Punto B:", punto_B)
print("Punto C:", punto_C)
print("Punto D:", punto_D)

# Consultar cuadrantes
print("\nCuadrante de A:", punto_A.cuadrante())
print("Cuadrante de C:", punto_C.cuadrante())
print("Cuadrante de D:", punto_D.cuadrante())

# Vectores AB y BA
vector_AB = punto_A.vector(punto_B)
vector_BA = punto_B.vector(punto_A)

print("\nVector AB:", vector_AB)
print("Vector BA:", vector_BA)

# Crear un rectángulo utilizando los puntos A y B
class Rectangulo:
    def __init__(self, punto_A, punto_B):
        self.punto_A = punto_A
        self.punto_B = punto_B

    def base(self):
        return abs(self.punto_A.x - self.punto_B.x)

    def altura(self):
        return abs(self.punto_A.y - self.punto_B.y)

    def area(self):
        return self.base() * self.altura()

rectangulo_AB = Rectangulo(punto_A, punto_B)

print("\nBase del rectángulo AB:", rectangulo_AB.base())
print("Altura del rectángulo AB:", rectangulo_AB.altura())
print("Área del rectángulo AB:", rectangulo_AB.area())
