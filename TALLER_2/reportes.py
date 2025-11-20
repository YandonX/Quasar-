def reporte_todos():
    global pacientes
    if not pacientes:
        print("No hay pacientes registrados")
        return
    
    print("\n--- TODOS LOS PACIENTES ---")
    for p in pacientes:
        print(f"{p['id']} - {p['nombre']} ({p['edad']} años)")

def reporte_ancianos():
    print("\n--- PACIENTES MAYORES DE 60 AÑOS ---")
    contador = 0
    
    for p in pacientes:
        if p["edad"] > 60:
            print(f"{p['nombre']} - {p['edad']} años")
            contador += 1
    
    print(f"\nTotal: {contador} pacientes")

def reporte_diagnosticos():
    diagnosticos = {}
    
    for p in pacientes:
        diag = p["diagnostico"]
        if diag in diagnosticos:
            diagnosticos[diag] += 1
        else:
            diagnosticos[diag] = 1
    
    print("\n--- DIAGNÓSTICOS FRECUENTES ---")
    for diag, cantidad in diagnosticos.items():
        print(f"{diag}: {cantidad} pacientes")

def reporte_total():
    total = len(pacientes)
    print(f"\nTotal de pacientes registrados: {total}")

def menu_reportes():
    print("\n--- REPORTES ---")
    print("1. Todos los pacientes")
    print("2. Mayores de 60 años")
    print("3. Diagnósticos frecuentes")
    print("4. Cantidad total")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        reporte_todos()
    elif opcion == "2":
        reporte_ancianos()
    elif opcion == "3":
        reporte_diagnosticos()
    elif opcion == "4":
        reporte_total()
    else:
        print("Opción inválida")
