"""
Sumar hasta que el usuario escriba 0.
"""
n = int(input("ingrese un numero: "))
sum = 0
while n !=0:
    sum += n
    n= int(input("ingrese otro numero: "))

if n == 0:
    print(f"la suma es {sum} y haz salido del final")



