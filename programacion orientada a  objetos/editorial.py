"""clase editorial"""
class Editorial:
    """Esta clase editorial es la en cargada de publicar libros"""

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        """este metodo lo usamos para vender el editorial"""
        print("vendiendo un editorial")


        # instancia de la clase Editorial
# Crear una instancia de la clase Editorial
editorial1 = Editorial("editorial omega", "Calle 8 #12-34, Ciudad Cucuta","321-456-7890")

# Uso del metodo vender()
editorial1.vender()
