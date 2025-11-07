"""
Tabla de multiplicar.
"""

x =int(input("ingrese el numero a multiplica"))

for i in range(1,11):
    resultado = x * i
    print(f"{x} x {i} = {resultado}")

