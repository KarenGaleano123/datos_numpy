
import numpy as np



def crear_notas():

    # 40 estudiantes
    # 5 materias

    notas = np.random.randint(
        0,
        101,
        (40,5)
    )

    return notas





def analizar(notas):


    # Promedio por estudiante

    promedio_estudiante = np.mean(
        notas,
        axis=1
    )


    # Promedio por asignatura

    promedio_asignatura = np.mean(
        notas,
        axis=0
    )


    # Mejor estudiante

    mejor = np.argmax(
        promedio_estudiante
    ) + 1


    # Peor estudiante

    peor = np.argmin(
        promedio_estudiante
    ) + 1


    # Aprobados

    aprobados = np.sum(
        promedio_estudiante >= 60
    )


    # Reprobados

    reprobados = np.sum(
        promedio_estudiante < 60
    )


    print("\n====== ANALISIS ACADEMICO ======")

    print(notas)

    print("\nPromedio estudiantes:")
    print(promedio_estudiante)

    print("\nPromedio asignaturas:")
    print(promedio_asignatura)

    print("\nMejor estudiante:", mejor)

    print("Peor estudiante:", peor)

    print("Aprobados:", aprobados)

    print("Reprobados:", reprobados)




def main():

    notas = crear_notas()

    analizar(
        notas
    )


main()