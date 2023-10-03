def main():
    calificaciones= input("Introduce las calificaciones: ")

    calificaciones_lista = calificaciones.split(',')

    calificaciones_enteras = []
    for calificacion in calificaciones_lista:
        try:
            calificacion_entero = int(calificacion)
            calificaciones_enteras.append(calificacion_entero)
        except ValueError:
            print(f"Error: '{calificacion}' no es un número entero válido.")

    print("Calificaciones en formato entero:", calificaciones_enteras)

if __name__ == "__main__":
    main()
