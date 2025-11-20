from archivo_Json import guardar_datos

def registrar_paciente():
    print("\n--- Registro de pacientes ---")
    agregar_paciente()


def pedir_id():
    global pacientes
    while True:
        id_pac = input("Ingrese la cédula del paciente: ")
        if not id_pac.isdigit():
            print("Por favor ingrese un ID válido (solo números).")
            continue
    
        for p in pacientes:
            if p["id"] == id_pac:
                print("Este ID ya está registrado en la base.")
                break
            else:
                return id_pac

def pedir_nombre():
    while True:
        nombre = input("Nombre: ")
        if (nombre.replace(' ','').isalpha()):
            return nombre
        print("Por favor ingrese un nombre válido (sin números).")

def edad_valida():
    while True:
        try:
            edad = int(input("Edad: "))
            if (edad > 0) and (edad < 120):
                return edad
            else:
                print("Por favor ingrese una edad válida (entre 1 y 119).")
        except ValueError:
            print("Por favor ingrese una edad válida (número entero).")

def genero_valido():   
    genero= input("ingresa el Género (M) si es Masculino, (F) si es Femenino: ")
    while genero.upper() not in ["M", "F"]:
        genero = input("Recuerda, Solamente la primera letra (M) Masculino, (F) Femenino").upper()
    return genero

def diagnostico():
    diagnostico = input("Diagnóstico: ")
    return diagnostico

def historial()
    historial = input("Historial médico: ")
    return historial

def agregar_paciente():
    
    paciente = {
        "id": pedir_id(),
        "nombre": pedir_nombre(),
        "edad": edad_valida(),
        "genero": genero_valido(),
        "diagnostico": diagnostico(),
        "historial": [historial()]
    }
    
    pacientes.append(paciente)
    guardar_datos()
    print("Paciente registrado exitosamente")
