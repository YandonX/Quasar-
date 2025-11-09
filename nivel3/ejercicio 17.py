"""
Adivina el número (usar random).
"""
import random
from string import ascii_letters

aleatorio = random.randint(1, 10)

while True:
    num =int(input("ingrese el numero: "))
    if num == aleatorio:
        print("ADIVINASTE EL NÚMERO")
        break
    elif num > aleatorio:
        print("estas por encima")
    elif num < aleatorio:
        print("estas por debajo")


