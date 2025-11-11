"""clase padre """
class Vehiculo:
    """clase base """
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def arrancar(self):
        """Metodo para que el vehiculo arranque """
        texto = "Pueden arranca "
        return texto

    def apagar(self):
        """Metodo para que el vehiculo se apague"""
        texto = "El vehiculo se apaga"
        return texto

    def acelerar_frenar(self):
        """Metodo para que el vehiculo acelere o frene"""
        texto = "El vehiculo acelera y frenar por mesdio de pedales"
        return texto

    def sistema_direccion(self):
        """Metodo para que el vehiculo se mueva en diferentes direcciones"""
        texto = "El vehiculo puede girar en diferentes direcciones con el volante "
        return texto

    def climatizacion(self):
        """Metodo para regular la temperatura"""
        texto = "El vehiculo puede enciender la climatizacion para regular la temperatura"
        return texto

    def tipo_seguridad(self):
        """Metodo de seguridad del vehiculo"""
        texto = "El vehilo tiene seguridad"
        return texto

    def luces(self):
        """Metodo luces del vehiculo"""
        texto = "El vehiculo posee luces que sirven al conductor para ver en la oscuridad"
        return texto

    def sistema_ventana(self):
        "Metodo sistema de ventanas del vehiculo"
        texto = "El vehiclo posee un sistema de ventanas para abrir y cerrar el cristal"
        return texto

    def sistema_espejos(self):
        "Metodo espejos del vehiculo"
        texto = "El vehiculo posee un par de espejos que le permiten" \
        "al conductor percibir el entorno"
        return texto

    def imprimir_datos(self):
        """Metodo para imprimir datos"""
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor} cilidros")
        print(f"Numero_puertas: {self.numero_puertas} puertas")
        print(f"Capacidad_pasajeros: {self.capacidad_pasajeros} pasajeros")
        print(f"Tipo_combustible: {self.tipo_combustible}")
