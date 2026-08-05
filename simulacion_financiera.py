
import numpy as np


# Generar precios
def generar():

    return np.random.uniform(
        50,
        300,
        100
    )


# Analizar precios
def analizar(precios):

    promedio = np.mean(precios)

    variacion = (
        (precios[-1] - precios[0])
        /
        precios[0]
    ) * 100

    superiores = np.where(
        precios > promedio
    )[0] + 1

    print("\n====== FINANZAS ======")

    print("Promedio:",
          round(promedio, 2))

    print("Máximo:",
          round(np.max(precios), 2))

    print("Mínimo:",
          round(np.min(precios), 2))

    print("Variación %:",
          round(variacion, 2))

    print("Días sobre promedio:")
    print(superiores)


def main():

    precios = generar()

    analizar(precios)


main()