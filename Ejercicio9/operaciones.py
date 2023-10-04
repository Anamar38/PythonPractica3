def suma(x, y):
    try:
        resultado = float(x) + float(y)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido."

def resta(x, y):
    try:
        resultado = float(x) - float(y)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido."

def producto(x, y):
    try:
        resultado = float(x) * float(y)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido."

def division(x, y):
    try:
        if float(y) == 0:
            raise ZeroDivisionError
        resultado = float(x) / float(y)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."

# Pruebas 
if __name__ == "__main__":
    print("Suma:", suma(8, 3))
    print("Resta:", resta(5, 'u'))
    print("Producto:", producto('2', 4))
    print("División:", division(6, 0))
