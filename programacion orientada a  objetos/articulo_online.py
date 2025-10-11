"""clase articulo online"""

class ArticuloOnline:
    """La clase articulo online representa un artilo en linea"""
    def __init__(self, tema):
        self.tema = tema

    def publicar(self):
        """este metodo es el encargado de imprimir que un articuko esta siendo publicado"""
        print("Publicando articulo online")
        print("")

        # intancia de la clase articulo online

articulo_online1 = ArticuloOnline("Innovaciones en inteligencia artificial")

# Usar el metodo publicar

articulo_online1.publicar()
