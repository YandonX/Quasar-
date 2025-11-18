import json

# Lista global de pacientes
pacientes = []

# =============== FUNCIONES DE ARCHIVO IR A JSON =================

def cargar_datos():
    global pacientes
    try:
        with open("pacientes.json", "r") as archivo:
            pacientes = json.load(archivo)
        print("Datos cargados correctamente")
    except FileNotFoundError:
        pacientes = []
        print("No hay datos previos")

def guardar_datos():
    with open("pacientes.json", "w") as archivo:
        json.dump(pacientes, archivo, indent=4)
    print("Datos guardados correctamente")

# ==================== FUNCIONES DE REGISTRO ====================

def registrar_paciente():
    print("\n--- Registro de pacientes ---")
    
    while True:
        id_pac = input("Ingrese la cédula del paciente: ")
        if id_pac.isdigit():
            break
        else:
            print("Por favor ingrese un ID válido (solo números).")
    
    for p in pacientes:
        if p["id"] == id_pac:
            print("Este ID ya está registrado en la base.")
            return
    
    while True:
        nombre = input("Nombre: ")
        if (nombre.strip()).isalpha() or " " in nombre:
            break
        else:
            print("Por favor ingrese un nombre válido (sin números).")
    while True:
        try:
            edad = int(input("Edad: "))
            if edad > 0 or edad < 120:
                break
            else:
                print("Por favor ingrese una edad válida (entre 1 y 119).")
        except ValueError:
            print("Por favor ingrese una edad válida (número entero).")
            
    genero= input("ingresa el Género (M) si es Masculino, (F) si es Femenino: ")
    while genero.upper() not in ["M", "F"]:
        genero = input("Recuerda, Solamente la primera letra (M) Masculino, (F) Femenino").upper()
        
    diagnostico = input("Diagnóstico: ")
    historial = input("Historial médico: ")
    
    paciente = {
        "id": id_pac,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "diagnostico": diagnostico,
        "historial": [historial]
    }
    
    pacientes.append(paciente)
    guardar_datos()
    print("Paciente registrado exitosamente")

# ==================== FUNCIONES DE BÚSQUEDA ====================

def buscar_por_id():
    id_buscar = input("Ingresa el ID: ")
    
    for p in pacientes:
        if id_buscar in p["id"]:
            mostrar_paciente(p)
            return
    
    print("Paciente no encontrado")

def buscar_por_nombre():
    nombre = input("Ingresa el nombre: ").lower()
    encontrados = []
    
    for p in pacientes:
        if nombre in p["nombre"].lower():
            encontrados.append(p)
    
    if encontrados:
        for p in encontrados:
            mostrar_paciente(p)
    else:
        print("No se encontraron pacientes")

def buscar_por_diagnostico():
    diag = input("Ingresa el diagnóstico: ").lower()
    encontrados = []
    
    for p in pacientes:
        if diag in p["diagnostico"].lower():
            encontrados.append(p)
    
    if encontrados:
        for p in encontrados:
            mostrar_paciente(p)
    else:
        print("No se encontraron pacientes")

def mostrar_paciente(p):
    print(f"\n{p['id']} es la identificación de {p['nombre']}, quien tiene {p['edad']}años")
    if p['genero'].lower() == 'f':
        print(f"Es una mujer (genero femenino)")
    else:
         print(f"Es un hombre (genero masculino)")
    print(f"su Diagnóstico es: {p['diagnostico']}")
    print(f"y tiene el siguiente historial: {p['historial']}")

def menu_buscar():
    print("\n--- BUSCAR PACIENTE ---")
    print("1. Por ID (ingrese el número '1')")
    print("2. Por Nombre, (ingrese el número '2')")
    print("3. Por Diagnóstico, (ingrese el número '3')")
    
    opcion = input("Opción 1, 2 o 3: ")
    
    if opcion == "1":
        buscar_por_id()
    elif opcion == "2":
        buscar_por_nombre()

    elif opcion == "3":
        buscar_por_diagnostico()
    else:
        print("Opción inválida")

