
"""clase articulo de segugunda mano"""

class ArticuloDeSegundaMano:

    """ Esta clase puede un articulo de segunda mano para la venta
    incluyendo detalles como la  descripcion."""

    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

         # ** instancia   de la clase articulo de segugunda mano **

articulo1 = ArticuloDeSegundaMano("electronica", "Jean Hernandez", "gagest antiguos")
