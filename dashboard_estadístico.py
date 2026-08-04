
# Importamos la librería NumPy
import numpy as np





# Función para crear una matriz
def crear_matriz():
    """
    Crea una matriz de ejemplo para analizar.

    La matriz puede cambiarse por cualquier
    conjunto de datos.
    """


    # Generamos una matriz aleatoria
    # de 5 filas y 4 columnas.
    matriz = np.random.randint(
        1,
        100,
        (5, 4)
    )


    # Retornamos la matriz creada
    return matriz





# Función encargada de generar el reporte
def generar_reporte(matriz):
    """
    Analiza cualquier matriz y muestra
    información estadística.
    """



    # Obtiene las dimensiones de la matriz.
    dimension = matriz.shape



    # Obtiene el número de filas.
    filas = matriz.shape[0]



    # Obtiene el número de columnas.
    columnas = matriz.shape[1]



    # Calcula la cantidad total de datos.
    total_datos = matriz.size



    # Encuentra el valor máximo.
    maximo = np.max(
        matriz
    )



    # Encuentra el valor mínimo.
    minimo = np.min(
        matriz
    )



    # Calcula el promedio.
    promedio = np.mean(
        matriz
    )



    # Calcula la mediana.
    mediana = np.median(
        matriz
    )



    # Calcula la varianza.
    varianza = np.var(
        matriz
    )



    # Calcula la desviación estándar.
    desviacion = np.std(
        matriz
    )



    # Mostrar el reporte

    print("\n========== DASHBOARD ESTADÍSTICO ==========")


    print("\nMatriz analizada:")
    print(matriz)



    print("\n========== INFORMACIÓN GENERAL ==========")


    print(
        "Dimensión de la matriz:",
        dimension
    )


    print(
        "Número de filas:",
        filas
    )


    print(
        "Número de columnas:",
        columnas
    )


    print(
        "Total de datos:",
        total_datos
    )



    print("\n========== ANÁLISIS ESTADÍSTICO ==========")


    print(
        "Valor máximo:",
        maximo
    )


    print(
        "Valor mínimo:",
        minimo
    )


    print(
        "Promedio:",
        f"{promedio:.2f}"
    )


    print(
        "Mediana:",
        mediana
    )


    print(
        "Varianza:",
        f"{varianza:.2f}"
    )


    print(
        "Desviación estándar:",
        f"{desviacion:.2f}"
    )







# Función principal
def main():
    """
    Ejecuta el programa completo.
    """


    # Crear la matriz que será analizada
    matriz = crear_matriz()


    # Generar el reporte estadístico
    generar_reporte(
        matriz
    )





# Punto de inicio del programa
if __name__ == "__main__":

    main()