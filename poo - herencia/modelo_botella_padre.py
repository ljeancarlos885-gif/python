"""Clase Botella"""
class Botella:
    """Clase base para una botella"""

    def __init__(self, material, capacidad, forma):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma

    def contener_liquidos(self):
        """metodo para contener liquidos"""
        texto = "Contiene solo liquidos"
        return texto

    def cierre_hermetico(self):
        """metodo para el cierre hermetico"""
        texto =  "Se cierra al vacio"
        return texto

    def imprimir_datos(self):
        """metodo para imprimir los datos basicos de la botella"""
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad}ml")
        print(f"Forma: {self.forma}")
