"""Clase Botella"""
class Botella:
    """Clase base para una botella"""

    def __init__(self, material, capacidad, forma):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma

    def contener_liquidos(self):
        """metodo para contener liquidos"""
        texto = "Contiene solo liquido"
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

    # Crear la clase botella plastica
class BotellaPlastica(Botella):
    """Clase hija para una botella plastica"""

    def __init__(self, material, capacidad, forma, diseño, grabados, tapa):
        super().__init__(material, capacidad, forma)
        self.diseño = diseño
        self.grabados = grabados
        self.tapa = tapa

    def facilitar_el_vertido(self):
        """metodo para facilitar el vertido del liquido"""
        texto = "Facilita el vertido del liquido gracias a su boquilla."
        return texto

    def transporte(self):
        """metodo para transportar la botella"""
        texto = "La botella es facil de transportar debido a su tamaño compacto."
        return texto

    def manejo(self):
        """metodo para el manejo de la botella"""
        texto = "La botella tiene un diseño ergonomico para un manejo comodo."
        return texto

    def compatibilidad_con_bebidas_calientes_frias(self):
        """metodo que indica si es compatible con bebidas calientes o frias"""
        texto = "Compatible con bebidas frias y calientes dentro de un rango adecuado de temperatura."
        return texto

    def reutilizacion(self):
        """metodo para indicar si la botella es reutilizable"""
        texto =  "La botella es reutilizable y amigable con el medio ambiente."
        return texto

    def transparencia(self):
        """metodo que muestra si la botella es transparente o no"""
        texto = "La botella tiene un diseño transparente."
        return texto

    def imprimir_datos(self):
        """metodo sobrescrito para imprimir los datos especificos de la botella plastica"""
        # Llamar al metodo de la clase padre
        super().imprimir_datos()

        print(f"Diseño: {self.diseño}")
        print(f"Grabados: {self.grabados}")
        print(f"Tapa: {self.tapa}\n")


class BotellaVidrio(Botella):
    """Clase hija para una botella de vidrio"""

    def __init__(self, material, capacidad, forma, diseño, grabados, tapa, grosor_vidrio):
        super().__init__(material, capacidad, forma)
        self.diseño = diseño
        self.grabados = grabados
        self.tapa = tapa
        self.grosor_vidrio = grosor_vidrio

    def facilitar_el_vertido(self):
        """metodo para facilitar el vertido del liquido"""
        texto = "Facilita el vertido del liquido gracias a su cuello estrecho."
        return texto

    def transporte(self):
        """metodo para transportar la botella"""
        texto = "La botella de vidrio es facil de transportar, pero es mas delicada."
        return texto

    def manejo(self):
        """metodo para el manejo de la botella"""
        texto = "La botella de vidrio tiene un diseño elegante y solido para un manejo seguro."
        return texto

    def compatibilidad_con_bebidas_calientes_frias(self):
        """metodo que indica si es compatible con bebidas calientes o frias"""
        texto = "Compatible con bebidas frias y calientes dentro de un rango adecuado de temperatura."
        return texto
    def reutilizacion(self):
        """metodo para indicar si la botella es reutilizable"""
        texto = "La botella de vidrio es reutilizable y reciclable."
        return texto
    def transparencia(self):
        """metodo que muestra si la botella es transparente o no"""
        texto = "La botella de vidrio es completamente transparente."
        return texto
    def imprimir_datos(self):
        """metodo para imprimir los datos especificos de la botella de vidrio"""

         # Llamar al metodo de la clase padre
        super().imprimir_datos()

        print(f"Diseño: {self.diseño}")
        print(f"Grabados: {self.grabados}")
        print(f"Tapa: {self.tapa}")
        print(f"Grosor del Vidrio: {self.grosor_vidrio}mm\n")

# Crear una instancia de BotellaPlastica
botella_plastica = BotellaPlastica(
    material ="Plastico",
    capacidad = 500,
    forma = "Cilindrica",
    diseño = "Moderno",
    tapa = "Tapa Hermetica",
    grabados = "Logo de la marca"
)

# Imprimir los datos de la botella plastica
print("\nDatos botella plastica")
botella_plastica.imprimir_datos()

# Llamar a algunos metodos
print(botella_plastica.contener_liquidos())
print(botella_plastica.facilitar_el_vertido())
print(botella_plastica.cierre_hermetico())
print(botella_plastica.transporte())
print(botella_plastica.manejo())
print(botella_plastica.compatibilidad_con_bebidas_calientes_frias())
print(botella_plastica.reutilizacion())
print(botella_plastica.transparencia())

# Crear una instancia de BotellaVidrio
botella_vidrio = BotellaVidrio(
    material = "Vidrio",
    capacidad = 750,
    forma = "Cilindrica",
    diseño = "Clasico",
    grabados ="Nombre de la marca",
    tapa = "Tapa de rosca",
    grosor_vidrio = 5
)

# Imprimir los datos de la botella de vidrio
print("\nDatos botella de vidrio")
botella_vidrio.imprimir_datos()


print(botella_vidrio.contener_liquidos())
print(botella_vidrio.facilitar_el_vertido())
print(botella_vidrio.transporte())
print(botella_vidrio.cierre_hermetico())
print(botella_vidrio.manejo())
print(botella_vidrio.compatibilidad_con_bebidas_calientes_frias())
print(botella_vidrio.reutilizacion())
print(botella_vidrio.transparencia())