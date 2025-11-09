"""
Comparador de tres números: mayor y menor.
"""
num1=int(input("ingrese el primer numero: "))
num2= int(input("ingrese el segundo numero:"))
num3= int(input("ingrese el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"el numero {num1} es el mayor")
elif num2> num1 and num2>num3:
    print(f"el numero {num2} es el mayor")
elif num3 >num1 and num3>num2:
    print(f"el numero {num3} es el mayor")


if num1 < num2 and num1 < num3:
    print(f"el numero {num1} es el menor")
elif num2< num1 and num2<num3:
    print(f"el numero {num2} es el menor")
elif num3 <num1 and num3<num2:
    print(f"el numero {num3} es el menor")