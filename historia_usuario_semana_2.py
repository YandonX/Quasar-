productos_dispo = {
    "banano": 2000,
    "lulo": 4000,
    "leche": 8000,
    "carne": 18000,
    "chunchcurria": 19000
}

carrito = []

def cantidad_x_producto():
    """Muestra la cantidad de cada producto en el carrito"""
    if not carrito:
        print("no hay productos en el carrito.")
        return
    
    print("\n----- PRODUCTOS EN EL CARRITO -----")
    for item, cantidad in carrito:
        print(f"{item}: {cantidad} unidades")
    print()

def cantidad_x_precio():
    """Calcula y muestra el precio total del carrito"""
    if not carrito:
        print("no hay productos en el carrito.")
        return
    
    total = 0
    print("\n----- CANTIDAD x PRECIO -----")
    
    for item, cantidad in carrito:
        precio_unitario = productos_dispo[item]
        subtotal = precio_unitario * cantidad
        total += subtotal
        print(f"{item}: {cantidad} x ${precio_unitario} = ${subtotal}")
    
    print(f"TOTAL A PAGAR: ${total}\n")

def agregar_productos():
    while True:
        print("bienvenido a D2")
        print("1. agregar producto")
        print("2. elimina un producto")
        print("3. que vendemos?")
        print("4. lo que llevas:")
        print("5. calcular cantidad x precio")
        print("6. salir")
        
        try:
            opcion = int(input("elige una opcion: "))
        except ValueError:
            print("agrega un numero por favor")
            continue
        
        if opcion == 1:
            item = input("que deseas agregar?: ").lower()
            if item in productos_dispo:
                cantidad = int(input("cuantos productos deseas llevar: "))
                carrito.append((item, cantidad))
                print(f"se agrego {cantidad} de {item}")
            else:
                print("el producto no existe")
        
        elif opcion == 2:
            eliminar = input("escribe el producto que deseas eliminar: ").lower()
            encontrado = False
            for producto in carrito:
                if producto[0] == eliminar:
                    carrito.remove(producto)
                    encontrado = True
                    print(f"se elimino a {eliminar} del carrito")
                    break
            if not encontrado:
                print("producto no encontrado")

        elif opcion == 3:
            print(f"que productos vendemos? {productos_dispo}")
            
        elif opcion == 4:
            cantidad_x_producto()
        
        elif opcion == 5:
            cantidad_x_precio()
        
        elif opcion == 6:
            print("saliendo del programa")
            break
        
        else:
            print("opcion no valida, intenta de nuevo")

agregar_productos()
# el objetivo de la semana era parender a usar diccionarios, funciones y listas este es un sistema 
# de mercado que calcula precio * cantidad use un diccionario con productos ya establecidos y precios
#una lista para guardar la cantidad de producto que se esta llevando y la opcion 5 que te muestra 
#cuanto tienes que pagar y la opcion 3 que te muestra una lista de lo que llevas 
#si no le gustan los precios demalas tiene mas tiendas por revisar