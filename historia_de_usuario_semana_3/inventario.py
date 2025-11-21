import csv
import os
#que hace los import csv y os el primero llama a csv  que es una librebria estandar de py
#esto separa los datos por comas como si fuera un excel ya que en mi opinion es el mejor
#para guardar datos o manejarlos por asi decirlo
#os interactua con el sistema osea que me deja hacer operaciones con los archivos
def guardar_datos_append(producto, ruta):
    archivo_vacio = not os.path.exists(ruta) or os.path.getsize(ruta) == 0
    with open(ruta, "a", newline="") as f:                                
        writer = csv.writer(f)
        if archivo_vacio:
            writer.writerow(["nombre", "precio", "cantidad"])
        writer.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print("producto guardado en el csv (modo append)")
#esta funsion lo que hace es guardar en la linea 8 lo que hace es verificar si el archivo existe o no esta vacio
#si esta vacio primero escribe el encabezado y escribe los datos en nueva linea


def guardar_datos(inventario, ruta):
    with open(ruta, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "precio", "cantidad"])          
        for p in inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])   
    print(f"Inventario guardado en: {ruta}")
#abre en modo w osea escribir es lo que hace es guardar los datos quese ingresan pero esto hace
#que sobreescriba en diferencia de "a" no sobre escribe mientras que "w" lo hace pero esto si o si
#debe estar para guardar los datos que se vayan a escribir


def cargar_csv(ruta):
    productos = []

    with open(ruta, "r") as f:
        reader = csv.reader(f)
        next(reader)  # saltar encabezado
        
        for fila in reader:
            nombre, precio, cantidad = fila
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
#la funsion de cargar y leer los datos que se habian guardado ya que si termino la funsion estos datos se pierden
#como hay una opcion que es la de cargar los datos esto trae de vuelta los datos que se "perdieron"
    return productos


def agregar(inventario):
 while True:
    nombre = input("agrega un producto nuevo: ").lower().strip()
    if any(char.isdigit() for char in nombre): #este if lo que hace es validar de que si sean letras y no numeros
        print("el nombre debe ser con letras")
        continue
#coloque varios while true ya que con poner letras saltaba error tanto en el int como en el float
#coloque 3 while tru y varios try paara que puedan validar de que si sean numeros y no letras
    while True:
        try:
            precio = float(input("ingresa el precio del producto: "))
            break
        except ValueError:
            print("Ingresa un numero por favor")
    while True:
        try:
            cantidad = int(input("cuantas cantidades deseas agregar?: "))
            break
        except ValueError:
            print("Ingresa un numero por favor otra vez")
            continue

  

    print("se van a guardar:")
    print(f"nombre: {nombre}")
    print(f"precio: {precio}")
    print(f"cantidad: {cantidad}")

    confirmar = input("deseas continuar?(S/N): ").upper()

    if confirmar == "S":
        inventario.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        guardar_datos(inventario, "inventario.csv")
        print("se agregaron correctamente")
    else:
        print("no se agrego nada")
    break

#esta funsion lo que hace es agregar los productos cantidad y precio como pueden ver
#se le coloco un if de que si s=confirmar osea que desea hacer los cambios y si le da n=no
#lo devuelve al menu por otra parte esto datos se guardan en una lista y si le dan en la opcion
#guardar datos en csv guarda todos los datos que se escribieron en la lista

def mostrar(inventario):
    if not inventario:
        print("no hay nada")
        return
    print("inventario actual")
    for producto in inventario:
        print(f"nombre: {producto['nombre']}, precio: {producto['precio']}, cantidad: {producto['cantidad']}")
#esto lo que hace es solo mostrar que tiene en el inventario el if not lo que hace es que
#si no tiene nada le lanza de que no tiene nada en el carrito

def buscar(inventario):
    if not inventario:
        print("no hay nada")
        return

    nombre_buscar = input("que producto deseas buscar: ").lower().strip()

    encontrado = False
    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            print(f"aqui esta el producto: {producto['nombre']}, {producto['precio']}, {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("no se encontro el producto")
#esto lo que hace es buscar un prodcuto en especifico mpor asi decirlo un filtro de bsuqueda
#escribes el producto que deseas buscar de tantos productos ya que no hay limite para guardar

def actualizar(inventario):
    if not inventario:
        print("no hay nada")
        return
    actualizar_datos = input("Escribe el producto que quieres actualizar: ").lower().strip()
    encontrado = False
    for producto in inventario:
        if producto["nombre"].lower() == actualizar_datos:
            print("se encontro el producto")
            nuevo_precio = input("ingresa un nuevo precio (enter para omitir):")
            nueva_cantidad = input("ingresa una nueva cantidad (enter para omitir): ")
            if nuevo_precio:
                producto["precio"] = float(nuevo_precio)
            if nueva_cantidad:
                producto["cantidad"] = int(nueva_cantidad)
            guardar_datos(inventario, "inventario.csv")
            encontrado = True
            break
    
    if not encontrado:
        print("no se encontro el producto")
#esta fusion actualiza los datos de los productos actualiza nombre precio y cantidad
#ya dando enter es por asi decirlo no cambiar todo de por si el false y true son para validar
#si estan en el inventario los productos

def eliminar(inventario):
    if not inventario:
        print("no hay nada para eliminar")
        return
    
    nombre_a_eliminar = input("Ingresa el nombre del producto a eliminar: ").lower().strip()

    encontrado = False
    for producto in inventario:
        if producto["nombre"] == nombre_a_eliminar:
            print(f"el producto {nombre_a_eliminar} fue eliminado")
            inventario.remove(producto)
            guardar_datos(inventario, "inventario.csv")
            encontrado = True
            break
    
    if not encontrado:
        print("el producto no existe")
#esto elimina los productos  esto es como actualizar excepto que lo elimina del todo poniendo el nombre
#mismas condiciones pero en vez de append se le coloca remove para que el for osea producto manda a 
#buscar el producto que quieren sacar

def estadistica(inventario):
    if not inventario:
        print("no se encontro nada en el inventario")
        return

    total_inventario = 0
    unidades_totales = 0

    producto_mas_caro = inventario[0]
    producto_por_stock = inventario[0]

    print("Estadística:\n")

    for producto in inventario:
        
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = producto["cantidad"]

        sub_total = precio * cantidad

        total_inventario += sub_total
        unidades_totales += cantidad

        if precio > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if cantidad > producto_por_stock["cantidad"]:
            producto_por_stock = producto

    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {total_inventario}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con mayor stock: {producto_por_stock['nombre']} ({producto_por_stock['cantidad']})")
    #esta funsion fue la mas dificil de entender tuve que usar ia para que me guiara de como debo hacerlo
    #no hize copia pega solo re escribi y envistigaba todas las funciones
    #total_inventario = 0
    #unidades_totales = 0
    #producto_mas_caro = inventario[0]
    #producto_por_stock = inventario[0]
    #estas variables estan en 0 por el valor total osea tanto en unidades como precio total 
    #los if son para demostrar de cuando se digite el precio de un producto o el stock lanze el
    #mensaje de cual es el mas caro y cual esta en mas stock
