
import numpy as np



def crear_ventas():

    # Matriz:
    # 12 vendedores
    # 6 meses

    ventas = np.random.randint(
        1000,
        8000,
        (12,6)
    )

    return ventas




def analizar_ventas(ventas):


    # Total vendido por vendedor
    total_vendedor = np.sum(
        ventas,
        axis=1
    )


    # Total vendido por mes
    total_mes = np.sum(
        ventas,
        axis=0
    )


    # Mejor vendedor
    mejor = np.argmax(
        total_vendedor
    ) + 1


    # Peor vendedor
    peor = np.argmin(
        total_vendedor
    ) + 1


    # Promedio mensual
    promedio = np.mean(
        ventas,
        axis=0
    )


    print("\n====== MATRIZ VENTAS ======")

    print(ventas)

    print("\nVentas por vendedor:")
    print(total_vendedor)

    print("\nVentas por mes:")
    print(total_mes)

    print("\nMejor vendedor:", mejor)

    print("Peor vendedor:", peor)

    print("\nPromedio mensual:")
    print(promedio)




def main():

    ventas = crear_ventas()

    analizar_ventas(
        ventas
    )


main()