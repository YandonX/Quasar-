# 19 y 20 — Lista de frutas: Agregar, eliminar y mostrar
'''
# Se crea una lista vacía para guardar las frutas
frutas = [] 

while True:
    print("opciones:")
    print("1. Agregar fruta")
    print("2. Eliminar fruta")
    print("3. Mostrar frutas")
    print("4. Salir")

    # Se pide una opción al usuario
    opcion = input("Elige una opción (1-4): ")

    # Si elige 1, agrega una nueva fruta a la lista
    if opcion == "1":
        fruta = input("Ingresa una fruta: ")
        frutas.append(fruta)
        print(f"{fruta} fue agregada a la lista.")

    # Si elige 2, elimina una fruta si está en la lista
    elif opcion == "2":
        fruta = input("¿Qué fruta deseas eliminar?: ")
        if fruta in frutas:
            frutas.remove(fruta)
            print(f"{fruta} fue eliminada.")
        else:
            print(f"{fruta} no está en la lista.")

    # Si elige 3, muestra todas las frutas guardadas
    elif opcion == "3":
        print("ver lista:")
        for f in frutas:
            print(f"-", f)

    # Si elige 4, sale del programa
    elif opcion == "4":
        print("saliendo del programa")
        break
    else:
        print("opcion no válida")
'''

# 21 — Buscar un elemento en la lista
'''
# Se crea una lista de estudiantes
estudiantes = ["anan", "segio", "alejo", "andres", "michel"]

# Se pide el nombre a buscar
nombre = input("¿Qué estudiante deseas buscar?: ")

# Se verifica si el nombre está en la lista
if nombre in estudiantes:
    print(f"{nombre} fue encontrado.")
else:
    print("No se encuentra en la lista.")
'''

# 22 — Lista de números y promedio
'''
numeros = []

# Se usa un bucle para pedir números al usuario
while True:
    entrada = input("Ingresa un número (o escribe 'salir' para terminar): ")

    # Si el usuario escribe "salir", se rompe el ciclo
    if entrada.lower() == "salir":
        break

    # Se intenta convertir la entrada en número
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, ingresa solo números.")

# Si hay números en la lista, se calcula el promedio
if len(numeros) > 0:
    promedio = sum(numeros) / len(numeros)
    print(f"El promedio es: {promedio:.2f}")
else:
    print("No se ingresaron números.")
'''

# 23 — Números pares: guardar solo los pares
'''
pares = []

# Se recorre del 0 al 99
for i in range(100):
    # Si el número es par (módulo 2 igual a 0)
    if i % 2 == 0:
        pares.append(i)

print("Números pares del 0 al 99:")
print(pares)
'''

# 24 — Eliminar duplicados
'''
frutas = ["mango", "lulo", "manzana"]

# Se piden frutas al usuario
while True:
    fruta = input("Ingresa una fruta (o escribe 'salir' para terminar): ")

    if fruta.lower() == "salir":
        break

    frutas.append(fruta)

# Se convierte la lista en un conjunto para eliminar duplicados
frutas = list(set(frutas))

print("Lista final sin duplicados:")
print(frutas)
'''
