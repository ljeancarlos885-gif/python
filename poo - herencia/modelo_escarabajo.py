"""importar la clase padre animal"""
from modelo_animal_padre import Animal

# clase hija escarabajo
class Escarabajo(Animal):
    """se crea la clase escarabajo"""
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_suelo, tipo_ala, velocidad_vuelo):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_suelo = tipo_suelo
        self.tipo_ala = tipo_ala
        self.velocidad_vuelo = velocidad_vuelo

    def moverse(self):
        """caminando o volando"""
        info = super().moverse()
        texto = info + "caminando con sus patas o volando con sus alas duras"
        return texto

    def comunicacion(self):
        """se comunican mediante vibraciones o feromonas"""
        texto = "se comunican usando vibraciones, sonidos o feromonas quimicas"
        return texto

    def adaptacion(self):
        """estan adaptados a diferentes tipos de suelo"""
        texto = "tiene un caparazon duro que protege su cuerpo y patas fuertes para excavar"
        return texto

    def alimentarse(self):
        """se alimentan segun su especie"""
        texto = "puede alimentarse de plantas, madera o restos organicos segun su especie"
        return texto

    def imprimir_datos(self):
        """metodo para imprimir datos del escarabajo"""
         # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"Tipo de suelo: {self.tipo_suelo}")
        print(f"Tipo de ala: {self.tipo_ala}")
        print(f"Velocidad de vuelo: {self.velocidad_vuelo} km/h\n")

        # Crear la instancia de la Escarabajo
escarabajo1 = Escarabajo(
    nombre="Hercules",
    edad="2 años",
    habitat="bosque tropical",
    dieta="omnivoro",
    tamaño="mediano",
    color="negro",
    tipo_suelo="humedo",
    tipo_ala="dura",
    velocidad_vuelo="15"
)
#Imprimir los datos del pez
print("\nDatos del escarabajo:")
escarabajo1.imprimir_datos()

#metodos heredados y complementados
print(escarabajo1.moverse())
print(escarabajo1.comunicacion())
print(escarabajo1.reproduccion())
print(escarabajo1.alimentarse())
print(escarabajo1.adaptacion())
print(escarabajo1.instintos())
print(escarabajo1.descanso())
print(escarabajo1.sueño())
print(escarabajo1.interaccion_social())

