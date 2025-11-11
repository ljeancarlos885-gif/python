"""importar la clase padre Botella"""
from modelo_botella_padre import Botella

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


