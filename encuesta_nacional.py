
import numpy as np


# Generar edades
def generar():

    return np.random.randint(
        1,
        101,
        500
    )


# Calcular moda
def moda(edades):

    valores, frecuencia = np.unique(
        edades,
        return_counts=True
    )

    return valores[
        np.argmax(frecuencia)
    ]


# Analizar edades
def analizar(edades):

    print("\n====== ENCUESTA ======")

    print("Promedio:",
          round(np.mean(edades), 2))

    print("Mediana:",
          np.median(edades))

    print("Moda:",
          moda(edades))

    print("Máxima:",
          np.max(edades))

    print("Mínima:",
          np.min(edades))

    print("Mayores de edad:",
          np.sum(edades >= 18))


def main():

    edades = generar()

    analizar(edades)


main()