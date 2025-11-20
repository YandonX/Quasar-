import json
import csv

NOMBRE_ARCHIVO_BASE = "inventario"
inventario = {}

def obtener_datos_producto():
    while True:
        nombre = input("Nombre del producto: ").strip().capitalize()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        try:
            precio = float(input("Precio unitario: $"))
            cantidad = int(input("Cantidad: "))
            if precio <= 0 or cantidad < 0:
                print("El precio debe ser positivo y la cantidad no negativa.")
                continue
            return nombre, precio, cantidad
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números correctos.")
        except KeyboardInterrupt:
            # Manejo de Ctrl+C durante la entrada de datos
            print("\nOperación cancelada.")
            return None, None, None

def agregar_producto():
    nombre, precio, cantidad = obtener_datos_producto()
    
    if nombre and precio is not None:
        if nombre in inventario:
            inventario[nombre]['cantidad'] += cantidad
            print(f"Producto '{nombre}' actualizado. Nueva cantidad: {inventario[nombre]['cantidad']}")
        else:
            inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
            print(f"Producto '{nombre}' agregado exitosamente.")

def editar_producto():
    nombre = input("Ingrese el nombre del producto a editar: ").strip().capitalize()
    if nombre not in inventario:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")
        return

    print(f"\n--- Editando: {nombre} (Precio actual: ${inventario[nombre]['precio']}, Cantidad actual: {inventario[nombre]['cantidad']}) ---")

    nuevo_precio_str = input("Ingrese el nuevo precio (deje vacío para no cambiar): $")
    if nuevo_precio_str:
        try:
            nuevo_precio = float(nuevo_precio_str)
            if nuevo_precio > 0:
                inventario[nombre]['precio'] = nuevo_precio
                print(f"Precio actualizado a ${nuevo_precio}.")
            else:
                print("Precio inválido. No se realizó el cambio.")
        except ValueError:
            print("Entrada de precio inválida. Debe ser un número.")

    nueva_cantidad_str = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
    if nueva_cantidad_str:
        try:
            nueva_cantidad = int(nueva_cantidad_str)
            if nueva_cantidad >= 0:
                inventario[nombre]['cantidad'] = nueva_cantidad
                print(f"Cantidad actualizada a {nueva_cantidad}.")
            else:
                print("Cantidad inválida. No se realizó el cambio.")
        except ValueError:
            print("Entrada de cantidad inválida. Debe ser un número entero.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print(f"Error: El producto '{nombre}' no se encuentra en el inventario.")

def mostrar_inventario():
    if not inventario:
        print("\n--- El inventario está vacío. ---")
        return

    print("\n--- Inventario Actual ---")
    encabezados = ["PRODUCTO", "PRECIO ($)", "CANTIDAD", "VALOR TOTAL ($)"]
    print("-" * 60)
    print(f"{encabezados[0]:<20} | {encabezados[1]:>10} | {encabezados[2]:>8} | {encabezados[3]:>15}")
    print("-" * 60)

    for nombre, detalles in inventario.items():
        precio = detalles['precio']
        cantidad = detalles['cantidad']
        valor_total_producto = precio * cantidad
        print(f"{nombre:<20} | {precio:>10.2f} | {cantidad:>8} | {valor_total_producto:>15.2f}")

    print("-" * 60)

def calcular_estadisticas():
    if not inventario:
        print("\n--- No hay productos para calcular estadísticas. ---")
        return

    valor_total = 0.0
    cantidad_total = 0
    tipos_productos = 0

    print("\n--- Estadísticas del Inventario ---")

    for nombre, detalles in inventario.items():
        valor_producto = detalles['precio'] * detalles['cantidad']
        valor_total += valor_producto
        cantidad_total += detalles['cantidad']
        tipos_productos += 1
        print(f" - {nombre}: {detalles['cantidad']} unidades @ ${detalles['precio']:.2f} c/u. Valor: ${valor_producto:.2f}")

    print("-" * 40)
    print(f"Tipos de productos en total: {tipos_productos}")
    print(f"Cantidad total de productos: {cantidad_total}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print("-" * 40)

def obtener_opcion_formato():
    while True:
        formato = input("Ingrese el formato (txt, json, csv): ").lower().strip()
        if formato in ['txt', 'json', 'csv']:
            return formato
        print("Formato no válido. Intente de nuevo.")

def guardar_datos(formato):
    nombre_archivo = f"{NOMBRE_ARCHIVO_BASE}.{formato}"
    try:
        if formato == 'json':
            with open(nombre_archivo, 'w') as f:
                json.dump(inventario, f, indent=4)
            print(f"Inventario guardado en '{nombre_archivo}' (JSON).")

        elif formato == 'csv':
            with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['nombre', 'precio', 'cantidad']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for nombre, detalles in inventario.items():
                    writer.writerow({
                        'nombre': nombre,
                        'precio': detalles['precio'],
                        'cantidad': detalles['cantidad']
                    })
            print(f"Inventario guardado en '{nombre_archivo}' (CSV).")

        elif formato == 'txt':
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                for nombre, detalles in inventario.items():
                    f.write(f"{nombre}|{detalles['precio']}|{detalles['cantidad']}\n")
            print(f"Inventario guardado en '{nombre_archivo}' (TXT).")

    except IOError as e:
        print(f"Error al guardar el archivo: {e}")

def cargar_datos(formato):
    global inventario
    nombre_archivo = f"{NOMBRE_ARCHIVO_BASE}.{formato}"
    
    try:
        if formato == 'json':
            with open(nombre_archivo, 'r') as f:
                data = json.load(f)
                inventario = {
                    k: {'precio': float(v['precio']), 'cantidad': int(v['cantidad'])}
                    for k, v in data.items()
                }
            print(f"Inventario cargado desde '{nombre_archivo}' (JSON).")

        elif formato == 'csv':
            nuevo_inventario = {}
            with open(nombre_archivo, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    nombre = row['nombre']
                    precio = float(row['precio'])
                    cantidad = int(row['cantidad'])
                    nuevo_inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
            inventario = nuevo_inventario
            print(f"Inventario cargado desde '{nombre_archivo}' (CSV).")

        elif formato == 'txt':
            nuevo_inventario = {}
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            nombre, precio_str, cantidad_str = line.split('|')
                            nuevo_inventario[nombre] = {
                                'precio': float(precio_str),
                                'cantidad': int(cantidad_str)
                            }
                        except ValueError:
                            print(f"Línea con formato incorrecto en TXT: {line}")
                            continue
            inventario = nuevo_inventario
            print(f"Inventario cargado desde '{nombre_archivo}' (TXT).")

    except FileNotFoundError:
        print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con inventario vacío.")

    except (IOError, json.JSONDecodeError, ValueError) as e:
        print(f"Error al procesar los datos de '{nombre_archivo}': {e}")

def menu_principal():
    
    print("--- Bienvenido al Gestor de Inventario Multiformato ---")
    print("\n--- Carga Inicial de Datos ---")
    formato_inicial = obtener_opcion_formato()
    cargar_datos(formato_inicial)
    
    opcion = 0
    while opcion != 9:
        print("\n" + "="*45)
        print("1- Agregar Producto")
        print("2- Mostrar Inventario")
        print("3- Calcular Estadísticas")
        print("4- Editar Producto")
        print("5- Eliminar Producto")
        print("6- Guardar Inventario (Multiformato)")
        print("7- Cargar Inventario (Multiformato)")
        print("9- Salir y Guardar")
        print("="*45)

        try:
            opcion = int(input("Ingrese su opción: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número del menú.")
            continue

        if opcion == 1:
            agregar_producto()

        elif opcion == 2:
            mostrar_inventario()

        elif opcion == 3:
            calcular_estadisticas()

        elif opcion == 4:
            editar_producto()

        elif opcion == 5:
            eliminar_producto()

        elif opcion == 6:
            formato = obtener_opcion_formato()
            guardar_datos(formato)

        elif opcion == 7:
            formato = obtener_opcion_formato()
            cargar_datos(formato)

        elif opcion == 9:
            print("\n--- Guardado Final ---")
            formato_guardado = obtener_opcion_formato()
            guardar_datos(formato_guardado)
            print("\n¡Gracias por usar el gestor! Saliendo del programa...")

        else:
            print("Opción no reconocida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()