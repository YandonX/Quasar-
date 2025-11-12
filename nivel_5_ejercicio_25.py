# -------------------------------------------
# Nivel 5 — Retos (Integración de todo)
# -------------------------------------------

# 25 Sistema de calificaciones
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
    # Menú principal del carrito
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
    
    # Agregar producto al carrito
    if opcion == 1:
        item=input("que deseas agregar?: ")
        carrito.append(item)
        print(f"se agrego: {item}")    

    # Eliminar producto del carrito
    elif opcion == 2:
        eliminar= input("escribe el producto que deseas eliminar: ")
        if eliminar in carrito:
            carrito.remove(eliminar)
        print(f"se elimino {eliminar}")
        
    # Mostrar productos actuales
    elif opcion == 3:
        for item in carrito:
            print("llevas en el carrito: ")
            print(f"-{item}") 

    # Salir del programa
    elif opcion == 4:
        print("saliendo del programa")
        break
    else:
        print("coloca un numero no letras para entrar en las opciones: ")'''


# 27 Cajero automático
'''saldo=2000000      # saldo inicial
depositos=[]          # lista de depósitos realizados
retiros=[]            # lista de retiros realizados

while True:
    print("bienvenido a nequi")
    print("1. retirar")
    print("2. cuanto has retirado")
    print("3. hacer un deposito")
    print("4. cuanto has mandado?")
    print("5. salir")

    try:
        opcion = int(input("elige una opcion:" ))
    except ValueError:
        print("agrega un numero por favor")
        continue
    
    # Opción para retirar dinero
    if opcion == 1:
        retiro=float(input("cuanto deseas retirar: "))
        saldo-=retiro
        retiros.append(retiro)
        print(f"saldo actual: {saldo}")  

    # Mostrar lista de retiros
    elif opcion == 2:
        for retiro in retiros:
            print("has retirado:")
            print(f"-{retiro}")    

    # Depositar dinero en la cuenta
    elif opcion == 3:
        transferrir= float (input("cuanto deseas consignar?: "))
        saldo+=tranferir
        depositos.append(transferrir)
        print(f"se consignó: {transferrir}")
        
    # Mostrar lista de depósitos
    elif opcion == 4:
        print("has mandado: ")
        for transferrir in depositos:            
            print(f"-{transferir}") 

    # Salir
    elif opcion == 5:
        print("saliendo del programa")
        break
    else:
        print("coloca un numero no letras para entrar en las opciones: ")'''


# 28 Gestión de estudiantes

# Lista vacía donde se guardarán los estudiantes
'''estudiantes = []

while True:
    print("bienvenido a master 2000")
    print("1. agregar estudiante")
    print("2. ver todos los estudiantes")
    print("3. buscar estudiante")
    print("4. eliminar estudiante")
    print("5. salir")

    try:
        opcion = int(input("elige una opcion: "))
    except ValueError:
        print("agrega un numero por favor")
        continue
    
    # Agregar estudiante nuevo
    if opcion == 1:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        nota = float(input("Nota: "))
        estudiantes.append({"nombre": nombre, "edad": edad, "nota": nota})
        print(f"Se agregó a: {nombre}")  

    # Mostrar lista de estudiantes
    elif opcion == 2:
        print("Nuevos estudiantes:")
        for student in estudiantes:
            print(f"- Nombre: {student['nombre']}, Edad: {student['edad']}, Nota: {student['nota']}")
              
    # Buscar estudiante por nombre
    elif opcion == 3:
        nombre_buscar = input("Ingresa el nombre del estudiante que buscas: ")
        encontrado = False  

        for student in estudiantes:
            if student["nombre"].lower() == nombre_buscar.lower():
                print(" Estudiante encontrado:")
                print(f"Nombre: {student['nombre']}, Edad: {student['edad']}, Nota: {student['nota']}")
                encontrado = True
                break 

        if not encontrado:
            print("No se encontró al estudiante.")

    # Eliminar estudiante por nombre
    elif opcion == 4:
        borrar = input("escribe el nombre del estudiante que deseas eliminar: ")
        encontrado=False

        for student in estudiantes:  
            if student["nombre"].lower() == borrar.lower():
                estudiantes.remove(student)
                print(f"se eliminó a {borrar}")
                encontrado= True
                break
        if not encontrado:
            print("no se encontró")

    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("coloca un numero no letra")'''


# 29 Calculadora avanzada (usando funciones)
'''def sumar(a, b):
   return a+b

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return "no se puede dividir entre 0"
   
