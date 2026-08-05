
import numpy as np


# Crear producción
def crear_produccion():

    produccion = np.random.randint(
        100,
        500,
        (30, 3)
    )

    return produccion


# Analizar producción
def analizar(datos):

    diaria = np.sum(
        datos,
        axis=1
    )

    semanal = [
        np.sum(
            diaria[i:i+7]
        )
        for i in range(0, 30, 7)
    ]

    mensual = np.sum(datos)

    mejor_linea = np.argmax(
        np.sum(datos, axis=0)
    ) + 1

    print("\n====== PRODUCCION ======")
    print(datos)

    print("\nProducción diaria:")
    print(diaria)

    print("\nProducción semanal:")
    print(semanal)

    print("\nProducción mensual:", mensual)

    print("Línea más productiva:", mejor_linea)


def main():

    datos = crear_produccion()

    analizar(datos)


main()