"""
Clasificador de notas (Excelente, Aprobado, Reprobado).
"""
nota=float(input("ingrese su nota: "))

if nota >3:
    print(f"su nota es {nota} y es excelente")
elif nota == 3:
    print(f"su nota es {nota} y aprobaste")
elif nota <3:
    print(f"su nota es{nota} y reprobaste")