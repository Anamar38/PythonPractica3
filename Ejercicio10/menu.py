# 1. Constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
OPCIONES_MENU = """
¿Qué quieres hacer? 
    1) Calcular el área de un circulo
    2) Calcular el área de un rectangulo
    3) Calcular el área de un cuadrado
    4) Salir.

Escribe una opción: """

# 2. Funciones y /o metodos

from areas import Circulo, Rectangulo, Cuadrado

def main():
    print(MENSAJE_BIENVENIDA)
    while True:
        opcion = input(OPCIONES_MENU)

        if opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio)
            print(f"Área del círculo: {circulo.calcular_area()}")

        elif opcion == '2':
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(f"Área del rectángulo: {rectangulo.calcular_area()}")

        elif opcion == '3':
            lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
            cuadrado = Cuadrado(lado_cuadrado)
            print(f"Área del cuadrado: {cuadrado.calcular_area()}")

        elif opcion == '4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# 3. Main
if __name__ == "__main__":
    main()

