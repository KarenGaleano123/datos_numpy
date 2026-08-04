
# Importamos la librería NumPy
import numpy as np



# Función para generar la producción
def generar_produccion():
    """
    Genera una matriz con la producción diaria.

    Filas:
    Representan días.

    Columnas:
    Representan líneas de producción.
    """


    # Generamos una matriz aleatoria
    # 30 días y 3 líneas
    produccion = np.random.randint(
        100,
        1000,
        (30, 3)
    )


    # Retornamos la matriz creada
    return produccion





# Función para analizar la producción
def analizar_produccion(produccion):
    """
    Realiza los cálculos solicitados.
    """


    # Calcula la producción diaria.
    # Suma las tres líneas por cada día.
    produccion_diaria = np.sum(
        produccion,
        axis=1
    )



    # Calcula la producción total
    # de cada línea.
    produccion_linea = np.sum(
        produccion,
        axis=0
    )



    # Calcula la producción semanal.
    # Divide los días en semanas de 7 días.
    semanas = np.reshape(
        produccion[:28],
        (4, 7, 3)
    )



    # Suma la producción de cada semana.
    produccion_semanal = np.sum(
        semanas,
        axis=1
    )



    # Calcula la producción mensual.
    produccion_mensual = np.sum(
        produccion
    )



    # Busca la línea con mayor producción.
    linea_productiva = np.argmax(
        produccion_linea
    )



    # Mostrar resultados

    print("\n========== PRODUCCIÓN ==========")

    print("\nMatriz de producción:")
    print(produccion)



    print("\n========== PRODUCCIÓN DIARIA ==========")

    for dia, cantidad in enumerate(produccion_diaria):

        print(
            f"Día {dia + 1}: "
            f"{cantidad} unidades"
        )



    print("\n========== PRODUCCIÓN SEMANAL ==========")

    for semana, cantidad in enumerate(produccion_semanal):

        total = np.sum(cantidad)

        print(
            f"Semana {semana + 1}: "
            f"{total} unidades"
        )



    print("\n========== PRODUCCIÓN MENSUAL ==========")

    print(
        f"Total producido: "
        f"{produccion_mensual} unidades"
    )



    print("\n========== LÍNEA MÁS PRODUCTIVA ==========")

    print(
        f"Línea {linea_productiva + 1}"
    )

    print(
        f"Producción total: "
        f"{produccion_linea[linea_productiva]} unidades"
    )





# Función principal
def main():

    """
    Ejecuta el programa completo.
    """


    # Genera los datos de producción
    produccion = generar_produccion()


    # Analiza la información
    analizar_produccion(produccion)




# Inicio del programa
if __name__ == "__main__":

    main()