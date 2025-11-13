lista_ids = []

def validar_id():
    while True:
        nuevo_id = int(input("Ingrese número de cedula: "))
        if nuevo_id not in lista_ids:
            lista_ids.append(nuevo_id)
            return nuevo_id
            
        
def registrar_paciente():
    identifica=validar_id()
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    genero = ""
    while genero.upper() != "F" and genero.upper() != "M":
        genero = input("Ingrese el género del paciente (F) si es femenino y (M) si es masculino: ")
    diagnostico = input("Ingrese los diagnostico del paciente: ")
    historial = input("Ingrese el historial médico del paciente: ")
    paciente = { 'id': identifica , "nombre": nombre , "edad": edad , "genero": genero, "diagnostico": diagnostico , "historial": historial }
    with open("pacientes.txt", "a") as archivo:
        archivo.write(f"{paciente}\n")
    
    print("Paciente registrado exitosamente.")
    
def mostrar_pacientes():
    try:
        with open("pacientes.txt", "r") as archivo:
            pacientes = archivo.readlines()
            if not pacientes:
                print("No hay pacientes registrados.")
                return
            for linea in pacientes:
                paciente = eval(linea.strip())
                print(f"Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Género: {paciente['genero']}, Diagnostico: {paciente['diagnostico']}")
    except FileNotFoundError:
        print("No hay pacientes registrados.")
        
def main():
    while True:
        print("\nSistema de Registro del paciente")
        print("1. Registrar nuevo paciente")
        print("2. Mostrar pacientes registrados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()