while True:
    print("calculadora")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")

    try:
        opcion = int(input("elige una opcion:" ))
    except ValueError:
        print("agrega un numero por favor")
        continue
    
    # según la opción se ejecuta la función correspondiente
    if opcion == 1:
        num1=float(input("coloca el primer numero: "))
        num2=float(input("coloca el segundo numero: "))
        resultado=sumar(num1,num2)
        print(f"el resultado es  {resultado}")

    elif opcion == 2:
        num1=float(input("coloca el primer numero: "))
        num2=float(input("coloca el segundo numero: "))
        resultado=restar(num1,num2)
        print(f"el resultado es  {resultado}")
       
    elif opcion == 3:
        num1=float(input("coloca el primer numero: "))
        num2=float(input("coloca el segundo numero: "))
        resultado=multiplicar(num1,num2)
        print(f"el resultado es  {resultado}")

    elif opcion == 4:
        num1=float(input("coloca el primer numero: "))
        num2=float(input("coloca el segundo numero: "))
        resultado=dividir(num1,num2)
        print(f"el resultado es  {resultado}")

    elif opcion == 5:
       print("saliendo de la calculadora")
       break
    else:
        print("coloca un numero no letras para entrar en las opciones")'''


# 30 Agenda de contactos
# Lista que guarda los contactos
'''conctatos = []

while True:
    print("bienvenido wpchino")
    print("1. agregar contacto")
    print("2. ver tus nuevos conctatos")
    print("3. buscar conctato")
    print("4. eliminar contacto")
    print("5. salir")

    try:
        opcion = int(input("elige una opcion: "))
    except ValueError:
        print("agrega un numero por favor")
        continue
    
    # Opción 1: Agregar contacto nuevo
    if opcion == 1:
        print("agrega un contacto")
        nombre = input("Nombre: ")
        numero = int(input("numero: "))
        email = (input("email: "))
        conctatos.append({"nombre": nombre, "numero de celuco": numero, "email": email})
        print(f"Se agregó a: {nombre}")  

    # Opción 2: Ver contactos guardados
    elif opcion == 2:
        print("Nuevos contactos:")
        for contac in conctatos:
            print(f"- Nombre: {contac['nombre']}, celuco: {contac['numero de celuco']}, email: {contac['email']}")
              
    # Opción 3: Buscar contacto
    elif opcion == 3:
        nombre_buscar = input("Ingresa el nombre del contacto: ")
        encontrado = False  

        for contac in conctatos:
            if contac["nombre"].lower() == nombre_buscar.lower():
                print("contacto encontrado:")
                print(f"- Nombre: {contac['nombre']}, celuco: {contac['numero de celuco']}, email: {contac['email']}")
                encontrado = True
                break 

        if not encontrado:
            print("No se encontró al contacto.")

    # Opción 4: Eliminar contacto
    elif opcion == 4:
        borrar = input("escribe el nombre del contacto que deseas eliminar: ")
        encontrado = False

        for contac in conctatos:  
            if contac["nombre"].lower() == borrar.lower():
                conctatos.remove(contac)
                print(f"se eliminó a {borrar}")
                encontrado = True
                break
        if not encontrado:
            print("no se encontró")

    # Opción 5: Salir
    elif opcion == 5:
        print("Saliendo del programa")
        break
    else:
        print("coloca un numero no letra")'''
#tengo todos los niveles asi con ''' para que no haya una explosion portanto bucle