"""importar la clase padre animal"""
from modelo_vehiculo_padre import Vehiculo

# Clase hija deportivo
class Deportivo(Vehiculo):

    """se crea la clase hija  deportivo"""
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible, tipo_ruedas, suspension, tipo, velocidad):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.tipo_ruedas = tipo_ruedas
        self.suspension = suspension
        self.tipo = tipo
        self.velocidad = velocidad

    def arrancar(self):
        """Metodo para arrancar el vehiculo deportivo"""
        info = super().arrancar()
        texto = info + "con solo con precionar un boton arranca"
        return texto

    def apagar(self):
        """Metodo para apagar el vehiculo deportivo"""
        info = super().arrancar()
        texto = info + "Con solo presiona un boton"
        return texto

    def tipo_seguridad(self):
        """Metodo tipo seguridad del vehiculo deportivo"""
        info = super().tipo_seguridad()
        texto = info + "activa y pasiva"
        return texto

    def sistema_direccion(self):
        info = super().sistema_direccion()
        texto = info + "ademas poseen un sistema de direccion asistida "
        return texto

    def imprimir_datos(self):
        """Metodo para imoprimir datos"""

        # llamamos al metodo imprimir de la clase padre
        super().imprimir_datos()

        print(f"tipo_ruedas {self.tipo_ruedas} de alto rendimiento")
        print(f"suspension {self.suspension}")
        print(f"tipo {self.tipo}")
        print(f"velocidad: {self.velocidad} km/h\n")

           # crear instancia de la clase deportivo
deportivo1 = Deportivo(
    modelo = "BMW",
    color = "Negro",
    motor = 6 ,
    numero_puertas = 2,
    capacidad_pasajeros = 1,
    tipo_combustible = "Gasolina",
    tipo_ruedas = "Deportivas",
    suspension = "Adaptativa",
    tipo = "Coche",
    velocidad = 250
)


# Imprimir los datos del coche deportivo
print("\nDatos del deportivo")
deportivo1.imprimir_datos()

print(deportivo1.arrancar())
print(deportivo1.apagar())
print(deportivo1.acelerar_frenar())
print(deportivo1.sistema_direccion())
print(deportivo1.climatizacion())
print(deportivo1.tipo_seguridad())
print(deportivo1.luces())
print(deportivo1.sistema_ventana())
print(deportivo1.sistema_espejos())
