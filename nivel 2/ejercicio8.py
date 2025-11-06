"""
Número positivo, negativo o cero.
"""

num= int(input("porfavor ingrese su numero: "))

if num >0:
    print(f"su numero es {num} y es positivo")
elif num <0:
    print(f"su numero es {num} y es negativo")
else:
    print("su numero es 0")