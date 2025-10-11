"""clase servidor"""
class Servidor:
    """Clase que representa un servidor web que maneja solicitudes como mostrar paginas,
    recibir sugerencias y enviar datos de compra o venta."""

    def muestra_pagina(self):
        """Muestra la pagina solicitada por el usuario."""
        print("Mostrando pagina al usuario")

    def envia_sugerencia(self):
        """Envia una sugerencia al servidor."""
        print("Enviando esta sugerencia al sevidor")

    def envia_datos_de_compra(self):
        """Envia datos de compra al servidor."""
        print("Enviando datos de compra al servidor")

    def envia_datos_de_venta(self):
        """Envia datos de venta al servidor."""
        print("Enviando datos de venta al servidor")

# **Instancia de la clase Servidor**
      # Creo instancia
servidor = Servidor()

# Usar los métodos
servidor.muestra_pagina()
servidor.envia_sugerencia()
servidor.envia_datos_de_compra()
servidor.envia_datos_de_venta()
