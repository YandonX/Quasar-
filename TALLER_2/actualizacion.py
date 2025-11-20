from archivo_Json import guardar_datos
def actualizar_paciente():
    global pacientes
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