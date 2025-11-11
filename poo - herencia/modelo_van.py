"""importar la clase padre animal"""
from modelo_vehiculo_padre import Vehiculo

# Clase hija van
class Van(Vehiculo):
    """clase hija vehiculo van"""
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible,tipo_ruedas, tipo, velocidad):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.tipo_ruedas = tipo_ruedas
        self.tipo = tipo
        self.velocidad = velocidad

    def arrancar(self):
        """Metodo para arrancar el vehiculo van"""
        info = super().arrancar()
        texto = info + "con la llave hasta la posicion encendido"
        return texto

    def apagar(self):
        """Metodo para apagar el vehiculo van"""
        info = super().apagar()
        texto = info + "con la llave hasta la posicion apagado"
        return texto

    def tipo_seguridad(self):
        """Metodo tipo seguridad del vehiculo van"""
        info = super().tipo_seguridad()
        texto = info + "activa y pasiva"
        return texto

    def imprimir_datos(self):
        """Metodo para imoprimir datos"""

        # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"tipo_ruedas {self.tipo_ruedas}")
        print(f"tipo {self.tipo}")
        print(f"velocidad: {self.velocidad}km/h\n")

        # crear instancia de la clase Van
van1 = Van(
modelo = "Chevrolet N300",
color = "Blanco",
motor = "1.5L",
numero_puertas = 4,
capacidad_pasajeros = 8,
tipo_combustible = "Gasolina",
tipo_ruedas = "comercial",
velocidad = 90,
tipo = "Buseta"
)

# Imprimir los datos de la van
print("\nDatos de la van")
van1.imprimir_datos()

print(van1.arrancar())
print(van1.apagar())
print(van1.acelerar_frenar())
print(van1.sistema_direccion())
print(van1.climatizacion())
print(van1.tipo_seguridad())
print(van1.luces())
print(van1.sistema_ventana())
print(van1.sistema_espejos())
