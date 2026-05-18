
def ingresar_calificaciones():
    """
    Permite ingresar materias y calificaciones.
    Retorna dos listas:
    - materias
    - calificaciones
    """

    materias = []
    calificaciones = []

    continuar = "s"

    while continuar.lower() == "s":

        # Ingreso del nombre de la materia
        materia = input("Ingrese el nombre de la materia: ").strip()

        # Validación
        while materia == "":
            print("Error: el nombre de la materia no puede estar vacío.")
            materia = input("Ingrese el nombre de la materia: ").strip()

        # Ingreso y validación de la calificación
        while True:
            try:
                nota = float(input("Ingrese la calificación (0 a 10): "))

                if 0 <= nota <= 10:
                    break
                else:
                    print("Error: la calificación debe estar entre 0 y 10.")

            except ValueError:
                print("Error: debe ingresar un número válido.")

        # Guardar datos en listas
        materias.append(materia)
        calificaciones.append(nota)

        # Preguntar si desea continuar con otra materia
        continuar = input("¿Desea ingresar otra materia? (s/n): ")

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Calcula y retorna el promedio de las calificaciones.
    """

    if len(calificaciones) == 0:
        return 0

    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)

    return promedio


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina materias aprobadas y reprobadas.
    Retorna dos listas con índices:
    - aprobadas
    - reprobadas
    """

    aprobadas = []
    reprobadas = []

    for i in range(len(calificaciones)):

        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra el índice de la nota más alta
    y el índice de la nota más baja.
    """

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


def main():

    print(" CALCULADORA DE PROMEDIOS ESCOLARES ")

    # Ingreso de datos
    materias, calificaciones = ingresar_calificaciones()

    # Verificar si se ingresaron materias
    if len(materias) == 0:
        print("\nNo se ingresaron materias.")
        print("Fin del programa.")
        return

    # Procesamiento
    promedio = calcular_promedio(calificaciones)

    aprobadas, reprobadas = determinar_estado(calificaciones)

    indice_max, indice_min = encontrar_extremos(calificaciones)

    # Mostrar resumen final
    print("\nRESUMEN")

    print("\nMaterias y calificaciones:")

    for i in range(len(materias)):
        print(f"- {materias[i]}: {calificaciones[i]}")

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas:")

    if len(aprobadas) > 0:
        for i in aprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")

    print("\nMaterias reprobadas:")

    if len(reprobadas) > 0:
        for i in reprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")

    print("\nMejor calificación:")
    print(f"{materias[indice_max]} ({calificaciones[indice_max]})")

    print("\nPeor calificación:")
    print(f"{materias[indice_min]} ({calificaciones[indice_min]})")

    print("\nGracias por utilizar el programa.")


# Ejecución principal
if __name__ == "__main__":
    main()