
# Importamos la librería NumPy
import numpy as np




# Función para generar las edades

def generar_edades():
    """
    Genera un arreglo con 500 edades aleatorias
    entre 1 y 100 años.
    """

    # Creamos 500 edades aleatorias enteras
    edades = np.random.randint(
        1,
        101,
        500
    )

    # Retornamos las edades generadas
    return edades





# Función para calcular la moda

def calcular_moda(edades):
    """
    Calcula la edad que más se repite
    utilizando NumPy.
    """

    # Obtenemos los valores únicos
    # y la cantidad de veces que aparecen
    valores, cantidades = np.unique(
        edades,
        return_counts=True
    )


    # Buscamos la posición del número
    # que más veces aparece
    posicion = np.argmax(
        cantidades
    )


    # Guardamos la edad con mayor frecuencia
    moda = valores[posicion]


    # Retornamos la moda
    return moda






# Función para analizar las edades

def analizar_edades(edades):
    """
    Realiza todos los cálculos estadísticos
    solicitados.
    """


    # Calculamos promedio de edades
    promedio = np.mean(
        edades
    )


    # Calculamos la mediana
    mediana = np.median(
        edades
    )


    # Calculamos la moda
    moda = calcular_moda(
        edades
    )


    # Buscamos la edad máxima
    edad_maxima = np.max(
        edades
    )


    # Buscamos la edad mínima
    edad_minima = np.min(
        edades
    )


    # Contamos personas mayores de edad
    # (18 años o más)
    mayores_edad = np.sum(
        edades >= 18
    )


    # Contamos menores de edad
    menores_edad = np.sum(
        edades < 18
    )



    
    # Mostrar resultados

    print("\n================================")
    print("     ENCUESTA NACIONAL")
    print("================================")


    print("\nEdades registradas:")
    print(edades)



    print("\n========== RESULTADOS ==========")


    print(
        "Promedio de edad:",
        round(promedio, 2),
        "años"
    )


    print(
        "Mediana:",
        mediana,
        "años"
    )


    print(
        "Moda:",
        moda,
        "años"
    )


    print(
        "Edad máxima:",
        edad_maxima,
        "años"
    )


    print(
        "Edad mínima:",
        edad_minima,
        "años"
    )


    print(
        "Cantidad de mayores de edad:",
        mayores_edad,
        "personas"
    )


    print(
        "Cantidad de menores de edad:",
        menores_edad,
        "personas"
    )






# Función principal

def main():
    """
    Ejecuta el programa.
    """


    # Generamos las edades
    edades = generar_edades()


    # Analizamos los datos
    analizar_edades(
        edades
    )






# Inicio del programa


if __name__ == "__main__":

    main()