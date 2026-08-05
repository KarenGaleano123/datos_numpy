
import numpy as np


# Crear imagen
def crear_imagen():

    return np.random.randint(
        0,
        256,
        (15, 15)
    )


# Aumentar brillo
def aumentar_brillo(imagen):

    return np.clip(
        imagen + 50,
        0,
        255
    )


# Disminuir brillo
def disminuir_brillo(imagen):

    return np.clip(
        imagen - 50,
        0,
        255
    )


# Invertir colores
def invertir(imagen):

    return 255 - imagen


# Programa principal
def main():

    imagen = crear_imagen()

    print("\nIMAGEN ORIGINAL")
    print(imagen)

    print("\nMAS BRILLO")
    print(aumentar_brillo(imagen))

    print("\nMENOS BRILLO")
    print(disminuir_brillo(imagen))

    print("\nIMAGEN INVERTIDA")
    print(invertir(imagen))

    print("\nTRANSPUESTA")
    print(np.transpose(imagen))


main()