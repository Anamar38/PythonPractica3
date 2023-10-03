def ingresar_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = map(int, fraccion.split('/'))

            if x <= y and y != 0:
                return x, y
            else:
                print("Error: X debe ser menor o igual a Y, y Y no puede ser 0. Inténtelo de nuevo.")
        except ValueError:
            print("Error: Ingrese una fracción válida. Inténtelo de nuevo.")
        except ZeroDivisionError:
            print("Error: Y no puede ser 0. Inténtelo de nuevo.")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100

    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return f'{round(porcentaje)}%'

def main():
    x, y = ingresar_fraccion()
    resultado = calcular_porcentaje(x, y)

    print(f"La cantidad de combustible en el tanque es: {resultado}")

if __name__ == "__main__":
    main()
