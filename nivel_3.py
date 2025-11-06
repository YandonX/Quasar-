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
contador= int(input("Ingrese un numero para iniciar el contador: "))
while contador>0:
    print(contador)
    contador-=1
