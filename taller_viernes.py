# Este bucle pide el nombre del producto
while True:
    productos = input("Ingrese el nombre del producto: ")

    # este if y else verifican que el texto no contenga números ni símbolos
    if productos.isalpha():
        break  # Sale del bucle si está correcto
    else:
        print("Por favor ingrese solo letras, sin números ni símbolos.")

# Variable para guardar el precio y canticadad
cantidad = None
precio = None

# este bucle pide el precio del producto
while True:
    try:
        # Convierte el valor ingresado a numero decimal
        precio = float(input("Ingresa el precio del producto: "))
        break  # Sale del bucle si el valor es correcto
    except ValueError:
        # Si el usuario pone algo que no es número le lanza este mensaje
        print("Por favor ingrese un valor numérico para el precio.")

# Bucle para pedir la cantidad de productos
while True:
    try:
        # Convierte el valor ingresado a numero entero
        cantidad = int(input("Ingresa la cantidad del producto: "))
        break  # Sale del bucle si el valor es válido
    except ValueError:
        # Si el usuario pone algo que no es número, muestra este mensaje
        print("Por favor ingrese un valor numérico para la cantidad.")

# Calcula el total multiplicando precio por cantidad
costo_total = cantidad * precio

# Muestra el resultado con formato (dos decimales)
print(f"El total por {cantidad} unidades de {productos} es: {costo_total}")

#https://drive.google.com/file/d/1OCJqt6rQSsRVLiMskglLK4v02-e8i0NL/view?usp=drive_link
