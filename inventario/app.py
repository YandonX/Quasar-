from inventario import agregar, mostrar, buscar, actualizar, eliminar, estadistica,guardar_datos,cargar_csv
#explicacion mas abajo 
inventario = []

def menu():
    while True:
        print("INVENTARIO")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        elegir()


def elegir():
    global inventario
    try:
      opcion = int(input("Elige una opción: "))
    except ValueError :
      print("coloca un numero")
      return
     
    if opcion == 1:
        agregar(inventario)

    elif opcion == 2:
        mostrar(inventario)

    elif opcion == 3:
        buscar(inventario)

    elif opcion == 4:
        actualizar(inventario)

    elif opcion == 5:
        eliminar(inventario)

    elif opcion == 6:
        estadistica(inventario)

    elif opcion == 7:
         guardar_datos(inventario, "inventario.csv")

    elif opcion == 8:
         inventario = cargar_csv("inventario.csv")
         print("se subio el archivo")

    elif opcion == 9:
        print("Saliendo...")
        exit()

    else:
        print("Opción incorrecta")


menu()
#todo esto es el menu use el from import para llamar al archivo que es inventario para poder traer
#todos las funsiones que hay en el codigo para cuando el usuario eliga la opcion lo mande a digitar 
#eliminar o actualizar los cambios como pueden ver la parte de arriba estan todas las funsiones que 
#hacen que el sistema de funciones guarde y agregue todo la variable global lo que hace es que no solo
#este dentro de la funsion si que pueda estar en todas las funciones y opciones que hay en patalla
#las funciones en parentesis hacen que pueden mostrar el codigo comotambien las demas funciones estan
#siendo llamadas todas tienen inventario para que guarden y hagan todo en la lista inventario 
#todos los datos se guardan en inventario 