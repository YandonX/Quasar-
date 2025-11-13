paciente = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Pedro", "edad": 40}
]
def delete():
    borrar = input("¿Qué paciente deseas borrar?: ")
    encontrado = False
    
    for p in paciente:
        if p["nombre"].lower() == borrar.lower():
            paciente.remove(p)
            print(f"{p['nombre']} fue eliminado")
            encontrado = True
            break
    
    if not encontrado:
        print("Este paciente no existe")
    
    print(paciente)
delete()
pacientes=[{"id": "001" , "name": "Juan", "genero": "M", "edad": 72, "diagnostico": "tos", "historial": "alergias"},
           {"id": "002" , "name": "Juan", "genero": "M", "edad": 50, "diagnostico": "tos", "historial": "alergias"},
           {"id": "001" , "name": "pedro", "genero": "M", "edad": 72, "diagnostico": "tos", "historial": "alergias"},
           {"id": "001" , "name": "jose", "genero": "M", "edad": 72, "diagnostico": "tos", "historial": "alergias"}]
def buscar_ancianos():    
    ancianos=0
    for paciente in pacientes:
      if paciente["edad"]>60 :
        print(f"estos son los pacientes ancianos {paciente["name"]} y su edad es {paciente["edad"]} su diagnostico es {paciente["diagnostico"]} su historial medico es {paciente["historial"]}")
        ancianos+=1
        print(f"cantidad total pacientes {ancianos}")
        return
buscar_ancianos()
def buscar():
        opcion= int(input("Ingresa el valor por el que deseas buscar: 1- id   2- nombre  3- diagnostico"))
        if opcion == 1:
            id_paciente= input("ingresa el id del paciente: ")   
        for paciente in pacientes:
           if paciente["id"]== id_paciente:
            print(f"datos del paciente {id_paciente} es {paciente}")
            break
        print("ingresa un dato valido")
buscar()