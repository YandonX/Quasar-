
calificaciones=[]
'''n=int(input("cuantas notas tienes"))
for i in range(n):
    ingresar= int(input("ingresa las notas: "))
    calificaciones.append(ingresar)
promedio = sum(calificaciones)/len(calificaciones)

print(f"el promedio:{promedio}")
print("nota",calificaciones)

if promedio >= 60:
    print("aprobado")
else:
    print("Reprobado ")'''
# 26 Carrito de compras
'''carrito=[]
while True:
    print("bienvenido a D2")
    print("1. agregar producto")
    print("2. elimina un producto")
    print("3. que productos llevas")
    print("4. salir")
    try:
     opcion = int(input("elige una opcion:" ))
    except ValueError:
       print("agrega un numero por favor")
       continue
    
    if opcion == 1:
        item=input("que deseas agregar?: ")
        carrito.append(item)
        print(f"se agrego: {item}")    

    elif opcion == 2:
        eliminar= input("escribe el producto que deseas eliminar: ")
        if eliminar in carrito:
          carrito.remove(eliminar)
        print(f"se elimino{eliminar}")
        
    elif opcion == 3:
        for item in carrito:
            print("llevas en el carrito: ")
            print(f"-{item}") 

    elif opcion == 4:
        print("saliendo del programa")
        break
    else:
        print("coloca un numero no letras para entrar en las opciones: ")'''
# 27 cajero automatico

'''saldo=2000000
depositos=[]
retiros=[]
while True:
    print("bienvenido a nequi")
    print("1. retirar")
    print("2. cuanto has retiradp")
    print("3. hacer un deposito")
    print("4. cuanto has mandado?")
    print("5. salir")
    try:
     opcion = int(input("elige una opcion:" ))
    except ValueError:
       print("agrega un numero por favor")
       continue
    
    if opcion == 1:
        retiro=float(input("cuanto deseas retirar: "))
        saldo-=retiro
        retiros.append(retiro)
        print(f"se retiro: {saldo}")  

    elif opcion == 2:
        for retiro in retiros:
            print("has retirado:")
            print(f"-{retiro}")    

    elif opcion == 3:
        concinar= float (input("cuanto deseas concinar?: "))
        saldo+=concinar
        depositos.append(concinar)
        print(f"se concino: {concinar}")
        
    elif opcion == 4:
        print("has mandado: ")
        for concinar in depositos:            
         print(f"-{concinar}") 

    elif opcion == 5:
        print("saliendo del programa")
        break
    else:
        print("coloca un numero no letras para entrar en las opciones: ")'''

#28  gestion de estudiantes




    

