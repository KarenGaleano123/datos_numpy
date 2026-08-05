
import numpy as np


# Crear matriz
def crear_matriz():

    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))

    return np.random.randint(
        1,
        100,
        (filas, columnas)
    )


# Generar reporte
def reporte(datos):

    print("\n====== DASHBOARD ======")

    print("Matriz:")
    print(datos)

    print("\nDimensión:",
          datos.shape)

    print("Filas:",
          datos.shape[0])

    print("Columnas:",
          datos.shape[1])

    print("Total datos:",
          datos.size)

    print("Máximo:",
          np.max(datos))

    print("Mínimo:",
          np.min(datos))

    print("Promedio:",
          round(np.mean(datos), 2))

    print("Mediana:",
          np.median(datos))

    print("Varianza:",
          round(np.var(datos), 2))

    print("Desviación:",
          round(np.std(datos), 2))


def main():

    matriz = crear_matriz()

    reporte(matriz)


main()