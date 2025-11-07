"""
Números pares: guardar solo los pares.
"""

numpares=[]

for i in range(1,11):
    z=int(input(f"ingrese el numero {i}: "))
    if z%2 == 0:
        numpares.append(z)

print(f" los numeros pares son {numpares} ")



