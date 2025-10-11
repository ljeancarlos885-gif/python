"""clase novedades"""
class Novedades:
    """esta clase muestra novedades los de productos"""

    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self):
        """Cambia la clasificacion del producto."""
        print("Clasificacion actualizada")
        print("")

        #*instancia  de la clase novedadad**

novedad1 = Novedades("Tecnologia", "Lanzamiento de nuevos dispositivos")

novedad1.cambiar_clasificacion()
