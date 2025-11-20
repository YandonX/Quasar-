import csv
import os

class CRUD:


    def crear_csv(self,archivo):
        if not os.path.exists(archivo):
            with open(archivo,"w", newline="") as file:
                escritor= csv.writer(file)
                escritor.writerow(["id","Nombre","Edad"])

    def obtener_id(self,archivo):
        with open(archivo, "r") as file:
            filas = list(csv.reader(file))
        
        if len(filas) == 1:
            return 1
        
        ultimo_id = int(filas[-1][0])

        return ultimo_id+1

    
    def agregar_linea(self,archivo,nombre,edad):
        id_nuevo= self.obtener_id(archivo)
        with open(archivo, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([id_nuevo,nombre,edad])
            return id_nuevo
        
    def listar(self,archivo):
        with open(archivo,"r") as file:
            reader= csv.reader(file)
            next(reader)
            return list(reader)
        
    def eliminar(self, archivo):
        id_buscar = int(input("Ingrese el ID a eliminar: "))

        # Leer todas las filas
        with open(archivo, "r") as file:
            filas = list(csv.reader(file))

        # Recorrer desde la segunda fila (índice 1) para no tocar encabezado
        for i in range(1, len(filas)):
            if int(filas[i][0]) == id_buscar:
                print(f"\n¿Seguro deseas eliminar a {filas[i][1]}?")
                confirmar = input("Escribe SI para confirmar, cualquier otra cosa para cancelar: ")

                if confirmar.lower() == "si":
                    filas.pop(i)  # eliminar la fila
                    # Guardar cambios en el CSV
                    with open(archivo, "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(filas)
                    print("Registro eliminado")
                else:
                    print("Eliminación cancelada")
                return

        print("Registro no encontrado")


    def actualizar_paciente():

        id_buscar = input("ID del registro a actualizar: ")

        with open(archivo, "r") as file:
            filas = list(csv.reader(file))
            for fila in filas:
                


        for p in archivo:
            if p["id"] == id_buscar:
                print("\n¿Qué deseas actualizar?")
                print("1. Nombre")
                print("2. Edad")
                
                opcion = input("Opción: ")

                if opcion == "1":
                    nueva_edad = int(input("Nueva edad: "))
                    p["edad"] = nueva_edad
                elif opcion == "2":
                    nuevo_diag = input("Nuevo diagnóstico: ")
                    p["diagnostico"] = nuevo_diag
                elif opcion == "3":
                    evento = input("Nuevo evento: ")
                    p["historial"].append(evento)
                else:
                    print("Opción inválida")
                    return

                # guardar_datos() --- revisar como guardar datos
                print("registro actualizado")
                return
    
    print("Registro no encontrado")