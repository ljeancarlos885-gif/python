"""******clases*******"""
#clase servidor
class Servidor:
    """Clase que representa un servidor web que maneja solicitudes como mostrar paginas,
    recibir sugerencias y enviar datos de compra o venta."""

    def muestra_pagina(self):
        """Muestra la pagina solicitada por el usuario."""
        print("Mostrando pagina al usuario")

    def envia_sugerencia(self):
        """Envia una sugerencia al servidor."""
        print("Enviando sugerencia")

    def envia_datos_de_compra(self):
        """Envia datos de compra al servidor."""
        print("Enviando datos de compra al servidor")

    def envia_datos_de_venta(self):
        """Envia datos de venta al servidor."""
        print("Enviando datos de venta al servidor")
        print("")

#**clase procesador**

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
        print("")


 # **clase indexador**

class Indexador:
    """Clase que se encarga de indexar contenido para facilitar su busqueda"""

    def actualiza_almacen(self):
        """metodo que actualiza datos del almacen"""
        print("actualizando almacen")

    def envia_resultado_de_busqueda(self):
        """metodo para enviar resultados de busqueda"""
        print("enviando resultados de busqueda")
        print("")

        #**clase producto**

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

        #clase editorial

    def vender(self):
        """metodo que muestra las ventas del producto."""
        print("realizando ventas de productos")

    def comprar(self):
        """metodo usado para la compra de productos."""
        print("realizando compra de productos")

    def ver_catalogo(self):
        """metodo usado para ver el catálogo"""
        print("observando un catalogo")
        print("")

class Editorial:
    """Esta clase editorial es la en cargada de publicar libros"""

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        """este metodo lo usamos para vender el editorial"""
        print("vendiendo un editorial")
        print("")


        #*clase recolector**

class Recolector:
    """Esta clase simula la recoleccion de datos y el envio opcional de novedades"""
    def enviar_novedades(self):
        """Este metodo simula el envio de novedades"""
        print("Enviando novedades:")
        print("")

        #---clase usuario----

class Usuario:
    """
    Esta clase almacena informacion basica sobre un usuario, como su nombre,
    correo electronico, y otros atributos que se deseen agregar."""

    def __init__(self, nombre, apellido, numero_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self):
        """permite al usuario enviar sugerencias"""
        print("enviando sugerencias")

    def leer(self):
        """simula que el usuario esta leyendo"""
        print("el usuario se encuentra leyendo")

    def comprar(self):
        """simula la accion de compra de un producto"""
        print("comprando un producto")

    def vender(self):
        """simula la venta de un producto"""
        print("vendiendo un producto")

    def realizar_reclamacion(self):
        """Permite al usuario realizar una reclamacion"""
        print("realizando reclamacion")
        print("")

        #*clase libro*

class Libro:
    """Esta clase muestra las caracteristicas y descripcion de un libro"""

    def __init__(self, genero):
        self.genero = genero

        #*clase revista*

class Revista:
    """esta clase muestra una revista """

    def __init__(self, categoria):
        self.categoria = categoria

            # *clase articulo online **

class ArticuloOnline:
    """La clase articulo online representa un artilo en linea"""
    def __init__(self, tema):
        self.tema = tema

    def publicar(self):
        """este metodo es el encargado de imprimir que un articuko esta siendo publicado"""
        print("Publicando articulo online")
        print("")

    # **clase articulo de segugunda mano**

class ArticuloDeSegundaMano:

    """ Esta clase puede un articulo de segunda mano para la venta
    incluyendo detalles como la  descripcion."""

    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor


         # **clase novedades**

class Novedades:
    """esta clase muestra novedades los de productos"""

    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def cambiar_clasificacion(self):
        """Cambia la clasificacion del producto."""
        print("Clasificacion actualizada")
        print("")


        #* clase Hilo ***

class Hilo:
    """Define una clase llamada Hilo que representa un producto, en este caso hilo."""

    def buscar_novedades(self):
        """Busca nuevas novedades sobre este producto."""
        print("Buscando novedades en el hilo")


         #*****codigo principal *******

# **Instancia de la clase Servidor**
      # Creo instancia
servidor = Servidor()

    # Usar los métodos
servidor.muestra_pagina()
servidor.envia_sugerencia()
servidor.envia_datos_de_compra()
servidor.envia_datos_de_compra()

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

# *instancia indexador***
    #creo instancia
mi_indexador = Indexador()
    #uso de metodo
mi_indexador.actualiza_almacen()
mi_indexador.envia_resultado_de_busqueda()

   # Instancia de la clase producto
    #creo la instancia
producto1 = Producto("40000", "python primeros pasos", "juan perez",
                     "editorial multitec", "2027-10-18", "programacion")

# Uso de métodos
producto1.ver_catalogo()
producto1.vender()
producto1.comprar()

  # instancia de la clase Editorial
# Crear una instancia de la clase Editorial
editorial1 = Editorial("editorial omega", "Calle 8 #12-34, Ciudad Cucuta","321-456-7890")

# Uso del metodo vender()
editorial1.vender()

 # instancia de la clase Recolector
    #creo la instancia
mi_recolector = Recolector()

    # uso del metodo
mi_recolector.enviar_novedades()

     #---- instancia de la clase usuario-------
#creo la instancia
usuario1 = Usuario("Jean", "hernandez", "88-569-58", "calle 8 21-0", "python","zeus76547")

# Uso de metodos
usuario1.enviar_sugerencia()
usuario1.leer()
usuario1.comprar()
usuario1.vender()
usuario1.realizar_reclamacion()

 #* instancia  de la clase libro ** #

libro_edition = Libro("el principito")

    #+++instancia  de la clase revista++++

revista01 = Revista("ciencia y tecnologia")

# intancia de la clase articulo online

articulo_online1 = ArticuloOnline("Innovaciones en inteligencia artificial")

# Usar el metodo publicar
articulo_online1.publicar()


 # ** instancia   de la clase articulo de segugunda mano **

articulo1 = ArticuloDeSegundaMano("electronica", "Jean Hernandez", "gagest antiguos")


  #*instancia  de la clase novedadad**

novedad1 = Novedades("Tecnologia", "Lanzamiento de nuevos dispositivos")

novedad1.cambiar_clasificacion()


# Instancia de la clase Hilo
hilo1 = Hilo()

# uso del metodo
hilo1.buscar_novedades()

