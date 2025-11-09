"""
Lista de números y promedio.
"""
numeros=[]
i=0
sum=0
for i in range(1,6):

    numero=int(input(f"ingrese la nota {i}: "))
    numeros.append(numero)
    sum+= numero
prom= (sum/i)

print(f"sus notas son {numeros} y su promedio es {prom}")

