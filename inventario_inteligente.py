
# Importamos la librería NumPy
import numpy as np




# Función para generar la matriz del inventario
def generar_inventario():
    """
    Genera una matriz de inventario.

    Filas:
    Representan productos.

    Columnas:
    Representan sucursales.
    """


    # Creamos una matriz aleatoria
    # 15 productos y 8 sucursales
    inventario = np.random.randint(
        0,
        500,
        (15, 8)
    )


    # Retorna la matriz generada
    return inventario





# Función para analizar el inventario
def analizar_inventario(inventario):
    """
    Realiza los cálculos solicitados
    sobre el inventario.
    """


    # Calcula el inventario total
    # sumando todos los productos.
    inventario_total = np.sum(
        inventario
    )


    # Calcula el inventario promedio.
    inventario_promedio = np.mean(
        inventario
    )



    # Suma las existencias por producto.
    # axis=1 suma las filas.
    inventario_producto = np.sum(
        inventario,
        axis=1
    )



    # Suma las existencias por sucursal.
    # axis=0 suma las columnas.
    inventario_sucursal = np.sum(
        inventario,
        axis=0
    )



    # Busca el producto con mayor cantidad
    # de unidades disponibles.
    producto_mayor = np.argmax(
        inventario_producto
    )



    # Busca la sucursal con menor inventario.
    sucursal_menor = np.argmin(
        inventario_sucursal
    )



    # Encuentra productos agotados.
    # Un producto está agotado cuando
    # su inventario total es igual a cero.
    productos_agotados = np.where(
        inventario_producto == 0
    )



    # Mostrar resultados
    print("\n========== MATRIZ DE INVENTARIO ==========")

    print("\nInventario de productos por sucursal:")
    print(inventario)



    print("\n========== INVENTARIO TOTAL ==========")

    print(
        f"Inventario total disponible: "
        f"{inventario_total} unidades"
    )



    print(
        f"\nInventario promedio: "
        f"{inventario_promedio:.2f} unidades"
    )



    print("\n========== PRODUCTO CON MAYOR EXISTENCIA ==========")

    print(
        f"Producto {producto_mayor + 1}"
    )

    print(
        f"Cantidad disponible: "
        f"{inventario_producto[producto_mayor]} unidades"
    )



    print("\n========== SUCURSAL CON MENOR INVENTARIO ==========")

    print(
        f"Sucursal {sucursal_menor + 1}"
    )

    print(
        f"Cantidad disponible: "
        f"{inventario_sucursal[sucursal_menor]} unidades"
    )



    print("\n========== PRODUCTOS AGOTADOS ==========")


    # Verifica si existen productos agotados
    if len(productos_agotados[0]) > 0:


        # Recorre los productos encontrados
        for producto in productos_agotados[0]:

            print(
                f"Producto {producto + 1} "
                "sin existencias"
            )


    else:

        print(
            "No existen productos agotados"
        )






# Función principal
def main():
    """
    Ejecuta el programa.
    """


    # Genera la matriz de inventario
    inventario = generar_inventario()


    # Analiza los datos generados
    analizar_inventario(inventario)





# Punto de inicio del programa
if __name__ == "__main__":

    # Ejecuta la función principal
    main()