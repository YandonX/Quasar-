#1 y 6: pedir al usuario su nombre y edad, luego mostrar un mensaje con esa información y la edad en 10 años
nombre = input("uuario porfavor ingresaru nombre: ")
edad = int(input("usuario porfavor ingrese su edad: "))
edad_futura = edad + 10
print(f"Hola {nombre}, tienes {edad} años. En 10 años tendrás {edad_futura} años.") 


#2 suma de dos números
num1 = float(input("usuario porfavor ingrese el primer número: "))
num2 = float(input("usuario porfavor ingrese el segundo número: "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}.")


#3 area de un triamgulo
base = float(input("usuario porfavor ingrese la base del triángulo: ")) 
altura = float(input("usuario porfavor ingrese la altura del triángulo: "))
area = (base * altura) / 2
print(f"el area del triangulo es: {area}")

#4 convertir grados Celsius a Fahrenheit
fahrenhet = float(input("usuario porfavor ingrese la temperatura en grados Celsius: "))
celsius = (fahrenhet * 9/5) + 32
print(f"{fahrenhet} grados Celsius son {celsius} grados Fahrenheit.")

#5 uso del type
type(nombre)
type(edad)
type(num1)
type(num2)
type(base)
type(altura)
type(fahrenhet)
type(celsius)
print(type(nombre))
print(type(edad))
print(type(num1))
print(type(num2))
print(type(base))
print(type(altura))
print(type(fahrenhet))
print(type(celsius))