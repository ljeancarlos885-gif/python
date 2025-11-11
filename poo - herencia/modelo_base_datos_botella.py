"""crear la base de datos botella"""
class BaseDatosBotella:
    """Simula una base de datos de botellas usando una lista."""

    def __init__(self):
        """Inicializa la lista de botellas."""
        self.botellas = []

    def crear_botella(self, nombre_botella):
        """Agrega una nueva botella a la lista."""
        self.botellas.append(nombre_botella)
        print(f'Botella "{nombre_botella}" agregada exitosamente.')

    def agregar_elementos_al_final(self, lista_botellas):
        """Agrega varias botellas al final de la lista."""
        self.botellas.extend(lista_botellas)
        print(f'Se agregaron las botellas: {lista_botellas}')

    def insertar_botella(self, posicion, nombre_botella):
        """Inserta una botella en una posicion especifica."""
        self.botellas.insert(posicion, nombre_botella)
        print(f'Botella "{nombre_botella}" insertada en la posicion {posicion}.')

    def eliminar_botella(self, nombre):
        """Elimina una botella por su nombre."""
        if nombre in self.botellas:
            self.botellas.remove(nombre)
            print(f'Botella "{nombre}" eliminada correctamente.')
        else:
            print(f'No se encontro la botella "{nombre}".')

    def eliminar_por_posicion(self, posicion):
        """Elimina una botella segun su posicion."""
        try:
            botella_eliminada = self.botellas.pop(posicion)
            print(f'Se elimino la botella en la posicion {posicion}: "{botella_eliminada}".')
        except IndexError:
            print('Error: la posicion ingresada no existe en la lista.')

    def obtener_posicion(self, nombre):
        """Muestra la posicion de una botella en la lista."""
        if nombre in self.botellas:
            posicion = self.botellas.index(nombre)
            print(f'La botella "{nombre}" se encuentra en la posicion {posicion}.')
        else:
            print(f'No se encontro la botella "{nombre}".')

    def contar_botella(self, nombre):
        """Cuenta cuantas veces aparece una botella."""
        cantidad = self.botellas.count(nombre)
        print(f'La botella "{nombre}" aparece {cantidad} vez/veces en la lista.')

    def ordenar_botellas(self):
        """Ordena las botellas alfabeticamente."""
        self.botellas.sort()
        print('Las botellas fueron ordenadas alfabeticamente.')

    def invertir_orden(self):
        """Invierte el orden actual de las botellas."""
        self.botellas.reverse()
        print('El orden de las botellas fue invertido.')

    def mostrar_botellas(self):
        """Muestra todas las botellas de la lista."""
        print("Lista actual de botellas:", self.botellas)


# ------------------ MENU CRUD ------------------
def menu():
    """Muestra el menu principal del programa."""
    base = BaseDatosBotella()

    while True:
        print("\n--- MENU BOTELLAS ---")
        print("1. Agregar botella")
        print("2. Agregar varias botellas")
        print("3. Insertar botella en posicion")
        print("4. Eliminar botella por nombre")
        print("5. Eliminar botella por posicion")
        print("6. Buscar posicion de una botella")
        print("7. Contar cuantas veces aparece una botella")
        print("8. Ordenar botellas")
        print("9. Invertir orden")
        print("10. Mostrar todas las botellas")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese que tipo de botella (plastico o vidrio):")
            base.crear_botella(nombre)

        elif opcion == "2":
            nombres = input("ingrese varios tipos de botella separadas por , : ")
            lista = [n.strip() for n in nombres.split(",")]
            base.agregar_elementos_al_final(lista)

        elif opcion == "3":
            nombre = input(" tipo de botella: ")
            pos = int(input("Posicion donde insertarla: "))
            base.insertar_botella(pos, nombre)

        elif opcion == "4":
            nombre = input("Ingrese el tipo de botella a eliminar: ")
            base.eliminar_botella(nombre)

        elif opcion == "5":
            pos = int(input("Ingrese la posicion a eliminar: "))
            base.eliminar_por_posicion(pos)

        elif opcion == "6":
            nombre = input("Ingrese el tipo de botella a buscar: ")
            base.obtener_posicion(nombre)

        elif opcion == "7":
            nombre = input("Ingrese el tipo de botella a contar: ")
            base.contar_botella(nombre)

        elif opcion == "8":
            base.ordenar_botellas()

        elif opcion == "9":
            base.invertir_orden()

        elif opcion == "10":
            base.mostrar_botellas()

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida, por favor intente de nuevo.")


# Ejecutar el menu solo si se ejecuta directamente
if __name__ == "__main__":
    menu()
