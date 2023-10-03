class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print(f"Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas is not None:
            print(f"Notas: {self.notas}")

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

# Ejemplo de uso
alumno1 = Alumno("Ana Martinez", "753279")
alumno1.display()

alumno1.set_edad(20)
alumno1.set_notas([18,16,19])

alumno1.display()
