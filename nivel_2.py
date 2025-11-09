# 7 — Mayor de edad
'''
# Se pide la edad al usuario y se compara con 18
edad = 18 
edades = int(input("Ingrese su edad: "))
if edades >= edad:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
'''

# 8 — Número positivo, negativo o cero
'''
# Se pide un número y se evalúa si es mayor, menor o igual a 0
numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es igual a 0")
'''

# 9 — Número par o impar
'''
# Se usa el operador módulo (%) para saber si tiene residuo al dividir entre 2
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
'''

# 10 — Calculadora básica
'''
# El usuario ingresa dos números y el tipo de operación que quiere realizar
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operaciones = input("Ingrese la operación (+, -, *, /): ")

if operaciones == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operaciones == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operaciones == "*":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operaciones == "/":
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
else:
    print("Operación no válida")
'''

# 11 — Clasificador de notas
'''
# Se pide la nota del estudiante y se evalúa su rango para dar una calificación
nota = int(input("Ingrese la nota del estudiante (0-100): "))

if nota >= 100:
    print("Excelente aprobaste.")
elif nota > 90:
    print("El estudiante ha aprobado.")
elif nota > 80:
    print("El estudiante ha aprobado.")
elif nota > 70:
    print("El estudiante ha aprobado.")
else:
    print("El estudiante ha reprobado.")
'''

# 12 — Comparador de tres números (mayor y menor)
'''
# Se comparan tres números para encontrar el mayor y el menor
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Comparar el mayor
if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")

# Comparar el menor
if num1 <= num2 and num1 <= num3:
    print(f"El número menor es: {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"El número menor es: {num2}")
else:
    print(f"El número menor es: {num3}")
'''
#tengo todos los niveles asi con ''' para que no haya una explosion portanto bucle