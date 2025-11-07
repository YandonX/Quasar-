# 19, 20, 
'''frutas = [] 

while True:
    print("opciones:")
    print("1. Agregar fruta")
    print("2. Eliminar fruta")
    print("3. Mostrar frutas")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        fruta = input("Ingresa una fruta: ")
        frutas.append(fruta)
        print(f"{fruta} fue agregada a la lista.")

    elif opcion == "2":
        fruta = input("¿Qué fruta deseas eliminar?: ")
        if fruta in frutas:
            frutas.remove(fruta)
            print(f"{fruta} fue eliminada.")
        else:
            print(f"{fruta} no está en la lista.")
    elif opcion == "3":
        print("ver lista")
        for f in frutas:
            print(f"-", f)
            break
    elif opcion == "4":
        print("saliendo del programa")
    else:
        print("opcion no validad")'''

#21 Buscar un elemento en la lista.
'''estudiantes=["anan","segio", "alejo", "andres","michel"]
nombre=input("que estudiantes deseas bucas?: ")
if nombre in estudiantes:
    print(f"{nombre}encontrado")
else:
    print("no se encuentra en la lista")'''

#22 Lista de números y promedio.
'''numeros= []
while True:
    entrada= (input("ingresa un numero: "))
s_pares=[] if entrada. lower() == "salir":

        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:      
      print("por favor ingresa numeros")

if len(numeros) >  0 :
          promedio= sum(numeros) / len(numeros)
          print(f"el promedio es {promedio: .2f}")
else:
        print("ingresa un numero no letras")'''

# 23 Números pares: guardar solo los pares.
'''pares= []

for i in range(100):
    if i % 2 == 0:
        pares.append(i)

print(pares)'''

#24 eliminar duplicados
'''frutas=["mango","lulo","manzana"]
while True:
    fruta= input("ingresa una fruta: ")

    if fruta.lower()== "salir":
     
     break

    frutas.append(fruta)
frutas= list(set(frutas))
print(frutas)'''

