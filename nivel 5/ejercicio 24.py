"""
Sistema de calificaciones.

"""
calificaciones_clase = {
    "Ana López": [8.5, 9.0, 7.5, 10.0],
    "Juan Pérez": [6.0, 7.0, 5.5, 8.0],
    "María García": [9.5, 10.0, 9.0, 9.8],
    "Pedro Ruiz": [4.0, 5.0, 6.5, 5.0]
}
for nombre, lista_notas in calificaciones_clase.items():
    suma_notas = sum(lista_notas)
    cantidad_notas = len(lista_notas)

    if cantidad_notas > 0:
        promedio = suma_notas / cantidad_notas
    else:
        promedio = 0


    estado = ""
    if promedio >= 7.0:
        estado = "APROBADO"
    elif promedio >= 5.0:
        estado = "REMEDIAL"
    else:
        estado = "REPROBADO"


    print(f"Estudiante: {nombre}")
    print(f"  Notas registradas: {lista_notas}")
    print(f"  Promedio Final: {promedio:.2f}")
    print(f"  Estado: {estado}")