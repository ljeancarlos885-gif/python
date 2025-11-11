"""clase padre animal"""
class Animal:
    """crear la clase base Animal"""
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        """se mueven en su entorno"""
        texto = "pueden desplazarse en cualquier direccion "
        return texto

    def reproduccion(self):
        """pueden reproducirse"""
        texto = "se reproducen segun su especie en (ovipara o vivipara)"
        return texto

    def instintos(self):
        """cada animal obtine diferentes instintos"""
        texto = "actuan por instinto cuando persiben el peligro o comida"
        return texto

    def descanso(self):
        """tienden a tomar su siesta cortas"""
        texto = "descansan para recuperar energias"
        return texto

    def sueño(self):
        """duermen para mantenerse sanos recuperara energias"""
        texto = "duermen de forma regular para mantenerse saludables"
        return texto

    def interaccion_social(self):
        """interactuan con su especie"""
        texto = "pueden interactuar con otros individuos de su especie"
        return texto

    def imprimir_datos(self):
        """Metodo para imprimir datos"""
        print(f"nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Habitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}")

#clase hija caballo
class Caballo(Animal):
    """se crea la clase caballo"""
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_tierra, raza, velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_tierra = tipo_tierra
        self.raza = raza
        self.velocidad = velocidad

    def moverse(self):
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
         # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"tipo_tierra: {self.tipo_tierra}")
        print(f"raza: {self.raza}")
        print(f"velocidad: {self.velocidad}\n")

        # clase hija cocodrilo
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

#************Coigo principal************
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
print("\nDatos del Caballo:")
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
