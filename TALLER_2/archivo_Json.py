import json
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