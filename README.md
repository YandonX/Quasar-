# Quasar-
this repository save code in the we are working 

Frutas = ["manzana", "pera", "mango"]
print(f"estas son las frutas que tienes: {Frutas}")

agregadas = int(input("Que cantidad de frutas vas a añadir: "))
for i in range(agregadas):
    nuevafruta = input("Ingresa la fruta que quieres agregar: ")
    Frutas.append(nuevafruta.lower())
print(f"ahora tienes las siguientes frutas: {Frutas}")

sustraidas = int(input("qué cantidad de frutas deseas eliminar: "))
for i in range(sustraidas):
    sustraida = input("nombre de la fruta que deseas sustraer: ")
    Frutas.remove(sustraida.lower())
print(f"ahora tienes las siguientes frutas: {Frutas}")

buscar = input("Ingresa la fruta que deseas buscar en tu lista, y te diré la posición: ")
if buscar in Frutas:
    print(f"la fruta {buscar} está en la lista")
    for i in range(len(Frutas)):
        if buscar == Frutas[i]:
            buscar = Frutas.index(buscar)
            print(f"en la posición {buscar + 1}")
else:
    print(f"la {buscar} no está en la lista")

Numeros = []
cantidad = int(input("¿cuantos numeros quieres ingresar a la lista? "))
for i in range(cantidad):
    numi = int(input(f"ingrese {i + 1} el número: "))
    Numeros.append(numi)

if len(Numeros) > 0:
    promedio = sum(Numeros) / len(Numeros)
    print(f"el promedio de los números es: {promedio:.2f}")
else:
    print("No ingresaste ningún número.")

