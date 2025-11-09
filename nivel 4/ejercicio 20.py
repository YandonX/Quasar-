"""
Agregar y eliminar frutas.
"""

frutas=[]
z=None

for i in range (0,5):
    fruta =str(input("ingrese la fruta: "))
    frutas.append(fruta)

    print(f"su carrito cuenta con {frutas}")

z=input("que elemento deseas quitar de tu carrito: ")

frutas.remove(z)

print(f"haz quitado {z} de tu carrito y ahora solo posee{frutas}")