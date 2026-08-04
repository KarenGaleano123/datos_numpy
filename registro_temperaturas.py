
# Importamos la librería NumPy y la renombramos como np
import numpy as np


# Función para generar las temperaturas del mes
def generar_temperaturas():
    """
    Genera 30 temperaturas aleatorias entre 10 y 40 grados.
    Retorna un arreglo NumPy.
    """

    # Genera 30 números enteros aleatorios entre 10 y 40
    temperaturas = np.random.randint(10, 41, 30)

    # Retorna el arreglo generado
    return temperaturas


# Función para analizar las temperaturas
def analizar_temperaturas(temperaturas):
    """
    Calcula estadísticas básicas del arreglo.
    """

    # Calcula la temperatura promedio
    promedio = np.mean(temperaturas)

    # Obtiene la temperatura máxima
    maxima = np.max(temperaturas)

    # Obtiene la temperatura mínima
    minima = np.min(temperaturas)

    # Calcula la desviación estándar
    desviacion = np.std(temperaturas)

    # Calcula la varianza
    varianza = np.var(temperaturas)

    # Obtiene la posición del valor más alto
    dia_mas_caluroso = np.argmax(temperaturas) + 1

    # Obtiene la posición del valor más bajo
    dia_mas_frio = np.argmin(temperaturas) + 1

    # Mostrar resultados
    print("\n========== REPORTE DE TEMPERATURAS ==========")

    print("\nTemperaturas registradas:")
    print(temperaturas)

    print(f"\nTemperatura promedio: {promedio:.2f} °C")

    print(f"Temperatura máxima: {maxima} °C")

    print(f"Temperatura mínima: {minima} °C")

    print(f"Desviación estándar: {desviacion:.2f}")

    print(f"Varianza: {varianza:.2f}")

    print(
        f"Día más caluroso: Día {dia_mas_caluroso} "
        f"con {maxima} °C"
    )

    print(
        f"Día más frío: Día {dia_mas_frio} "
        f"con {minima} °C"
    )


# Función principal
def main():
    """
    Ejecuta el programa principal.
    """

    # Genera las temperaturas
    temperaturas = generar_temperaturas()

    # Analiza las temperaturas
    analizar_temperaturas(temperaturas)


# Punto de entrada del programa
if __name__ == "__main__":
    main()