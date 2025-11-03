"""Clase Botella"""
class Botella:
    """Clase base para una botella"""

    def __init__(self, material, capacidad, forma):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma

    def contener_liquidos(self):
        """Método para contener líquidos"""
        return "Contiene solo líquido"

    def cierre_hermetico(self):
        """Método para el cierre hermético"""
        return "Se cierra al vacío"

    def imprimir_datos(self):
        """Método para imprimir los datos básicos de la botella"""
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Forma: {self.forma}")


class BotellaPlastica(Botella):
    """Clase hija para una botella plástica"""

    def __init__(self, material, capacidad, forma, diseño, grabados, tapa):
        super().__init__(material, capacidad, forma)
        self.diseño = diseño
        self.grabados = grabados
        self.tapa = tapa

    def facilitar_el_vertido(self):
        """Método para facilitar el vertido del líquido"""
        return "Facilita el vertido del líquido gracias a su boquilla."

    def transporte(self):
        """Método para transportar la botella"""
        return "La botella es fácil de transportar debido a su tamaño compacto."

    def manejo(self):
        """Método para el manejo de la botella"""
        return "La botella tiene un diseño ergonómico para un manejo cómodo."

    def compatibilidad_con_bebidas_calientes_frias(self):
        """Método que indica si es compatible con bebidas calientes o frías"""
        return "Compatible con bebidas frías y calientes dentro de un rango adecuado de temperatura."

    def reutilizacion(self):
        """Método para indicar si la botella es reutilizable"""
        return "La botella es reutilizable y amigable con el medio ambiente."

    def transparencia(self):
        """Método que muestra si la botella es transparente o no"""
        return "La botella tiene un diseño transparente."

    def imprimir_datos(self):
        """Método sobrescrito para imprimir los datos específicos de la botella plástica"""
        super().imprimir_datos()  # Llamar al método de la clase base
        print(f"Diseño: {self.diseño}")
        print(f"Grabados: {self.grabados}")
        print(f"Tapa: {self.tapa}")


class BotellaVidrio(Botella):
    """Clase hija para una botella de vidrio"""

    def __init__(self, material, capacidad, forma, diseño, grabados, tapa, grosor_vidrio):
        super().__init__(material, capacidad, forma)
        self.diseño = diseño
        self.grabados = grabados
        self.tapa = tapa
        self.grosor_vidrio = grosor_vidrio

    def facilitar_el_vertido(self):
        """Método para facilitar el vertido del líquido"""
        return "Facilita el vertido del líquido gracias a su cuello estrecho."

    def transporte(self):
        """Método para transportar la botella"""
        return "La botella de vidrio es fácil de transportar, pero es más delicada."

    def manejo(self):
        """Método para el manejo de la botella"""
        return "La botella de vidrio tiene un diseño elegante y sólido para un manejo seguro."

    def compatibilidad_con_bebidas_calientes_frias(self):
        """Método que indica si es compatible con bebidas calientes o frías"""
        return "Compatible con bebidas frías y calientes dentro de un rango adecuado de temperatura."

    def reutilizacion(self):
        """Método para indicar si la botella es reutilizable"""
        return "La botella de vidrio es reutilizable y reciclable."

    def transparencia(self):
        """Método que muestra si la botella es transparente o no"""
        return "La botella de vidrio es completamente transparente."

    def imprimir_datos(self):
        """Método sobrescrito para imprimir los datos específicos de la botella de vidrio"""
        super().imprimir_datos()  # Llamar al método de la clase base
        print(f"Diseño: {self.diseño}")
        print(f"Grabados: {self.grabados}")
        print(f"Tapa: {self.tapa}")
        print(f"Grosor del Vidrio: {self.grosor_vidrio} mm")




# Crear una instancia de BotellaPlastica
botella_plastica = BotellaPlastica("Plástico", 500, "Cilíndrica", "Moderno", "Logo de la marca", "Tapa Hermética")

# Imprimir los datos de la botella plástica
botella_plastica.imprimir_datos()

# Llamar a algunos métodos
print(botella_plastica.contener_liquidos())
print(botella_plastica.facilitar_el_vertido())
print(botella_plastica.transporte())
print(botella_plastica.manejo())
print(botella_plastica.compatibilidad_con_bebidas_calientes_frias())
print(botella_plastica.reutilizacion())
print(botella_plastica.transparencia())

# Crear una instancia de BotellaVidrio
botella_vidrio = BotellaVidrio(
    material="Vidrio",
    capacidad=750,
    forma="Cilíndrica",
    diseño="Clásico",
    grabados="Nombre de la marca",
    tapa="Tapa de rosca",
    grosor_vidrio=5
)

# Imprimir los datos de la botella de vidrio
botella_vidrio.imprimir_datos()


print(botella_vidrio.contener_liquidos())
print(botella_vidrio.facilitar_el_vertido())
print(botella_vidrio.transporte())
print(botella_vidrio.manejo())
print(botella_vidrio.compatibilidad_con_bebidas_calientes_frias())
print(botella_vidrio.reutilizacion())
print(botella_vidrio.transparencia())  