from archivos_csv import CRUD
from archivo_json import guardar_json

crud= CRUD()
archivo = "datos.csv"
crud.crear_csv(archivo)

while True:
    print("\n ==== MENÚ ====")
    print("1. Crear persona")
    print("2. Listar personas")
    print("3. Modificar registros")
    print("4. Eliminar personas")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        nombre= input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")

        id_creado = crud.agregar_linea(archivo,nombre,edad)
        print(f"Esta persona fue creada con el ID {id_creado}")

    elif opcion == '2':
        datos= crud.listar(archivo)
        print("\n === LISTADO === ")
        for fila in datos:
            print(f"ID:\t {fila[0]} \t| Nombre: \t{fila[1]}\t| Edad: {fila[2]}")

    elif opcion == '3':
        print("aquí es donde modificamos")
    
    elif opcion == '4':
        print("aquí eliminamos")

    elif opcion == '5':
        break

    else:
        print("ERROR \nOpción elegida no es válida")