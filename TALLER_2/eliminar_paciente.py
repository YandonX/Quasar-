from archivo_Json import guardar_datos

def eliminar_paciente():
    global pacientes
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