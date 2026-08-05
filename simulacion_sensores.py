
import numpy as np


# Generar mediciones
def generar():

    return np.random.uniform(
        10,
        100,
        100
    )


# Analizar sensores
def analizar(datos):

    fuera_rango = datos[
        (datos < 20)
        |
        (datos > 80)
    ]

    promedio = np.mean(datos)

    desviacion = np.std(datos)

    criticos = np.sum(
        (datos < 15)
        |
        (datos > 90)
    )

    print("\n====== SENSORES ======")

    print(datos)

    print("\nSensores fuera de rango:")
    print(fuera_rango)

    print("\nPromedio:", round(promedio, 2))

    print("Desviación:", round(desviacion, 2))

    print("Sensores críticos:", criticos)


def main():

    datos = generar()

    analizar(datos)


main()