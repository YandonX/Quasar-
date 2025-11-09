""""
Carrito de compras.
"""

# Definición de la Colección Principal (Carrito de Compras)
# Clave: Nombre del producto (str)
# Valor: Diccionario de detalles {"cantidad": int, "precio_unitario": float}
carrito = {}


# --- FUNCIÓN 1: Agregar Producto ---
def agregar_producto(nombre, precio, cantidad):
    """Agrega un producto o actualiza la cantidad si ya existe."""
    nombre = nombre.strip().title()  # Limpia y capitaliza el nombre

    if nombre in carrito:
        # Si el producto ya está, solo suma la cantidad
        carrito[nombre]["cantidad"] += cantidad
        print(f"✅ Cantidad actualizada de '{nombre}'. Total: {carrito[nombre]['cantidad']}")
    else:
        # Si el producto es nuevo, lo agrega
        carrito[nombre] = {
            "cantidad": cantidad,
            "precio_unitario": precio
        }
        print(f"✅ '{nombre}' agregado al carrito.")


# --- FUNCIÓN 2: Eliminar Producto ---
def eliminar_producto(nombre):
    """Elimina un producto completamente del carrito."""
    nombre = nombre.strip().title()

    if nombre in carrito:
        del carrito[nombre]
        print(f" '{nombre}' eliminado del carrito.")
    else:
        print(f" El producto '{nombre}' no se encuentra en el carrito.")


# --- FUNCIÓN 3: Calcular Total ---
def calcular_total():
    """Calcula la suma total de todos los productos en el carrito."""
    total_general = 0

    # Uso de bucle 'for' para iterar sobre cada producto
    for nombre, detalles in carrito.items():
        subtotal = detalles["cantidad"] * detalles["precio_unitario"]
        total_general += subtotal

    return total_general


# --- FUNCIÓN 4: Mostrar Carrito ---
def mostrar_carrito():
    """Imprime el contenido actual del carrito en un formato legible."""
    if not carrito:
        print("\nEl carrito de compras está vacío.")
        return

    print("\n--- CONTENIDO DEL CARRITO ---")
    print(f"{'Producto':<20} {'Precio Unit.':>15} {'Cantidad':>10} {'Subtotal':>15}")
    print("-" * 60)

    # Bucle 'for' para mostrar los detalles de cada artículo
    for nombre, detalles in carrito.items():
        subtotal = detalles["cantidad"] * detalles["precio_unitario"]

        # Uso de f-strings con alineación para formato de tabla
        print(f"{nombre:<20} {detalles['precio_unitario']:>15.2f} {detalles['cantidad']:>10} {subtotal:>15.2f}")

    # Mostrar el total general
    total = calcular_total()
    print("-" * 60)
    print(f"{'Total a Pagar:':<45} {total:>15.2f}")
    print("------------------------------")


# =======================================================
# SIMULACIÓN DE USO
# =======================================================

print("--- INICIANDO COMPRA ---")

# 1. Agregando productos
agregar_producto("Camiseta Algodón", 19.99, 2)
agregar_producto("Pantalón Jeans", 45.50, 1)
agregar_producto("Camiseta Algodón", 19.99, 3)  # Agrega más cantidad
agregar_producto("Calcetines Deporte", 5.00, 4)

# 2. Mostrando el estado actual
mostrar_carrito()

# 3. Eliminando un producto
print("\n--- PROCESO DE ELIMINACIÓN ---")
eliminar_producto("Calcetines Deporte")

# 4. Mostrando el estado final y el total
mostrar_carrito()

# 5. Intentando eliminar un producto inexistente
eliminar_producto("Gorra")