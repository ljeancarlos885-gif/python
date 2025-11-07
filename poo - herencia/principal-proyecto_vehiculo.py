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
        texto = "El vehículo puede girar en diferentes direcciones con el volante "
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
        texto = "El vehículo posee un par de espejos que le permiten" \
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
        """Método para arrancar el vehículo volqueta"""
        info = super().arrancar()
        texto = info + " con la llave hasta la posición encendido"
        return texto

    def apagar(self):
        """Método para apagar el vehículo volqueta"""
        info = super().apagar()
        texto = info + " con la llave hasta la posición apagado"
        return texto

    def tipo_seguridad(self):
        """Método tipo seguridad del vehículo volqueta"""
        info = super().tipo_seguridad()
        texto = info + " activa y pasiva"
        return texto

    def imprimir_datos(self):
        """Método para imprimir datos"""
        super().imprimir_datos()
        print(f"tipo_ruedas: {self.tipo_ruedas}")
        print(f"tipo: {self.tipo}")
        print(f"velocidad: {self.velocidad} km/h\n")

# **********Codigo principal***********
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


