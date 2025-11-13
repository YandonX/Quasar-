import random
lista_ids = []

def validar_id():
    while True:
        nuevo_id = random.randint(10000, 99999)
        if nuevo_id not in lista_ids:
            lista_ids.append(nuevo_id)
            return nuevo_id
            
        
def registrar_paciente():
    identifica=avalidar_id()
    if value is not in list:
        list.append(value)
        identifica=value
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    genero = input("Ingrese el género del paciente: ")
    diagnostico = input("Ingrese los síntomas del paciente: ")
    historial = input("Ingrese el historial médico del paciente: ")
    paciente = { 'id': identifica , "nombre": nombre , "edad": edad , "genero": genero, "diagnostico": diagnostico , "historial": historial }
    with open("pacientes.txt", "a") as archivo:
        KeyboardInterrupt
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
                print(f"Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Género: {paciente['genero']}, Síntomas: {paciente['sintomas']}")
    except FileNotFoundError:
        print("No hay pacientes registrados.")
        
def main():
    while True:
        print("\nSistema de Registro de Pacientes")
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
if __name__ == "__main__":
    main() 
