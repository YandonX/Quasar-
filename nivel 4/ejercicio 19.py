"""
Lista de frutas.
"""
print(" se agregaran diez frutas a su carrito: ")
frutas=[]
frutas2=["mango, pera "]
for i in range (0,5):
    fruta =str(input("ingrese la fruta: "))
    frutas.append(fruta)
    z = frutas+[frutas2]
    print(f"su carrito cuenta con {z}")


