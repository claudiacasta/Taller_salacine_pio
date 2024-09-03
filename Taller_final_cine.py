import os # Importamos os para operaciones del sistema de archivos

class SalaCine: # Se creo esta clase con el fin de que el código esté mas organizado. añadiendo todas las funciones en una clase
    def __init__(self):
        self.sala = []
        self.filas = 0
        self.columnas = 0

    def crear_sala(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        # Ceamos una matriz 2D inicializada con ceros (asientos libres)
        self.sala = [[0 for _ in range(columnas)] for _ in range(filas)]

    def ver_sala(self):
        # Imprimimos cada fila de la sala
        for fila in self.sala:
            print(" ".join(str(asiento) for asiento in fila))

    def asignar_puesto(self, fila, columna):
        if self.sala[fila][columna] == 0: # Si el asiento está libre
            self.sala[fila][columna] = 1 #Lo marcamos como ocupado 
            return True
        return False # El asiento ya estaba ocupado

    def guardar_sala(self):
        # Abrimos el archivo en modo escritura
        with open("sala_cine.txt", "w") as f:
            # Escribimos las dimensiones de la sala en la primera línea
            f.write(f"{self.filas},{self.columnas}\n")
            # Escribimos cada fila de la sala en una nueva linea
            for fila in self.sala:
                f.write(",".join(map(str, fila)) + "\n")
        print("Sala guardada exitosamente en 'sala_cine.txt'")

    def cargar_sala(self):
        # Verificamos si existe el archivo
        if os.path.exists("sala_cine.txt"):
            with open("sala_cine.txt", "r") as f:
                # leemos las dimensiones de la primera línea
                dimensiones = f.readline().strip().split(",")
                self.filas, self.columnas = map(int, dimensiones)
                self.sala = []
                # Leemos cada fila de la sala
                for _ in range(self.filas):
                    fila = list(map(int, f.readline().strip().split(",")))
                    self.sala.append(fila)
            print("Sala cargada exitosamente desde 'sala_cine.txt'")
            return True
        print("No se encontró un archivo de sala guardado.")
        return False

def menu_principal():
    # Imprimimos las opciones del menú
    print("\n1 - CREAR SALA")
    print("2 - VER SALA")
    print("3 - ASIGNAR PUESTO")
    print("4 - CARGAR SALA")
    print("5 - SALIR")
    return input("Seleccione la opción deseada: ")

def main():
    sala_cine = SalaCine() # Creamos una instancia de "SalaCine"

    while True:
        opcion = menu_principal() # Mostramos el memú y obtenemos la opción

        if opcion == "1":
            # Creamos una nueva sala
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            sala_cine.crear_sala(filas, columnas)
            print("La sala de cine ha sido creada exitosamente!")
            sala_cine.guardar_sala()

        elif opcion == "2":
            # Mostramos la sala actual
            if sala_cine.sala:
                print("Ver la sala de cine")
                sala_cine.ver_sala()
            else:
                print("Primero debe crear una sala.")

        elif opcion == "3":
            #Asignamos un puesto
            if sala_cine.sala:
                print("Asignar puesto")
                sala_cine.ver_sala()
                fila = int(input("Ingrese el número de fila: ")) - 1
                columna = int(input("Ingrese el número de columna: ")) - 1
                if sala_cine.asignar_puesto(fila, columna):
                    print(f"Su puesto asignado es: {fila+1},{columna+1}")
                    sala_cine.guardar_sala()
                else:
                    print("Este puesto ya está ocupado.")
            else:
                print("Primero debe crear una sala.")

        elif opcion == "4":
            # Cargamos una sala guardada previamente
            if sala_cine.cargar_sala():
                print("Sala cargada exitosamente!!")
            else:
                print("No hay sala guardada para cargar.")

        elif opcion == "5":
            # Salimos del programa
            print("Gracias por usar el sistema de reserva. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

        input("Presione <ENTER> para continuar")

if __name__ == "__main__":
    main() # Iniciamos la ejecución del programa principal