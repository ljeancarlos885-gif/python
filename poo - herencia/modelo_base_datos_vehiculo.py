"""crear la base de datos vehiculo"""
class BaseDatosvehiculo:
    """Simula una base de datos de vehiculos usando una lista."""

    def __init__(self):
        """Inicializa la lista de vehiculos."""
        self.vehiculo = []

    def crear_vehiculo(self, nombre_vehiculo):
        """Agrega un nuevo vehiculo a la lista."""
        self.vehiculo.append(nombre_vehiculo)
        print(f'vehiculo"{nombre_vehiculo}" agregado exitosamente.')

    def agregar_elementos_al_final(self, lista_vehiculo):
        """Agrega varios vehiculos al final de la lista."""
        self.vehiculo.extend(lista_vehiculo)
        print(f"Se agregaron los vehiculos: {lista_vehiculo}")

    def insertar_vehiculo(self, posicion, vehiculo):
        """Inserta  vehiculoes en una posicion especifica."""
        self.vehiculo.insert(posicion, vehiculo)
        print(f'vehiculoes "{vehiculo}" insertada en la posicion {posicion}.')

    def eliminar_vehiculo(self, nombre):
        """Elimina  vehiculoes por su nombre."""
        if nombre in self.vehiculo:
            self.vehiculo.remove(nombre)
            print(f'vehiculo "{nombre}" eliminado correctamente.')
        else:
            print(f'No se encontro el vehiculo "{nombre}".')

    def eliminar_por_posicion(self, posicion):
        """Elimina el vehiculo segun su posicion."""
        try:
            vehiculoes_eliminada = self.vehiculo.pop(posicion)
            print(f'Se elimino el vehiculo en la posicion {posicion}: "{vehiculo_eliminado}".')
        except IndexError:
            print("Error: la posicion ingresada no existe en la lista.")

    def obtener_posicion(self, nombre):
        """Muestra la posicion de un vehiculo en la lista."""
        if nombre in self.vehiculo:
            posicion = self.vehiculo.index(nombre)
            print(f'El vehiculo "{nombre}" se encuentra en la posicion {posicion}.')
        else:
            print(f'No se encontro el vehiculo "{nombre}".')

    def contar_vehiculoes(self, nombre):
        """Cuenta cuantas veces aparece un vehiculo."""
        cantidad = self.vehiculo.count(nombre)
        print(f'El vehiculo "{nombre}" aparece {cantidad} vez/veces en la lista.')


    def ordenar_vehiculo(self):
        """Ordena los vehiculoes alfabeticamente."""
        self.vehiculo.sort()
        print("Los vehiculoes fueron ordenadas alfabeticamente.")

    def invertir_orden(self):
        """Invierte el orden actual de los vehiculoes."""
        self.vehiculo.reverse()
        print("El orden de los vehiculo fue invertido.")

    def mostrar_vehiculo(self):
        """Muestra todas los vehiculoes de la lista."""
        print("Lista actual del vehiculo:", self.vehiculo)


# ------------------ MENU CRUD ------------------
def menu():
    """Muestra el menu principal del programa."""
    base = BaseDatosvehiculo()

    while True:
        print("\n--- MENU vehiculo ---")
        print("1. Agregar vehiculoes")
        print("2. Agregar varias vehiculoes")
        print("3. Insertar vehiculo en posicion")
        print("4. Eliminar vehiculo por nombre")
        print("5. Eliminar vehiculo por posicion")
        print("6. Buscar posicion del vehiculo")
        print("7. Contar cuantas veces aparece el vehiculo")
        print("8. Ordenar vehiculoes")
        print("9. Invertir orden")
        print("10. Mostrar todas los vehiculoes")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese los vehiculoes :")
            base.crear_vehiculoes(nombre)

        elif opcion == "2":
            nombres = input("ingrese varios vehiculoes separadas por , : ")
            lista = [n.strip() for n in nombres.split(",")]
            base.agregar_elementos_al_final(lista)

        elif opcion == "3":
            nombre = input(" tipo de vehiculoes: ")
            pos = int(input("Posicion donde insertarlo: "))
            base.insertar_vehiculoes(pos, nombre)

        elif opcion == "4":
            nombre = input("Ingrese el tipo de vehiculoes a eliminar: ")
            base.eliminar_vehiculoes(nombre)

        elif opcion == "5":
            pos = int(input("Ingrese la posicion a eliminar: "))
            base.eliminar_por_posicion(pos)

        elif opcion == "6":
            nombre = input("Ingrese el vehiculo a buscar: ")
            base.obtener_posicion(nombre)

        elif opcion == "7":
            nombre = input("Ingrese los vehiculoes a contar: ")
            base.contar_vehiculoes(nombre)

        elif opcion == "8":
            base.ordenar_vehiculo()

        elif opcion == "9":
            base.invertir_orden()

        elif opcion == "10":
            base.mostrar_vehiculo()

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida, por favor intente de nuevo.")


# Ejecutar el menu solo si se ejecuta directamente
if __name__ == "__main__":
    menu()
