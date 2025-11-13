# Lista de pacientes (cada uno es un diccionario con sus datos)
pacientes = [
    {"id": 12345678, "nombre": "juanjo villa", "edad": 29, "diagnostico": "asma", "historial": "ataque recurrentes" },
    {"id": 13456789, "nombre": "genevieve castilla", "edad": 21, "diagnostico": "fiebre", "historial": "temperatura cerca de lo 40grados"},
    {"id": 19876543, "nombre": "liliana roset", "edad": 35, "diagnostico": "lupus", "historial": "si era lupus"}
    ]

#while para iterar
while True:
    print("\n== SISTEMA PACIENTES ==")
    for paciente in pacientes:
        print(f"ID: {paciente['id']}, {paciente['nombre']}, (edad: {paciente['edad']}, diagnotico: {paciente['diagnostico']}, historial: {paciente['historial']})")

    opcion = input("\nescoje el ID del pasiente que desee modificar (escribir 'salir'):")
    
    if opcion.lower() == "salir":
        input("programa terminado")
        break
    
    if opcion.isdigit():
        id_encontar =int(opcion)
    else:
        print("opcion no valida, intente denuevo")
        continue
    
    paciente_hayado = None
    for paciente in pacientes:
        if paciente['id'] == id_encontar:
            paciente_hayado = paciente
            break
        
    if paciente_hayado is None:
        print("ID no hayado, intente denuevo")
        continue

    paciente = paciente_hayado
    
    #ficha paciente
    print(f"\n--FICHA DE {paciente['nombre'].upper()}--")
    print(f"edad: {paciente['edad']}")
    print(f"diagnotico: {paciente['diagnostico']}")
    print("historial:")
    for i, evento in enumerate(int(paciente_hayado["historial"], start=1)):
        print(f"  {i}. {evento}")
    
    #menu modificacion
    print("\nque desea modificar?")
    print("1. edad")
    print("2. diagnotico")
    print("3. historial")
    print("4. terminar")
    
    accion = input("opcion (1-4): ")
    
    if accion == "1":
        nueva_edad = input("ingrese la nueva edad: ")
        if nueva_edad.isdigit():
            paciente["edad"] = int(nueva_edad)
            print("edad actualizada correctamente")
        else:
            print("debe ingresar un numero valido")
    elif accion == "2":
        nuevo_dig = input("escribe el nuevo diagnotico: ")
        paciente["diagnotico"] = nuevo_dig
        print("diagnotico actualizado correctamente")
    elif accion == "3":
        nuevo_his = input("nuevo historial")
        paciente['historial'] = nuevo_his
        print("hitorial actualizado")
    elif accion == "4":
        print("volviendo al menu principal")
    else:
        print("opcion no valida")