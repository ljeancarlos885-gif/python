"""importar la clase padre animal"""
from modelo_vehiculo_padre import Vehiculo

# Clase hija volqueta
class Volqueta(Vehiculo):
    """Clase hija de Vehiculo: Volqueta"""

    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros,
                 tipo_combustible, tipo_ruedas, tipo, velocidad, capacidad_carga):
        super().__init__(modelo, color, motor, numero_puertas,
                         capacidad_pasajeros, tipo_combustible)
        self.tipo_ruedas = tipo_ruedas
        self.tipo = tipo
        self.velocidad = velocidad
        self.capacidad_carga = capacidad_carga  # typo fixed

    def arrancar(self):
        """Metodo para arrancar el vehiculo volqueta"""
        info = super().arrancar()
        texto = info + " con la llave hasta la posicion encendido"
        return texto

    def apagar(self):
        """Metodo para apagar el vehiculo volqueta"""
        info = super().apagar()
        texto = info + " con la llave hasta la posicion apagado"
        return texto

    def tipo_seguridad(self):
        """Metodo tipo seguridad del vehiculo volqueta"""
        info = super().tipo_seguridad()
        texto = info + " activa y pasiva"
        return texto

    def imprimir_datos(self):
        """Metodo para imprimir datos"""
        super().imprimir_datos()
        print(f"tipo_ruedas: {self.tipo_ruedas}")
        print(f"tipo: {self.tipo}")
        print(f"velocidad: {self.velocidad} km/h\n")

# Crear instancia de la clase Volqueta
volqueta1 = Volqueta(
    modelo = "volvo",
    color = "Blanco",
    motor = " 6 cilindros en linea",
    numero_puertas = 2,
    capacidad_pasajeros = 1,
    tipo_combustible = "diesel",
    tipo_ruedas = "radiales y diagonales. ",
    velocidad = 50,
    tipo = "camion de volteo",
    capacidad_carga = 5
)

# Imprimir los datos de la volqueta
print("\nDatos de la volqueta")
volqueta1.imprimir_datos()

print(volqueta1.arrancar())
print(volqueta1.apagar())
print(volqueta1.acelerar_frenar())
print(volqueta1.sistema_direccion())
print(volqueta1.climatizacion())
print(volqueta1.tipo_seguridad())
print(volqueta1.luces())
print(volqueta1.sistema_ventana())
print(volqueta1.sistema_espejos())
