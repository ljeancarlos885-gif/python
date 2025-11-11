"""importar la clase padre animal"""
from modelo_animal_padre import Animal

class Cocodrilo(Animal):
    """se crea la clase cocodrilo"""

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua, longitud, fuerza_mandibula):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua
        self.longitud = longitud
        self.fuerza_mandibula = fuerza_mandibula

    def moverse(self):
        """los cocodrilos se mueven caminando o nadando"""
        info = super().moverse()
        texto = info + "arrastrandose en tierra y nadando con fuerza en el agua"
        return texto

    def comunicacion(self):
        """los cocodrilos se comunican de varias maneras"""
        texto = "se comunican con rugidos, gruñidos y movimientos del cuerpo"
        return texto

    def adaptacion(self):
        """los cocodrilos estan adaptados a su entorno"""
        texto = "tiene una piel gruesa y resistente al agua, y pueden " \
        "estar mucho tiempo bajo el agua"
        return texto

    def alimentarse(self):
        """los cocodrilos son carnivoros"""
        texto = "se alimenta de peces, aves y otros animales que atrapan en el agua o cerca de ella"
        return texto

    def imprimir_datos(self):
        """metodo para imprimir datos del cocodrilo"""
        # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"Tipo de agua: {self.tipo_agua}")
        print(f"Longitud: {self.longitud} metros")
        print(f"Fuerza de mandibula: {self.fuerza_mandibula}\n")

# Crear instancia de la clase Cocodrilo
cocodrilo1 = Cocodrilo(
    nombre = "Rex",
    edad = "6 años",
    habitat = "Pantano",
    dieta = "Carnivoro",
    tamaño = "Grande",
    color = "Verde oscuro",
    tipo_agua = "Dulce",
    longitud = "5",
    fuerza_mandibula = "3700 newton"
)

# Imprimir los datos del cocodrilo
print("\nDatos del Cocodrilo:")
cocodrilo1.imprimir_datos()

#metodos heredados y complementados
print(cocodrilo1.moverse())
print(cocodrilo1.comunicacion())
print(cocodrilo1.reproduccion())
print(cocodrilo1.alimentarse())
print(cocodrilo1.adaptacion())
print(cocodrilo1.instintos())
print(cocodrilo1.descanso())
print(cocodrilo1.sueño())
print(cocodrilo1.interaccion_social())


