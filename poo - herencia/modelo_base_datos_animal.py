"""crear la base de datos animales"""
class BaseDatosAnimal:
    """Simula una base de datos de animales usando una lista."""

    def __init__(self):
        """Inicializa la lista de animales."""
        self.animal = []

    def crear_animales(self, nombre_animal):
        """Agrega un nuevo animal a la lista."""
        self.animal.append(nombre_animal)
        print(f'animal"{nombre_animal}" agregado exitosamente.')

    def agregar_elementos_al_final(self, lista_animal):
        """Agrega varios animales al final de la lista."""
        self.animal.extend(lista_animal)
        print(f"Se agregaron los animales: {lista_animal}")

    def insertar_animales(self, posicion, nombre_animales):
        """Inserta  animales en una posicion especifica."""
        self.animal.insert(posicion, nombre_animales)
        print(f'animales "{nombre_animales}" insertada en la posicion {posicion}.')

    def eliminar_animales(self, nombre):
        """Elimina  animales por su nombre."""
        if nombre in self.animal:
            self.animal.remove(nombre)
            print(f'animal "{nombre}" eliminado correctamente.')
        else:
            print(f'No se encontro el animal "{nombre}".')

    def eliminar_por_posicion(self, posicion):
        """Elimina animales segun su posicion."""
        try:
            animales_eliminada = self.animal.pop(posicion)
            print(f'Se elimino el animal en la posicion {posicion}: "{animales_eliminada}".')
        except IndexError:
            print("Error: la posicion ingresada no existe en la lista.")

    def obtener_posicion(self, nombre):
        """Muestra la posicion de un animal en la lista."""
        if nombre in self.animal:
            posicion = self.animal.index(nombre)
            print(f'El animal "{nombre}" se encuentra en la posicion {posicion}.')
        else:
            print(f'No se encontro el animal "{nombre}".')

    def contar_animales(self, nombre):
        """Cuenta cuantas veces aparece un animal."""
        cantidad = self.animal.count(nombre)
        print(f'El animal "{nombre}" aparece {cantidad} vez/veces en la lista.')


    def ordenar_animal(self):
        """Ordena los animales alfabeticamente."""
        self.animal.sort()
        print("Los animales fueron ordenadas alfabeticamente.")

    def invertir_orden(self):
        """Invierte el orden actual de los animales."""
        self.animal.reverse()
        print("El orden de los animal fue invertido.")

    def mostrar_animal(self):
        """Muestra todas los animales de la lista."""
        print("Lista actual del animal:", self.animal)


# ------------------ MENU CRUD ------------------
def menu():
    """Muestra el menu principal del programa."""
    base = BaseDatosAnimal()

    while True:
        print("\n--- MENU animal ---")
        print("1. Agregar animal")
        print("2. Agregar variaos animales")
        print("3. Insertar animal en posicion")
        print("4. Eliminar animal por nombre")
        print("5. Eliminar animal por posicion")
        print("6. Buscar posicion del animal")
        print("7. Contar cuantas veces aparece el animal")
        print("8. Ordenar animales")
        print("9. Invertir orden")
        print("10. Mostrar todas los animales")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre animal :")
            base.crear_animales(nombre)

        elif opcion == "2":
            nombres = input("ingrese el nombre de los animales separados por , :")
            lista = [n.strip() for n in nombres.split(",")]
            base.agregar_elementos_al_final(lista)

        elif opcion == "3":
            nombre = input("ingrese el nombre del animal:")
            pos = int(input("Posicion donde insertarlo: "))
            base.insertar_animales(pos, nombre)

        elif opcion == "4":
            nombre = input("Ingrese el nombre de animal a eliminar: ")
            base.eliminar_animales(nombre)

        elif opcion == "5":
            pos = int(input("Ingrese la posicion a eliminar: "))
            base.eliminar_por_posicion(pos)

        elif opcion == "6":
            nombre = input("Ingrese el animal a buscar: ")
            base.obtener_posicion(nombre)

        elif opcion == "7":
            nombre = input("Ingrese el animal a contar:")
            base.contar_animales(nombre)

        elif opcion == "8":
            base.ordenar_animal()

        elif opcion == "9":
            base.invertir_orden()

        elif opcion == "10":
            base.mostrar_animal()

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida, por favor intente de nuevo.")


# Ejecutar el menu solo si se ejecuta directamente
if __name__ == "__main__":
    menu()
