#19-20 lista de fruta agregar y eliminar frutas
frutas = []
while True:
    fruta = input("Ingrese el nombre de una fruta (o 'salir' para terminar): ")
    if fruta.lower() == 'salir':
        break
    frutas.append(fruta)
print("Las frutas ingresadas son:")
for fruta in frutas:
    print(fruta)
    
while True:
    fruta_eliminar = input("Ingrese el nombre de una fruta para eliminar (o 'salir' para terminar): ")
    if fruta_eliminar.lower() == 'salir':
        break
    if fruta_eliminar in frutas:
        frutas.remove(fruta_eliminar)
        print(f"{fruta_eliminar} ha sido eliminada.")
    else:
        print(f"{fruta_eliminar} no se encuentra en la lista.")
        
        #21bucar un elemento en una lista
fruta_buscar = input("ingrese el nombre de una fruta para buscarla: ")
if fruta_buscar in frutas:
    print(f"{fruta_buscar}  se encuentra en la lista.")
else:
    print(f"{fruta_buscar} no se encuentra en la lista")

#22 lista de numeros y promedio
numeros = []

while True:
    entrada = input("Usuario, ingrese un número (ingrese 0 para terminar): ")

    if not entrada.isdigit() and not (entrada.startswith('-') and entrada[1:].isdigit()):
        print("⚠️ Por favor, ingrese un número válido.")
        continue

    numero = int(entrada)

    if numero == 0:
        break

    numeros.append(numero)

if numeros:
    suma = sum(numeros)
    promedio = suma / len(numeros)
    print(f"\n Números ingresados: {numeros}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron números.")

#23 numeros pares: guardar solo los mumeros pares
numeros = []
while True:
    entrada =input("uuario ingrese unnumer0 (ingrese litsto para terminar): ")
    if entrada.lower() == "listo":
        break
    if not entrada.isdigit() and not (entrada.startswith('-') and entrada [1]. isdigit()):
        print(" Por favor ingrese un numero valido.")
        continue
    numero = int(entrada)
    if numero % 2 == 0:
        numeros.append(numero)
        print(f"el numero {numero} es par y se ha guardado exitoxamnete")
print(f"los numeros pares guardados son: {numeros}")

#24 eliminar duplicados
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7]
no_duplicados = list(set(lista))
print(f"lista: {lista}")
print(f"lita sin duplicados: {no_duplicados}")

    
            