# 13 Print numbers from 0 to 10
'''for i in range(1,11):
    print(i)'''
# 14 Sumatoria del 1 al n.
'''n= int(input("Ingrese un numero: "))
suma=0
for i in range(1,n+1):
    suma+=i
    print("La suma es: ", suma)'''
# 15 tabla de multiplicar.
'''multi=int(input("Ingrese un numero para ver su tabla de multiplicar: "))
for i in range(1,11):
    print(f"{multi} x {i} = {multi*i}")'''

# 16 contador con ciclo while
'''contador= int(input("Ingrese un numero para iniciar el contador: "))
while contador>0:
    print(contador)
    contador-=1'''
# 17 Adivina el número (usar random
'''import random
numero_secreto= random.randint(1,10)
while True:
    intento = int(input("Adivina el numero: "))
    if intento == numero_secreto:
        print("Felicidades! Adivinaste el numero.")
        break
    else:
        print("Intenta de nuevo.")'''
# 18 Sumar hasta que el usuario escriba 0.
'''total= 0 
while True:
    numero= int (input("ingresa un numero para sumar: "))
    if numero == 0:
        break
    total = total + numero
print("La suma total es: ", total)'''

        




