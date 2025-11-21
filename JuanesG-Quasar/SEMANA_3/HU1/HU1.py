from servicio import *
from archivo_csv import guardar_csv, cargar_csv

inventario = []
ARCHIVO_CSV= ("Inventario.csv")
def Menu():
    global inventario
    while True:
        opcion = input(
            "1. Agregar\n2. Mostrar\n3. Buscar\n4. Actualizar\n5. Eliminar\n6. Estadísticas\n7. Guardar CSV\n8. Cargar CSV\n9. Salir\nElige: "
        )
        if opcion == "1":
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario, nombre, cantidad, precio)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            encontrados = buscar_producto(inventario, nombre)
            for p in encontrados:
                print(p)
        elif opcion == "4":
            nombre = input("Nombre a actualizar: ")
            nueva_cant = input("Nueva cantidad (dejar vacío para omitir): ")
            nuevo_precio = input("Nuevo precio (dejar vacío para omitir): ")
            actualizar_producto(
                inventario,
                nombre,
                nueva_cantidad=int(nueva_cant) if nueva_cant else None,
                nuevo_precio=float(nuevo_precio) if nuevo_precio else None
            )
        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")
            eliminar_producto(inventario, nombre)
        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            print(stats)
        elif opcion == "7":  # Guardar CSV
            guardar_csv(inventario, ARCHIVO_CSV)

        elif opcion == "8":  # Cargar CSV
            cargados = cargar_csv(ARCHIVO_CSV)
            if cargados:
                decision = input("Sobrescribir inventario actual? (S/N): ")
                if decision.upper() == "S":
                    inventario = cargados
                else:
                    for c in cargados:
                        for p in inventario:
                            if p["nombre"].lower() == c["nombre"].lower():
                                p["cantidad"] += c["cantidad"]
                                p["precio"] = c["precio"]
                                break
                        else:
                            inventario.append(c)
        elif opcion == "9":
            print("Eso fue todo por hoy, un placer")
            break
        else:
            print("Opción inválida")

Menu()
