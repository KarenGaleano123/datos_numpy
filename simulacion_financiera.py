
# Importamos la librería NumPy
import numpy as np




# Función para generar los precios
def generar_precios():
    """
    Genera los precios de una acción durante 100 días.

    Los valores representan precios en pesos.
    """


    # Genera 100 precios aleatorios decimales
    # entre 5000 y 20000 pesos.
    precios = np.random.uniform(
        5000,
        20000,
        100
    )


    # Retorna el arreglo generado
    return precios





# Función para analizar los precios
def analizar_accion(precios):
    """
    Realiza los cálculos financieros
    solicitados.
    """


    # Calcula el precio promedio
    # de la acción durante los 100 días.
    precio_promedio = np.mean(
        precios
    )



    # Obtiene el precio máximo alcanzado.
    precio_maximo = np.max(
        precios
    )



    # Obtiene el precio mínimo alcanzado.
    precio_minimo = np.min(
        precios
    )



    # Calcula la variación porcentual
    # entre el primer y último día.
    variacion_porcentual = (
        (precios[-1] - precios[0])
        /
        precios[0]
    ) * 100



    # Encuentra los días donde el precio
    # fue superior al promedio.
    dias_superiores = np.where(
        precios > precio_promedio
    )



    # Mostrar resultados

    print("\n========== SIMULACIÓN FINANCIERA ==========")


    print("\nPrecios registrados:")
    print(precios)



    print(
        "\nPrecio promedio:",
        f"${precio_promedio:,.2f}"
    )



    print(
        "Precio máximo:",
        f"${precio_maximo:,.2f}"
    )



    print(
        "Precio mínimo:",
        f"${precio_minimo:,.2f}"
    )



    print(
        "Variación porcentual:",
        f"{variacion_porcentual:.2f}%"
    )



    print(
        "\nDías donde el precio fue superior al promedio:"
    )


    # Recorre los días encontrados
    for dia in dias_superiores[0]:

        print(
            f"Día {dia + 1}: "
            f"${precios[dia]:,.2f}"
        )







# Función principal
def main():
    """
    Ejecuta el programa completo.
    """


    # Genera los precios de la acción
    precios = generar_precios()


    # Analiza los datos financieros
    analizar_accion(
        precios
    )





# Punto de inicio del programa
if __name__ == "__main__":

    main()