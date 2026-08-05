
import numpy as np


# Crear matriz de inventario
def crear_inventario():

    # 15 productos x 8 sucursales
    inventario = np.random.randint(
        0,
        500,
        (15, 8)
    )

    return inventario


# Analizar inventario
def analizar(inventario):

    producto_mayor = np.argmax(
        np.sum(inventario, axis=1)
    ) + 1

    sucursal_menor = np.argmin(
        np.sum(inventario, axis=0)
    ) + 1

    total = np.sum(inventario)

    promedio = np.mean(inventario)

    agotados = np.where(
        inventario == 0
    )

    print("\n====== INVENTARIO ======")
    print(inventario)

    print("\nProducto con mayor existencia:", producto_mayor)
    print("Sucursal con menor inventario:", sucursal_menor)
    print("Inventario total:", total)
    print("Inventario promedio:", round(promedio, 2))
    print("Productos agotados:", agotados)


def main():

    inventario = crear_inventario()

    analizar(inventario)


main()