# ==================== FUNCIONES DE ACTUALIZACIÓN ====================

def actualizar_paciente():
    id_buscar = input("ID del paciente a actualizar: ")
    
    for p in pacientes:
        if p["id"] == id_buscar:
            print("\n¿Qué deseas actualizar?")
            print("1. Edad")
            print("2. Diagnóstico")
            print("3. Añadir evento al historial")
            
            opcion = input("Opción: ")
            
            if opcion == "1":
                nueva_edad = int(input("Nueva edad: "))
                p["edad"] = nueva_edad
            elif opcion == "2":
                nuevo_diag = input("Nuevo diagnóstico: ")
                p["diagnostico"] = nuevo_diag
            elif opcion == "3":
                evento = input("Nuevo evento: ")
                p["historial"].append(evento)
            else:
                print("Opción inválida")
                return
            
            guardar_datos()
            print("Paciente actualizado")
            return
    
    print("Paciente no encontrado")

# ==================== FUNCIONES DE ELIMINACIÓN ====================

def eliminar_paciente():
    id_buscar = input("ID del paciente a eliminar: ")
    
    for p in pacientes:
        if p["id"] == id_buscar:
            print(f"\n¿Seguro que deseas eliminar a {p['nombre']}?")
            confirmar = input("Escribe 'SI' para confirmar: ").upper()
            
            if confirmar == "SI":
                pacientes.remove(p)
                guardar_datos()
                print("Paciente eliminado")
            else:
                print("Eliminación cancelada")
            return
    
    print("Paciente no encontrado")

# ==================== FUNCIONES DE REPORTES ====================

def reporte_todos():
    if not pacientes:
        print("No hay pacientes registrados")
        return
    
    print("\n--- TODOS LOS PACIENTES ---")
    for p in pacientes:
        print(f"{p['id']} - {p['nombre']} ({p['edad']} años)")

def reporte_ancianos():
    print("\n--- PACIENTES MAYORES DE 60 AÑOS ---")
    contador = 0
    
    for p in pacientes:
        if p["edad"] > 60:
            print(f"{p['nombre']} - {p['edad']} años")
            contador += 1
    
    print(f"\nTotal: {contador} pacientes")

def reporte_diagnosticos():
    diagnosticos = {}
    
    for p in pacientes:
        diag = p["diagnostico"]
        if diag in diagnosticos:
            diagnosticos[diag] += 1
        else:
            diagnosticos[diag] = 1
    
    print("\n--- DIAGNÓSTICOS FRECUENTES ---")
    for diag, cantidad in diagnosticos.items():
        print(f"{diag}: {cantidad} pacientes")

def reporte_total():
    total = len(pacientes)
    print(f"\nTotal de pacientes registrados: {total}")

def menu_reportes():
    print("\n--- REPORTES ---")
    print("1. Todos los pacientes")
    print("2. Mayores de 60 años")
    print("3. Diagnósticos frecuentes")
    print("4. Cantidad total")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        reporte_todos()
    elif opcion == "2":
        reporte_ancianos()
    elif opcion == "3":
        reporte_diagnosticos()
    elif opcion == "4":
        reporte_total()
    else:
        print("Opción inválida")

# ==================== MENÚ PRINCIPAL ====================

def menu_principal():
    cargar_datos()
    
    while True:
        print("\n" + "="*38)
        print("   SISTEMA DE GESTIÓN DE PACIENTES")
        print("="*38)
        print("1. Registrar paciente")
        print("2. Buscar paciente")
        print("3. Actualizar paciente")
        print("4. Eliminar paciente")
        print("5. Reportes")
        print("6. Salir")
        print("="*38)
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            menu_buscar()
        elif opcion == "3":
            actualizar_paciente()
        elif opcion == "4":
            eliminar_paciente()
        elif opcion == "5":
            menu_reportes()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

# Iniciar el programa
menu_principal()