# 13 — Contar del 1 al 10
'''
# El ciclo for recorre los números del 1 al 10
for i in range(1, 11):
    print(i)
'''

# 14 — Sumatoria del 1 al n
'''
# Se pide un número al usuario
n = int(input("Ingrese un número: "))
suma = 0

# Se usa un ciclo for para sumar todos los números desde 1 hasta n
for i in range(1, n + 1):
    suma += i

print("La suma es:", suma)
'''

# 15 — Tabla de multiplicar
'''
# El usuario ingresa un número
multi = int(input("Ingrese un número para ver su tabla de multiplicar: "))

# Se recorre del 1 al 10 y se muestra la multiplicación
for i in range(1, 11):
    print(f"{multi} x {i} = {multi * i}")
'''

# 16 — Contador regresivo con while
'''
# Se pide un número para iniciar el conteo regresivo
contador = int(input("Ingrese un número para iniciar el contador: "))

# El ciclo while se repite hasta que el contador llegue a 0
while contador > 0:
    print(contador)
    contador -= 1
'''

# 17 — Adivina el número (usar random)
'''
# Se importa la librería random para generar un número aleatorio
import random

# Se genera un número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

# Se repite hasta que el usuario adivine
while True:
    intento = int(input("Adivina el número: "))
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        break
    else:
        print("Intenta de nuevo.")
'''

# 18 — Sumar hasta que el usuario escriba 0
'''
total = 0 

# Se repite hasta que el usuario escriba 0
while True:
    numero = int(input("Ingresa un número para sumar (0 para salir): "))
    if numero == 0:
        break
    total += numero

print("La suma total es:", total)
'''
#tengo todos los niveles asi con ''' para que no haya una explosion portanto bucle


