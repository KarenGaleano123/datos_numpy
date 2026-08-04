
# Importamos la librería NumPy
import numpy as np



# Función para generar las mediciones
def generar_mediciones():
    """
    Genera mediciones aleatorias de 100 sensores.

    Los valores representan mediciones
    de temperatura en grados Celsius.
    """


    # Genera 100 valores decimales aleatorios
    # entre 20 y 100 grados.
    mediciones = np.random.uniform(
        20,
        100,
        100
    )


    # Retorna el arreglo generado
    return mediciones




# Función para analizar los sensores
def analizar_sensores(mediciones):
    """
    Realiza el análisis de las mediciones
    obtenidas por los sensores.
    """


    # Calcula el promedio de todas
    # las mediciones.
    promedio = np.mean(
        mediciones
    )



    # Calcula la desviación estándar.
    desviacion = np.std(
        mediciones
    )



    # Define el rango máximo permitido.
    limite_maximo = 80



    # Encuentra sensores que superan
    # el límite permitido.
    sensores_fuera_rango = np.where(
        mediciones > limite_maximo
    )



    # Cuenta la cantidad de sensores críticos.
    cantidad_criticos = len(
        sensores_fuera_rango[0]
    )



    # Mostrar resultados

    print("\n========== SENSORES IoT ==========")


    print("\nMediciones registradas:")
    print(mediciones)



    print(
        "\nPromedio de mediciones:",
        f"{promedio:.2f} °C"
    )



    print(
        "Desviación estándar:",
        f"{desviacion:.2f}"
    )



    print(
        "\nSensores fuera del rango permitido:"
    )



    # Verifica si existen sensores críticos
    if cantidad_criticos > 0:


        # Recorre las posiciones encontradas
        for sensor in sensores_fuera_rango[0]:

            print(
                f"Sensor {sensor + 1}: "
                f"{mediciones[sensor]:.2f} °C"
            )


    else:

        print(
            "No existen sensores fuera del rango"
        )



    print(
        "\nCantidad de sensores críticos:",
        cantidad_criticos
    )






# Función principal del programa
def main():
    """
    Ejecuta todo el programa.
    """


    # Genera las mediciones
    mediciones = generar_mediciones()


    # Analiza los datos obtenidos
    analizar_sensores(
        mediciones
    )





# Inicio del programa
if __name__ == "__main__":

    main()