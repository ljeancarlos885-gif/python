"""importar la clase padre animal"""
from modelo_animal_padre import Animal

 # clase hija pez
class Pez(Animal):
    """se crea la clase pez"""

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua, velocidad_nado, profundidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua
        self.velocidad_nado = velocidad_nado
        self.profundidad = profundidad

    def moverse(self):
        """los peces se mueven nadando"""
        info = super().moverse()
        texto = info + "nadando gracias a sus aletas y cola"
        return texto

    def comunicacion(self):
        """los peces usan senales visuales o quimicas"""
        texto = "se comunican mediante movimientos y senales quimicas en el agua"
        return texto

    def adaptacion(self):
        """los peces estan adaptados a la vida acuatica"""
        texto = "posee branquias para respirar bajo el agua y escamas para proteger su cuerpo"
        return texto

    def alimentarse(self):
        """los peces se alimentan segun su tipo"""
        texto = "se alimenta de plancton, algas o peces mas pequenos segun su especie"
        return texto

    def imprimir_datos(self):
        """metodo para imprimir datos del pez"""
         # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"Tipo de agua: {self.tipo_agua}")
        print(f"Velocidad de nado: {self.velocidad_nado} km/h")
        print(f"Profundidad maxima: {self.profundidad} metros\n")

        #crear la instancia dela clase Pez
pez1 = Pez(
    nombre = "Nemo",
    edad = "5 meses",
    habitat = "rio",
    dieta = "Omnivoro",
    tamaño = "pequeño",
    color = "gris",
    tipo_agua = "Dulce",
    velocidad_nado = "10 km/h",
    profundidad = "40 metros"
)

#Imprimir los datos del pez
print("\nDatos del pez:")
pez1.imprimir_datos()


#metodos heredados y complementados
print(pez1.comunicacion())
print(pez1.reproduccion())
print(pez1.alimentarse())
print(pez1.adaptacion())
print(pez1.instintos())
print(pez1.descanso())
print(pez1.sueño())
print(pez1.interaccion_social())
