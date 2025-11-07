""""Contador regresivo con while."""
from math import trunc

num =int(input("ingrese el numero a hacerle la cuenta regresiva: "))

while num>0:
    num-= 1
    print(f"la cuenta regresa es {num}")