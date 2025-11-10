name= input("Ingrese el nombre del producto: ")
while True:
    price=input("Por Favor ingrese el precio: ")
    try:
        price= float(price)
        break
    except ValueError:
        print("Asegurate de ingresar un numero, sin espacios ni puntuacion")

while True:
    quantity= input("Ingrese la cantidad: ")
    try:
        quantity= int(quantity)
        if quantity <=0:
            print("Valor no es válido")
        else:
            break
    except ValueError:
        print("Asegurate de que ingreses números")

total_value= quantity*price

print(f"compraste {quantity} {name}/s, el valor unitario es: ${price:.1f}\n por lo que el total es: ${total_value:.1f}")