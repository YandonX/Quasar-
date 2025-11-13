import json

lista_ids = []

def cargar_pacientes():
    try:
        with open("pacientes.txt", "r") as archivo:
            lineas = archivo.readlines()
            pacientes = []
            for linea in lineas:
                paciente = eval(linea.strip())
                pacientes.append(paciente)
                lista_ids.append(paciente['id'])
            return pacientes
    except FileNotFoundError:
        return []

def guardar_pacientes(pacientes):
    with open("pacientes.txt", "w") as archivo:
        for paciente in pacientes:
            archivo.write(f"{paciente}\n")

def validar_id():
    while True:
        nuevo_id = int(input("Ingrese número de cédula: "))
        if nuevo_id not in lista_ids:
            lista_ids.append(nuevo_id)
            return nuevo_id
        else:
            print("Este ID ya existe. Ingrese otro.")

def registrar_paciente(pacientes):
    identifica = validar_id()
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    genero = ""
    while genero.upper() != "F" and genero.upper() != "M":
        genero = input("Ingrese el género del paciente (F) si es femenino y (M) si es masculino: ")
    diagnostico = input("Ingrese el diagnóstico del paciente: ")
    historial = input("Ingrese el historial médico del paciente: ")
    
    paciente = {
        'id': identifica,
        'nombre': nombre,
        'edad': edad,
        'genero': genero,
        'diagnostico': diagnostico,
        'historial': historial
    }
    
    pacientes.append(paciente)
    guardar_pacientes(pacientes)
    print("Paciente registrado exitosamente.")

def mostrar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    print("\n== LISTA DE PACIENTES ==")
    for paciente in pacientes:
        print(f"ID: {paciente['id']}, {paciente['nombre']}, (Edad: {paciente['edad']}, Diagnóstico: {paciente['diagnostico']}, Historial: {paciente['historial']})")

def modificar_paciente(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    mostrar_pacientes(pacientes)
    
    opcion = input("\nEscoja el ID del paciente que desea modificar (o escriba 'salir'): ")
    
    if opcion.lower() == "salir":
        return
    
    if not opcion.isdigit():
        print("Opción no válida, intente de nuevo")
        return
    
    id_encontrar = int(opcion)
    paciente_hallado = None
    
    for paciente in pacientes:
        if paciente['id'] == id_encontrar:
            paciente_hallado = paciente
            break
    
    if paciente_hallado is None:
        print("ID no hallado, intente de nuevo")
        return
    
    print(f"\n-- FICHA DE {paciente_hallado['nombre'].upper()} --")
    print(f"Edad: {paciente_hallado['edad']}")
    print(f"Diagnóstico: {paciente_hallado['diagnostico']}")
    print(f"Historial: {paciente_hallado['historial']}")
    
    print("\n¿Qué desea modificar?")
    print("1. Edad")
    print("2. Diagnóstico")
    print("3. Historial")
    print("4. Nombre")
    print("5. Género")
    print("6. Terminar")
    
    accion = input("Opción (1-6): ")
    
    if accion == "1":
        nueva_edad = input("Ingrese la nueva edad: ")
        if nueva_edad.isdigit():
            paciente_hallado["edad"] = nueva_edad
            print("Edad actualizada correctamente")
        else:
            print("Debe ingresar un número válido")
    
    elif accion == "2":
        nuevo_diag = input("Escriba el nuevo diagnóstico: ")
        paciente_hallado["diagnostico"] = nuevo_diag
        print("Diagnóstico actualizado correctamente")
    
    elif accion == "3":
        nuevo_hist = input("Ingrese el nuevo historial: ")
        paciente_hallado['historial'] = nuevo_hist
        print("Historial actualizado")
    
    elif accion == "4":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        paciente_hallado['nombre'] = nuevo_nombre
        print("Nombre actualizado correctamente")
    
    elif accion == "5":
        nuevo_genero = ""
        while nuevo_genero.upper() != "F" and nuevo_genero.upper() != "M":
            nuevo_genero = input("Ingrese el nuevo género (F/M): ")
        paciente_hallado['genero'] = nuevo_genero
        print("Género actualizado correctamente")
    
    elif accion == "6":
        print("Volviendo al menú principal")
        return
    
    else:
        print("Opción no válida")
        return
    
    guardar_pacientes(pacientes)

def main():
    pacientes = cargar_pacientes()
    
    while True:
        print("\n========================================")
        print("   SISTEMA DE REGISTRO DE PACIENTES")
        print("========================================")
        print("1. Registrar nuevo paciente")
        print("2. Mostrar pacientes registrados")
        print("3. Modificar paciente")
        print("4. Salir")
        print("========================================")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            registrar_paciente(pacientes)
        
        elif opcion == "2":
            mostrar_pacientes(pacientes)
        
        elif opcion == "3":
            modificar_paciente(pacientes)
        
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()