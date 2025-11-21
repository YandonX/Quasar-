import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda el inventario en un archivo CSV.
    
    Parámetros:
        inventario (list): Lista de diccionarios con productos.
        ruta (str): Ruta del archivo CSV.
        incluir_header (bool): Si True, escribe encabezado.
    """
    if not inventario:
        print("Inventario vacío. No se puede guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for prod in inventario:
                writer.writerow([prod["nombre"], prod["precio"], prod["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print("Error: No se puede escribir en el archivo (permiso denegado).")
    except Exception as e:
        print(f"Error inesperado: {e}")

def cargar_csv(ruta):
    """Carga un CSV y retorna lista de productos válidos.
    
    Parámetros:
        ruta (str): Ruta del archivo CSV.
    Retorna:
        lista de diccionarios con productos.
    """
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # Validar encabezado
            if reader.fieldnames != ["nombre", "precio", "cantidad"]:
                print("Error: Encabezado inválido")
                return []

            for fila in reader:
                try:
                    nombre = fila["nombre"].strip()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except (ValueError, KeyError):
                    errores += 1
        if errores:
            print(f"{errores} filas inválidas omitidas")
        return inventario
    except FileNotFoundError:
        print("Archivo no encontrado")
        return []
    except UnicodeDecodeError:
        print("Error al leer el archivo (codificación inválida)")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []
