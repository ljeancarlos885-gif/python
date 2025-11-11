"""importar la clase padre animal"""
from modelo_animal_padre import Animal

#crear la clase caballo
class Caballo(Animal):
    """se crea la clase caballo"""
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_tierra, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_tierra = tipo_tierra
        self.raza = raza
        self.velocidad = velocidad

    def moverse(self):
        """Metodo como se desplaza el caballo"""
        info = super().moverse()
        texto = info + "galopando con rapidez alcanzandodo velocidades km/h"
        return texto

    def comunicacion(self):
        """Metodo de como ed la comunicacion de los caballos"""
        texto = "se comunica relinchando y realizan movimientos con su cuerpo"
        return texto

    def adaptacion(self):
        """Metodo adaptacion del caballo"""
        texto = "tiene patas fuertes y cascos duros adaptados para correr largas distacias"
        return texto

    def alimentarse(self):
        """Metodo como es su alimentacion"""
        texto = "se alimenta principalmente de pasto y heno"
        return texto

    def imprimir_datos(self):
        """Metodo para imprimir datos"""
         # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"tipo_tierra: {self.tipo_tierra}")
        print(f"raza: {self.raza}")
        print(f"velocidad: {self.velocidad}\n")

         # Crear la instancia de la clase Caballo
caballo1 = Caballo(
    nombre = "Sultan",
    edad = "2 años",
    habitat = "Pradera",
    dieta = "Herbivoro",
    tamaño = "Grande",
    color = "Marron",
    tipo_tierra = "Llanura",
    raza = "pura sangre",
    velocidad = "88 km/h"
)

# Imprimir los datos del caballo
print("Datos del Caballo:")
caballo1.imprimir_datos()

#metodos heredados y complementados
print(caballo1.moverse())
print(caballo1.comunicacion())
print(caballo1.reproduccion())
print(caballo1.alimentarse())
print(caballo1.adaptacion())
print(caballo1.instintos())
print(caballo1.descanso())
print(caballo1.sueño())
print(caballo1.interaccion_social())
