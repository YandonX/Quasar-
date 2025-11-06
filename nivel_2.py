# 7 mayor de edad
edad = 18 
edades = int(input("Ingrese su edad: "))
if edades >= edad:
     print("Eres mayor de edad")
else:
     print("Eres menor de edad")

# 8 numero positivo, negativo o cero
numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")  
else:
    print("El número es igual a 0")
# 9 número par o impar
num = int(input("Ingrese un número: "))
if num % 2 == 0:
     print("El número es par")  
elif num % 2 != 0:
     print("El número es impar")
else: 
     print("El número es cero")
# 10 calculadora basica
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))
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
     print(f"el resultado de la división es: {resultado}")
else:
        print("Operación no válida")

#clasificador de notas 
nota= int(input("Ingrese la nota del estudiante (0-100): "))
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
# comparador de 3 numeros
num1 = float (input("Ingrese el primer número: "))
num2 = float (input("Ingrese el segundo número: "))
num3 = float (input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")

if num1 <= num2 and num1 <= num3:
    print(f"El número menor es: {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"El número menor es: {num2}")
else:
    print(f"El número menor es: {num3}")
