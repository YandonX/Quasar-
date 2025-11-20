from archivo_Json import cargar_datos, guardar_datos
from registrar_paciente import *
from busqueda import *
from actualizacion import actualizar_paciente
from eliminar_paciente import eliminar_paciente
from reportes import *

# Lista global de pacientes
pacientes = []

# ==================== MENÚ PRINCIPAL ====================

def menu_principal():
    cargar_datos()
    
    while True:
        print("\n" + "="*38)
        print("   SISTEMA DE GESTIÓN DE PACIENTES")
        print("="*38)
        print("1. Registrar paciente")
        print("2. Buscar paciente")
        print("3. Actualizar paciente")
        print("4. Eliminar paciente")
        print("5. Reportes")
        print("6. Salir")
        print("="*38)
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            menu_buscar()
        elif opcion == "3":
            actualizar_paciente()
        elif opcion == "4":
            eliminar_paciente()
        elif opcion == "5":
            menu_reportes()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

# Iniciar el programa
menu_principal()