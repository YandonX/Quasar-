#7 edad delusuario
nombre = input("usuario porfavor ingrese su nombre: ")
edad = int(input("usuario porfavor ingrese su edad: "))
if edad >= 18:
    print(f"Hola {nombre}, tienes {edad} eres mayor de edad.")
else:
    print(f"Hola {nombre}, tienes {edad} eres menor de edad.")

#8 numero positivo, negativo o cero
numero = int(input("porfavor ingrese un número: "))
if numero > 0:
    print(f"el numero {numero} es positivo.")
elif numero < 0:
    print(f"el numero {numero} es negativo.")
else:
    print("el numero es cero.")
    
#9 numero par o impar
numero = int(input("porfavor ingresar un numero:"))
if numero % 2 == 0:
    print(f"el numero {numero} es par.")
else:
    print(f"el numero {numero} es impar.")

#10 calculadora simple
num1 = int(input("usuario ingrese el primer numero:"))
num2 = int(input("usuario ingrese el segundo numero:"))
operacion = input("usuario ingrese la operacion (+, -, *, /): ")
if operacion == "+":
    resultado = num1 + num2
    print(f"el resultado de {num1} + {num2} es {resultado}.")
elif operacion == "-":
    resultado = num1 - num2
    print(f"el resultado de {num1} - {num2} es {resultado}.")
elif operacion == "*":
    resultado = num1 * num2
    print(f"el resultado de {num1} * {num2} es {resultado}.")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"el resultado de {num1} / {num2} es {resultado}.")
    else:
        print("Error: No se puede dividir por cero.")
else:
   print("Operacion no valida.")
   
#11 calificador de notas aprobado reprobado y excelente
nota = float(input("usuario porfavor ingrese la nota (0-5.0): "))
if 0 <= nota <3.0:
    print("Reprobado")
elif 3.0 <= nota < 4.5:
    print("aprobado")
elif 4.5 <= nota <= 5.0:
    print("exelente")
else:
    print("nota no valida.")
    
#12 comparador de tre nmeros: mayor y menor
num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
print(f"el numero mayor es: {mayor}")
print(f"el numero menor e: {menor}")
   
