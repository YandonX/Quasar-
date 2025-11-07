#Segun la documentacion un string siempre sera string entonces no necesita validacion
nombre= str(input('porfavor ingrese el nombre del producto:'))



#Solicitud del precio float
#Este código usa un bucle infinito (while True) y la instrucción break para salir solo si la conversión de datos es exitosa.
#dato ingresado es un float y en caso de que se ingrese algo en str pueda pedir que ingrese el dato como es requerido

precio= None
#Utilizamos un bucle para validar la entrada del precio
while True:
    entrada_precio= input('porfavor ingrese el precio del producto:')
    try:
        precio= float(entrada_precio)
        break
    except ValueError:
        print('Dato invalido porfavor ingrese el precio en numero')


cantidad= None
while True:
    entrada_cantidad= input('porfavor ingrese la cantidad de producto:')
    try:
        cantidad= int(entrada_cantidad)
        break
    except ValueError:
        print('Dato invalido por favor ingrese un cantidad en numero')

costo_total= precio * cantidad


## ✅ Datos Finales Válidos
print("\n--- ¡Datos de Producto Registrados! ---")
print(f"Nombre: **{nombre}**")
print(f"Precio: **{precio}**")
print(f"Cantidad: **{cantidad}**")
print(f'El Costo total del **{costo_total}**')

#el programa en si pide al usuario ingresar el nombre, precio y cantidad de un producto,
# luego calcula el costo total multiplicando el precio por la cantidad y muestra todos los datos ingresados junto con el costo total.
#aqui se asegura que el precio sea un numero decimal(float) y la cantidad un numero entero(int)
# Si el usuario ingresa un valor no valido, se le pide que ingrese el dato nuevamente hasta que sea correcto.
# Al final, se imprimen todos los datos del producto ingresado por el usuario.
# El uso de validaciones mejora la robustez del programa al manejar entradas incorrectas de manera adecuada.
# Esto es especialmente útil en aplicaciones del mundo real donde los usuarios pueden cometer errores al ingresar datos.
# Se utilizan bloques try-except para capturar errores de conversión y proporcionar retroalimentación al usuario.
# Se utiliza el blucle while True para repetir la solicitud de entrada hasta que se obtenga un valor válido.
# En resumen, este código es un ejemplo básico de cómo interactuar con el usuario, validar entradas y realizar cálculos simples en Python.
