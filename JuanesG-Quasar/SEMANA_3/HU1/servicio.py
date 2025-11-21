def agregar_producto(inventario, nombre, cantidad, precio):
    """Agrega un producto al inventario."""
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print(f"Producto '{nombre}' agregado.")

def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("Inventario vacío")
        return
    print("Nombre | Cantidad | Precio")
    for item in inventario:
        print(f"{item['nombre']} | {item['cantidad']} | {item['precio']}")

def buscar_producto(inventario, nombre):
    """Busca productos por nombre."""
    encontrados = [p for p in inventario if nombre.lower() in p["nombre"].lower()]
    if not encontrados:
        print(f"No se encontró '{nombre}'")
    return encontrados

def actualizar_producto(inventario, nombre, nueva_cantidad=None, nuevo_precio=None):
    """Actualiza un producto si existe."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            if nueva_cantidad is not None:
                p["cantidad"] = nueva_cantidad
            if nuevo_precio is not None:
                p["precio"] = nuevo_precio
            print(f"Producto '{nombre}' actualizado")
            return
    print(f"Producto '{nombre}' no encontrado")

def eliminar_producto(inventario, nombre):
    """Elimina un producto por nombre."""
    for i, p in enumerate(inventario):
        if p["nombre"].lower() == nombre.lower():
            inventario.pop(i)
            print(f"Producto '{nombre}' eliminado")
            return
    print(f"Producto '{nombre}' no encontrado")

def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario."""
    if not inventario:
        return {"unidades_totales": 0, "valor_total": 0, "producto_mas_caro": None, "producto_mayor_stock": None}

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["cantidad"] * p["precio"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }
