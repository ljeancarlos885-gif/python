"""clase procesador"""
class Procesador:
    """
    Clase que representa un procesador encargado de ejecutar tareas especificas,
    manipular datos o coordinar operaciones dentro del sistema.
    """

    def mandar_datos_de_venta(self):
        """mtodo usado para el mandar datos de venta"""
        print("enviando datos de venta")

    def mandar_articulo_online(self):
        """metodo para mandar articulo online"""
        print("enviando articulo online")

    def envia_sugerencia_administrador (self):
        """metodo para enviar sugerencias al administrador"""
        print("enviando sugerencia al administrador")

    def modificar_stock(self):
        """metodo para modificar el stock"""
        print("modificando datos de stock")

    def realizar_cobro(self):
        """este metodo se ipmplementa para cobrar"""
        print("realizando cobro")

    def realizar_pago(self):
        """metodo para para hacer el pago"""
        print("realizando pago")

    def actualiza_catalogo(self):
        """metodo para actualiza el catalogo"""
        print("actualizando catalogo")

    def realiza_busqueda(self):
        """metodo ppara realizar busqueda"""
        print("realizando... busqueda")

         #**instancia procesador**
    #creo instancia
mi_procesador = Procesador()
    #usar de metodos
mi_procesador.mandar_datos_de_venta()
mi_procesador.mandar_articulo_online()
mi_procesador.envia_sugerencia_administrador()
mi_procesador.modificar_stock()
mi_procesador.realizar_cobro()
mi_procesador.realizar_pago()
mi_procesador.actualiza_catalogo()
mi_procesador.realiza_busqueda()
