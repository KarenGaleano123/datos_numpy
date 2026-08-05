
# Importamos NumPy
import numpy as np


# Función para generar temperaturas
def generar_temperaturas():

    # Genera 30 temperaturas aleatorias
    temperaturas = np.random.randint(
        15,
        40,
        30
    )

    return temperaturas



# Función para analizar temperaturas
def analizar_temperaturas(datos):

    # Calcula promedio
    promedio = np.mean(datos)

    # Temperatura máxima
    maxima = np.max(datos)

    # Temperatura mínima
    minima = np.min(datos)

    # Desviación estándar
    desviacion = np.std(datos)

    # Varianza
    varianza = np.var(datos)

    # Día más caluroso
    dia_caluroso = np.argmax(datos) + 1

    # Día más frío
    dia_frio = np.argmin(datos) + 1


    print("\n====== TEMPERATURAS ======")
    print(datos)

    print("\nPromedio:", round(promedio,2))
    print("Máxima:", maxima)
    print("Mínima:", minima)
    print("Desviación:", round(desviacion,2))
    print("Varianza:", round(varianza,2))
    print("Día más caluroso:", dia_caluroso)
    print("Día más frío:", dia_frio)



# Programa principal
def main():

    temperaturas = generar_temperaturas()

    analizar_temperaturas(
        temperaturas
    )


main()