"""importar la clase padre animal"""
from modelo_animal_padre import Animal

# clase hija pato
class Pato(Animal):
    """se crea la clase pato"""

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua, tipo_pico, envergadura_alas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua
        self.tipo_pico = tipo_pico
        self.envergadura_alas = envergadura_alas

    def moverse(self):
        """caminando, nadando y volando"""
        info = super().moverse()
        texto = info + "caminando, nadando y volando segun el entorno"
        return texto

    def comunicacion(self):
        """los patos se comunican con sonidos y gestos"""
        texto = "se comunican mediante graznidos y movimientos del cuerpo"
        return texto

    def adaptacion(self):
        """los patos estan adaptados a ambientes acuaticos"""
        texto = "posee plumas impermeables y patas palmeadas para nadar facilmente"
        return texto

    def alimentarse(self):
        """los patos se alimentan de semillas, insectos y plantas acuaticas"""
        texto = "se alimenta de plantas acuaticas, insectos y pequeños crustaceos"
        return texto

    def imprimir_datos(self):
        """metodo para imprimir datos del pato"""
         # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"Tipo de agua: {self.tipo_agua}")
        print(f"Tipo de pico: {self.tipo_pico}")
        print(f"Envergadura de alas: {self.envergadura_alas} cm\n")

        # Crear instancia de la clase Pato
pato1 = Pato(
    nombre="Lucas",
    edad="1 año",
    habitat="lago",
    dieta="omnivoro",
    tamaño="mediano",
    color="blanco",
    tipo_agua="dulce",
    tipo_pico="ancho y plano",
    envergadura_alas="80"
)
#Imprimir los datos del pez
print("\nDatos del pato:")
pato1.imprimir_datos()

#metodos heredados y complementados
print(pato1.moverse())
print(pato1.comunicacion())
print(pato1.reproduccion())
print(pato1.alimentarse())
print(pato1.adaptacion())
print(pato1.instintos())
print(pato1.descanso())
print(pato1.sueño())
print(pato1.interaccion_social())


