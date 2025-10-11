"""clase producto"""
class Producto:
    """Esta clase almacena información relevante sobre un producto, como su nombre,
    precio y descripción."""

    def __init__(self, precio, titulo, autor, editorial, año_de_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_de_edicion = año_de_edicion
        self.preferencias = preferencias

    def vender(self):
        """metodo que muestra las ventas del producto."""
        print("realizando ventas de productos")

    def comprar(self):
        """metodo usado para la compra de productos."""
        print("realizando compra de productos")

    def ver_catalogo(self):
        """metodo usado para ver el catálogo"""
        print("observando un catalogo")

        # Instancia de la clase producto
    #creo la instancia
producto1 = Producto("40000", "python primeros pasos", "juan perez",
                     "editorial multitec", "2027-10-18", "programacion")

# Uso de métodos
producto1.ver_catalogo()
producto1.vender()
producto1.comprar()
