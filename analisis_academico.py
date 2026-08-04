
# Importamos la librería NumPy
import numpy as np



# Función para generar las notas
def generar_calificaciones():
    """
    Genera una matriz de 40 estudiantes
    y 5 asignaturas.
    
    Cada valor representa una nota
    entre 0 y 100.
    """


    # Creamos una matriz aleatoria
    # 40 filas = estudiantes
    # 5 columnas = asignaturas
    calificaciones = np.random.randint(
        0,
        101,
        (40, 5)
    )


    # Retorna la matriz generada
    return calificaciones




# Función encargada de analizar las notas
def analizar_rendimiento(calificaciones):
    """
    Realiza los cálculos académicos
    solicitados.
    """


    # Calcula el promedio de cada estudiante.
    # axis=1 indica que trabaja por filas.
    promedio_estudiante = np.mean(
        calificaciones,
        axis=1
    )


    # Calcula el promedio de cada asignatura.
    # axis=0 indica que trabaja por columnas.
    promedio_asignatura = np.mean(
        calificaciones,
        axis=0
    )


    # Busca el estudiante con mayor promedio.
    mejor_estudiante = np.argmax(
        promedio_estudiante
    )


    # Busca el estudiante con menor promedio.
    peor_estudiante = np.argmin(
        promedio_estudiante
    )


    # Cuenta los estudiantes aprobados.
    # La nota mínima para aprobar es 60.
    aprobados = np.sum(
        promedio_estudiante >= 60
    )


    # Calcula los estudiantes reprobados.
    reprobados = np.sum(
        promedio_estudiante < 60
    )



    # Mostrar la matriz completa
    print("\n========== MATRIZ ACADÉMICA ==========")

    print("\nCalificaciones de los estudiantes:")
    print(calificaciones)



    # Mostrar promedio por estudiante
    print("\n========== PROMEDIO POR ESTUDIANTE ==========")


    for i, promedio in enumerate(promedio_estudiante):

        print(
            f"Estudiante {i + 1}: "
            f"{promedio:.2f}"
        )



    # Mostrar promedio por asignatura
    print("\n========== PROMEDIO POR ASIGNATURA ==========")


    for i, promedio in enumerate(promedio_asignatura):

        print(
            f"Asignatura {i + 1}: "
            f"{promedio:.2f}"
        )



    # Mostrar mejor estudiante
    print(
        "\nMejor estudiante:"
        f" Estudiante {mejor_estudiante + 1}"
    )


    print(
        "Promedio obtenido:"
        f" {promedio_estudiante[mejor_estudiante]:.2f}"
    )



    # Mostrar peor estudiante
    print(
        "\nPeor estudiante:"
        f" Estudiante {peor_estudiante + 1}"
    )


    print(
        "Promedio obtenido:"
        f" {promedio_estudiante[peor_estudiante]:.2f}"
    )



    # Mostrar cantidad de aprobados
    print(
        "\nCantidad de estudiantes aprobados:",
        aprobados
    )


    # Mostrar cantidad de reprobados
    print(
        "Cantidad de estudiantes reprobados:",
        reprobados
    )





# Función principal
def main():
    """
    Ejecuta todo el programa.
    """


    # Genera la matriz de calificaciones
    calificaciones = generar_calificaciones()


    # Envía la matriz para analizarla
    analizar_rendimiento(calificaciones)




# Verifica que el archivo se ejecute directamente
if __name__ == "__main__":

    # Ejecuta el programa principal
    main()