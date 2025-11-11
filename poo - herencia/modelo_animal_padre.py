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
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Habitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}")
