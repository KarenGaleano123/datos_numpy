
# Importamos la librería NumPy
import numpy as np



# Función encargada de crear la matriz de ventas
def generar_ventas():
    """
    Crea una matriz de 12 filas y 6 columnas.
    Cada fila representa un vendedor.
    Cada columna representa un mes.
    """

    # Generamos una matriz aleatoria de ventas
    # Valores entre 100000 y 5000000 pesos colombianos
    ventas = np.random.randint(
        100000,
        5000001,
        (12, 6)
    )


    # Retornamos la matriz creada
    return ventas



# Función encargada de realizar los cálculos
def analizar_ventas(ventas):
    """
    Realiza los análisis solicitados
    sobre la matriz de ventas.
    """


    # Suma las ventas de cada vendedor.
    # axis=1 significa que suma por filas.
    ventas_por_vendedor = np.sum(
        ventas,
        axis=1
    )


    # Suma las ventas realizadas cada mes.
    # axis=0 significa que suma por columnas.
    ventas_por_mes = np.sum(
        ventas,
        axis=0
    )


    # Calcula el promedio de ventas de cada mes.
    promedio_mensual = np.mean(
        ventas,
        axis=0
    )


    # Busca la posición del vendedor
    # con mayor cantidad de ventas.
    mejor_vendedor = np.argmax(
        ventas_por_vendedor
    )


    # Busca la posición del vendedor
    # con menor cantidad de ventas.
    peor_vendedor = np.argmin(
        ventas_por_vendedor
    )


    # Muestra la matriz generada
    print("\n========== MATRIZ DE VENTAS ==========")

    print("\nVentas de los 12 vendedores durante 6 meses:")
    print(ventas)


    # Mostrar ventas totales por vendedor
    print("\n========== TOTAL POR VENDEDOR ==========")

    for i, total in enumerate(ventas_por_vendedor):
        print(
            f"Vendedor {i + 1}: "
            f"${total:,}"
        )


    # Mostrar ventas totales por mes
    print("\n========== TOTAL POR MES ==========")

    for i, total in enumerate(ventas_por_mes):
        print(
            f"Mes {i + 1}: "
            f"${total:,}"
        )


    # Mostrar promedio mensual
    print("\n========== PROMEDIO MENSUAL ==========")

    for i, promedio in enumerate(promedio_mensual):
        print(
            f"Mes {i + 1}: "
            f"${promedio:,.2f}"
        )


    # Mostrar mejor vendedor
    print(
        "\nMejor vendedor:"
        f" Vendedor {mejor_vendedor + 1}"
    )

    print(
        "Total vendido: "
        f"${ventas_por_vendedor[mejor_vendedor]:,}"
    )


    # Mostrar peor vendedor
    print(
        "\nPeor vendedor:"
        f" Vendedor {peor_vendedor + 1}"
    )

    print(
        "Total vendido: "
        f"${ventas_por_vendedor[peor_vendedor]:,}"
    )




# Función principal del programa
def main():
    """
    Ejecuta el programa completo.
    """


    # Crear la matriz de ventas
    ventas = generar_ventas()


    # Enviar la matriz para realizar los cálculos
    analizar_ventas(ventas)




# Verifica que el programa se ejecute directamente
if __name__ == "__main__":

    # Ejecuta la función principal
    main()