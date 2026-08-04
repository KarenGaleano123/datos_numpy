
# Importamos la librería NumPy
import numpy as np




# Función para crear la imagen
def crear_imagen():
    """
    Genera una imagen en escala de grises.

    Cada valor representa la intensidad
    de un píxel entre 0 y 255.
    """


    # Creamos una matriz de 15 filas y 15 columnas
    # con valores aleatorios entre 0 y 255.
    imagen = np.random.randint(
        0,
        256,
        (15, 15)
    )


    # Retornamos la imagen creada
    return imagen





# Función para aumentar el brillo
def aumentar_brillo(imagen):
    """
    Incrementa la intensidad de los píxeles
    para hacer la imagen más clara.
    """


    # Sumamos 50 a cada píxel
    imagen_brillante = imagen + 50



    # Limitamos los valores para que
    # no superen el máximo permitido (255).
    imagen_brillante = np.clip(
        imagen_brillante,
        0,
        255
    )


    # Retornamos la imagen modificada
    return imagen_brillante





# Función para disminuir el brillo
def disminuir_brillo(imagen):
    """
    Reduce la intensidad de los píxeles
    para oscurecer la imagen.
    """


    # Restamos 50 a cada píxel
    imagen_oscura = imagen - 50



    # Evitamos valores menores que 0.
    imagen_oscura = np.clip(
        imagen_oscura,
        0,
        255
    )


    # Retornamos la imagen modificada
    return imagen_oscura





# Función para invertir colores
def invertir_colores(imagen):
    """
    Invierte los tonos de la imagen.

    Negro pasa a blanco y blanco pasa a negro.
    """


    # Restamos cada valor a 255
    imagen_invertida = 255 - imagen


    # Retornamos la imagen invertida
    return imagen_invertida





# Función para obtener la transpuesta
def obtener_transpuesta(imagen):
    """
    Cambia las filas por columnas
    de la imagen.
    """


    # Aplicamos la transposición
    imagen_transpuesta = np.transpose(
        imagen
    )


    # Retornamos la nueva imagen
    return imagen_transpuesta





# Función principal del programa
def main():
    """
    Ejecuta todas las operaciones
    de procesamiento de imagen.
    """


    # Creamos la imagen original
    imagen = crear_imagen()



    # Aplicamos aumento de brillo
    imagen_brillante = aumentar_brillo(
        imagen
    )



    # Aplicamos disminución de brillo
    imagen_oscura = disminuir_brillo(
        imagen
    )



    # Invertimos los colores
    imagen_invertida = invertir_colores(
        imagen
    )



    # Obtenemos la imagen transpuesta
    imagen_transpuesta = obtener_transpuesta(
        imagen
    )



    # Mostrar resultados

    print("\n========== IMAGEN ORIGINAL ==========")

    print(imagen)



    print("\n========== IMAGEN CON MÁS BRILLO ==========")

    print(imagen_brillante)



    print("\n========== IMAGEN CON MENOS BRILLO ==========")

    print(imagen_oscura)



    print("\n========== IMAGEN INVERTIDA ==========")

    print(imagen_invertida)



    print("\n========== IMAGEN TRANSPUESTA ==========")

    print(imagen_transpuesta)






# Punto de inicio del programa
if __name__ == "__main__":

    main()