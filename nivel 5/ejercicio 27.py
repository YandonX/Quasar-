# Definición de la Colección (Mini Base de Datos)
base_datos_estudiantes = []
proximo_id = 1  # Para asignar IDs únicos


# --- FUNCIONES DE GESTIÓN ---

def agregar_estudiante(nombre, edad, curso):
    """Agrega un nuevo estudiante a la base de datos."""
    global proximo_id

    nuevo_estudiante = {
        "id": proximo_id,
        "nombre": nombre.strip().title(),
        "edad": int(edad),
        "curso": curso.strip().upper()
    }
    base_datos_estudiantes.append(nuevo_estudiante)
    print(f"✅ Estudiante '{nombre}' agregado con ID: {proximo_id}")
    proximo_id += 1


def mostrar_estudiantes():
    """Imprime todos los estudiantes registrados."""
    if not base_datos_estudiantes:
        print("\n⚠️ La base de datos está vacía.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    print(f"{'ID':<5} {'Nombre':<20} {'Edad':<5} {'Curso':<10}")
    print("-" * 40)

    for estudiante in base_datos_estudiantes:
        print(f"{estudiante['id']:<5} {estudiante['nombre']:<20} {estudiante['edad']:<5} {estudiante['curso']:<10}")
    print("-" * 40)


def modificar_estudiante(id_modificar, nuevo_nombre, nueva_edad, nuevo_curso):
    """Busca un estudiante por ID y actualiza sus datos."""
    try:
        id_modificar = int(id_modificar)
        nueva_edad = int(nueva_edad)
    except ValueError:
        print("⛔ Error: ID y Edad deben ser números.")
        return False

    for estudiante in base_datos_estudiantes:
        if estudiante["id"] == id_modificar:
            # Actualización In-Place del diccionario
            estudiante["nombre"] = nuevo_nombre.strip().title()
            estudiante["edad"] = nueva_edad
            estudiante["curso"] = nuevo_curso.strip().upper()

            print(f"✅ Datos de ID {id_modificar} actualizados a {estudiante['nombre']}.")
            return True

    print(f"❌ Estudiante con ID {id_modificar} no encontrado.")
    return False


def eliminar_estudiante(id_eliminar):
    """Elimina un estudiante de la base de datos por su ID."""
    try:
        id_eliminar = int(id_eliminar)
    except ValueError:
        print("⛔ El ID debe ser un número entero.")
        return False

    for indice, estudiante in enumerate(base_datos_estudiantes):
        if estudiante["id"] == id_eliminar:
            # Elimina el diccionario de la lista usando su índice
            nombre_eliminado = estudiante['nombre']
            del base_datos_estudiantes[indice]
            print(f"🗑️ Estudiante ID {id_eliminar} ('{nombre_eliminado}') eliminado.")
            return True

    print(f"❌ Estudiante con ID {id_eliminar} no encontrado para eliminar.")
    return False


# --- FUNCIÓN PRINCIPAL: Menú Interactivo ---

def menu_principal():
    """Ejecuta el menú principal del sistema de gestión."""
    print("\n--- BIENVENIDO AL SISTEMA DE GESTIÓN DE ESTUDIANTES ---")

    # Bucle While para mantener la interactividad
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Agregar Nuevo Estudiante")
        print("2. Mostrar Todos los Estudiantes")
        print("3. Modificar Estudiante Existente")
        print("4. Eliminar Estudiante por ID")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        print("-" * 20)

        if opcion == '1':
            # AGREGAR ESTUDIANTE
            try:
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                curso = input("Curso: ")
                agregar_estudiante(nombre, edad, curso)
            except ValueError:
                print("⛔ Entrada de Edad inválida. Debe ser un número.")
            except Exception as e:
                print(f"⛔ Ocurrió un error al agregar: {e}")

        elif opcion == '2':
            # MOSTRAR ESTUDIANTES
            mostrar_estudiantes()

        elif opcion == '3':
            # MODIFICAR ESTUDIANTE
            try:
                id_modificar = input("ID del estudiante a modificar: ")
                if not id_modificar.isdigit():
                    raise ValueError("El ID debe ser un número.")

                print("\n** Ingrese los NUEVOS datos: **")
                nuevo_nombre = input("Nuevo Nombre: ")
                nueva_edad = int(input("Nueva Edad: "))
                nuevo_curso = input("Nuevo Curso: ")
                modificar_estudiante(id_modificar, nuevo_nombre, nueva_edad, nuevo_curso)
            except ValueError as e:
                print(f"⛔ Entrada inválida: {e}")
            except Exception as e:
                print(f"⛔ Ocurrió un error al modificar: {e}")

        elif opcion == '4':
            # ELIMINAR ESTUDIANTE
            id_eliminar = input("ID del estudiante a eliminar: ")
            eliminar_estudiante(id_eliminar)

        elif opcion == '5':
            # SALIR
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break  # Sale del bucle while

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecutar el menú principal al inicio del script
if __name__ == "__main__":
    menu_principal()