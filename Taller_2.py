pacientes=[{"name": "Juan", "genero": "M", "edad": 72, "diagnostico": "tos", "historial": "alergias"},
           {"name": "Juan", "genero": "M", "edad": 50, "diagnostico": "tos", "historial": "alergias"}]
ancianos=0
for paciente in pacientes:
    if paciente["edad"]>60 :
        print(f"estos son los pacientes ancianos{paciente}")
        ancianos+=1
        print(f"cantidad total pacientes {ancianos}")