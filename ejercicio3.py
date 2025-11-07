#13 contar del uno al 10
for i in range(1, 11):
    print(i)
    
#14 sumatoria del 1 al n
n = int(input("usuario ingresar un numero entero positivo: "))
for i in range(1, n + 1):
    print(i)
if n > 0:
    suma = sum(range(1, n + 1))
    print(f"la sumatoria del 1 al {n} es {suma}")
    
#15tabla de multiplicar
num = int(input("usuario ingrese un numero para su tabla de multiplicar: "))


for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    
#16 cuenta regresiva con while
n = int(input("ingrese un numero para la cuenta regresiva: "))
while n >= 0:
    print(n)
    n -= 1
    
#17 adivina el numero
import random
numero_secreto = random.randint(1, 100)
intentos = 0
print("¡Bienvenido al juego de adivina el número! Estoy pensando en un número entre 1 y 100.")
while True:
    intento = int(input("Por favor, ingresa tu intento: "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        break
    
#18umar hasta que el usuario ecriba 0
suma = 0
while True:
    numero = int(input("usuario ingrese un numero (ingrese 0 para terminar: "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")
        
    