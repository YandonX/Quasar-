"""
Buscar un elemento en la lista.
"""

ropa=["camisa", "camiseta", "pantalon","saco", "corbata"]
print(f"los elementos con que cuenta la tienda son:{ropa} ")
busqueda= input("que elemento deseas buscar: ")

while True:

    if busqueda in ropa:
        print(f"poseemos {busqueda}")
        break
    else:
        print(f"recuerda que solo contamos con {ropa}")