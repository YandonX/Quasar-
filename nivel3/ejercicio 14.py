"""
Sumatoria del 1 al n.
"""

n= int(input("ingrese hasta que numero que desea sumar"))

suma= 0
for i in range(1,n+1):
    suma += i
print(f"el resultado de la suma es: {suma}")