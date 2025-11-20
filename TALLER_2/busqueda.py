def buscar_por_id():
    id_buscar = input("Ingresa el ID: ")
    
    for p in pacientes:
        if id_buscar in p["id"]:
            mostrar_paciente(p)
            return
    
    print("Paciente no encontrado")

def buscar_por_nombre():
    global pacientes
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
