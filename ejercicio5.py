#25 sistema de calificaciones
calificaciones = []
n = int(input("cunatas calificaciones tienes: "))
for i in range(n):
    ingresar = float(input("ingrese us calificaciones (0-5.0): "))
    calificaciones.append(ingresar)
promedio = sum(calificaciones) / n
print(f"el promedio de tus calificaciones es: {promedio:.2f}")

#26 carrito de compras
carrito = []  

while True:
    producto = input("Ingrese el nombre del producto (o 'ok' para terminar): ")

    if producto.lower() == 'ok':  
        break

    precio = float(input("Ingrese el precio del producto: "))
    carrito.append((producto, precio))


total = sum(precio for _, precio in carrito)


print("\nProductos en el carrito:")
for producto, precio in carrito:
    print(f"- {producto}: ${precio:.3f}")

print(f"\nTotal a pagar: ${total:.3f}")

#27 cajero automatico
saldo = 1000.0
while True:
    print("\nBienvenido al Cajero Automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        print(f"Su saldo actual es: ${saldo:.3f}")
    elif opcion == '2':
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print(f"Has depositado ${deposito:.3f}. Nuevo saldo: ${saldo:.3f}")
    elif opcion == '3':
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Has retirado ${retiro:.3f}. Nuevo saldo: ${saldo:.3f}")
    elif opcion == '4':
        print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

#28 gestion de estudiantes (mini base de datos)
estudiantes = {}
while True:
    print("\nGestión de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Ver estudiantes")
    print("3. Eliminar estudiante")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiantes[nombre] = edad
        print(f"Estudiante {nombre} agregado.")
    elif opcion == '2':
        if estudiantes:
            print("\nLista de Estudiantes:")
            for nombre, edad in estudiantes.items():
                print(f"- {nombre}, Edad: {edad}")
        else:
            print("No hay estudiantes registrados.")
    elif opcion == '3':
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print(f"Estudiante {nombre} eliminado.")
        else:
            print(f"No se encontró al estudiante {nombre}.")
    elif opcion == '4':
        print("Saliendo de la gestión de estudiantes. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

#29 calculadora avanzada
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
while True:
    print("\nCalculadora Avanzada")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {dividir(num1, num2)}")
    elif opcion == '5':
        print("Saliendo de la calculadora avanzada. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        
#30 agenda de contactos (lista de diccionarios)
agenda = []
while True:
    print("\nAgenda de Contactos")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        contacto = {"nombre": nombre, "telefono": telefono}
        agenda.append(contacto)
        print(f"Contacto {nombre} agregado.")
    elif opcion == '2':
        if agenda:
            print("\nLista de Contactos:")
            for contacto in agenda:
                print(f"- {contacto['nombre']}, Teléfono: {contacto['telefono']}")
        else:
            print("No hay contactos en la agenda.")
    elif opcion == '3':
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        for contacto in agenda:
            if contacto['nombre'] == nombre:
                agenda.remove(contacto)
                print(f"Contacto {nombre} eliminado.")
                break
        else:
            print(f"No se encontró al contacto {nombre}.")
    elif opcion == '4':
        print("Saliendo de la agenda de contactos. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
    
 
     
    