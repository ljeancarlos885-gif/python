"""*****************clases******************"""

class Servidor:
    """Clase que representa un servidor web que maneja solicitudes como mostrar páginas,
    recibir sugerencias y enviar datos de compra o venta."""

    def __init__(self, nombre_servidor, direccion_ip):
        self.nombre_servidor = nombre_servidor
        self.direccion_ip = direccion_ip

    def muestra_pagina(self, url):
        """Muestra la página solicitada por el usuario."""
        print(f"Mostrando la página: {url}")

    def envia_sugerencia(self, sugerencia):
        """Envía una sugerencia al servidor."""
        print(f"Enviando sugerencia: {sugerencia}")

    def envia_datos_de_compra(self, datos_compra):
        """Envía datos de compra al servidor."""
        print(f"Enviando datos de compra al servidor: {datos_compra}")

    def envia_datos_de_venta(self, datos_venta):
        """Envía datos de venta al servidor."""
        print(f"Enviando datos de venta al servidor: {datos_venta}")
        print("")


 # ***clase inxesador***

class Indexador:
    """Clase que se encarga de indexar contenido para facilitar su busqueda"""

    def __init__(self ,nombre_indexador):
        self.nombre_indexador = nombre_indexador

    def actualiza_almacen(self,  almacen):
        """actualiza datos del almacen."""
        print(f"actualizando almacen {almacen}")

    def envia_resultado_de_busqueda(self, busqueda):
        """envio resultados de busqueda."""
        print(f"enviando resultados de busqueda {busqueda}")
        print("")

#***clase procesador***

class Procesador:
    """
    Clase que representa un procesador encargado de ejecutar tareas específicas,
    manipular datos o coordinar operaciones dentro del sistema.
    """
    def __init__(self ,nombre_procesador):
        self.nombre_procesador = nombre_procesador

    def mandar_datos_de_venta(self , datos_venta):
        "envio datos de venta"
        print(f"enviando datos de venta {datos_venta}")

    def mandar_articulo_online(self , articulo_online):
        "envio articulo online ."
        print(f"enviando articulo online {articulo_online}")

    def envia_sugerencia_administrador (self , sugerencia_administrador):
        "se le en envio sugerencia al administrador"
        print(f"enviando sugerencia al administrador {sugerencia_administrador}")

    def modificar_stock(self , stock):
        "datos de stock modificado"
        print(f"modificando datos de stock {stock}")

    def realizar_cobro(self , cobro):
        "realiza cobro"
        print(f"realizando cobro {cobro}")

    def realizar_pago(self , pago):
        "realiza pago"
        print(f"realizando pago {pago}")

    def actualiza_catalogo(self , catalogo):
        "actualiza catalogo"
        print(f"actualizando catalogo {catalogo}")

    def realiza_busqueda(self , busqueda):
        "realiza busqueda"
        print(f"realizando busqueda {busqueda}")
        print("")
#---clase usuario----

class Usuario:
    """
    Esta clase almacena información básica sobre un usuario, como su nombre,
    correo electrónico, y otros atributos que se deseen agregar."""

    def __init__(self, nombre, apellido, numero_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self, sugerencia):
        """permite al usuario enviar sugerencias"""
        print(f"{self.nombre} envió una sugerencia: {sugerencia}")

    def leer(self, contenido):
        """simula que el usuario esta leyendo"""
        print(f"{self.nombre} está leyendo: {contenido}")

    def comprar(self, producto):
        """simula la acción de compra de un producto"""
        print(f"{self.nombre} compró el producto: {producto}")

    def vender(self, producto):
        """simula la venta de un producto"""
        print(f"{self.nombre} vendió el producto: {producto}")

    def realizar_reclamacion(self, mensaje):
        """Permite al usuario realizar una reclamación"""
        print(f"{self.nombre} realizó una reclamación: {mensaje}")
        print("")

                   #***clase producto***
class Producto:
    """ Esta clase almacena información relevante sobre un producto, como su nombre,
    precio y descripción."""

    def __init__(self, precio, titulo, autor, editorial,fecha_de_edicion,
        preferencias, vender, comprar):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.fecha_de_edicion = fecha_de_edicion
        self.preferencias = preferencias
        self.vender = vender
        self.comprar = comprar

    def ver_catalogo(self):
        """muestra toda la descripcion del catalogo """
        print("=== Catálogo del Producto ===")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de edición: {self.fecha_de_edicion}")
        print(f"Precio: ${self.precio}")
        print(f"Preferencias: {', '.join(self.preferencias)}")
        print(f"Disponible para venta: {'Sí' if self.vender else 'No'}")
        print(f"Interesado en comprar: {'Sí' if self.comprar else 'No'}")
        print("")


        #****clase libro****
class Libro:
    """Esta clase muestra las características y descripción de un libro."""

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_libro(self):
        """
        Imprime los detalles del libro con formato.
        """
        print("== Libro última edición 2025 ==")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print("")


        #****clase revista****

class Revista:
    """esta clase muestra una revista """

    def __init__(self, titulo, tipo_revista):
        self.titulo = titulo
        self.tipo_revista = tipo_revista

    def mostrar_revista(self):
        """descripcion de la revista"""
        print("===revista===")
        print(f"Titulo: {self.titulo}")
        print(f"Tipo de revista {self.tipo_revista}")
        print("")

    # *****clase articulo de segugunda mano*****

class ArticuloDeSegundaMano:

    """ Esta clase puede un articulo de segunda mano para la venta
    incluyendo detalles como la  descripción."""

    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

    def mostrar_info(self):
        """descripcion y atributos del articulo"""
        print("=== artículo de Segunda Mano ===")
        print(f"Clasificación: {self.clasificacion}")
        print(f"Tema: {self.tema}")
        print(f"Vendedor: {self.vendedor}")
        print("")

         # *****clase novedades*****

class Novedades:
    """esta clase muestra novedades los de productos"""

    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def mostrar_info(self):
        " descripcion de las novedades"
        print("=== Novedad ===")
        print(f"Clasificación: {self.clasificacion}")
        print(f"Tema: {self.tema}")
        print()

    def cambiar_clasificacion(self, nueva_clasificacion):
        """Cambia la clasificación del producto."""
        self.clasificacion = nueva_clasificacion
        print(f"Clasificación actualizada a: {self.clasificacion}")
        print()


        #*** clase Hilo *****

class Hilo:
    """Define una clase llamada Hilo que representa un producto, en este caso hilo."""

    def __init__(self, nombre_hilo):
        self.nombre_hilo = nombre_hilo

    def buscar_novedades(self, novedades_disponibles, filtro):
        """Busca nuevas novedades sobre este producto."""
        print(f"Buscando novedades en el hilo: {self.nombre_hilo}")
        encontradas = False

        for novedad in novedades_disponibles:
            if (
                filtro.lower() in novedad.tema.lower()
                or filtro.lower() in novedad.clasificacion.lower()
            ):
                novedad.mostrar_info()
                encontradas = True

        if not encontradas:
            print("No se encontraron novedades con ese filtro.\n")
            print("")

  #****clase recolector*****

class Recolector:
    """Esta clase simula la recolección de datos y el envío opcional de novedades"""

    def __init__(self, envia_novedades: bool):
        self.envia_novedades = envia_novedades
        self.novedades = []

    def recolectar(self, novedad):
        """Este método simula la recolección de datos"""
        print(f"Recolectando dato: {novedad}")
        self.novedades.append(novedad)

        if self.envia_novedades:
            self.enviar_novedades()
        else:
            print("Novedades no enviadas (envia_novedades es False).")

    def enviar_novedades(self):
        """Este método simula el envío de novedades"""
        print("Enviando novedades:")
        for novedad in self.novedades:
            print(f"- {novedad}")
        # clase editorial


class Editorial:
    """Esta clase editorial es la en cargada de publicar libros y puede ono venderlos"""

    def __init__(self, nombre, direccion, telefono, puede_vender):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.puede_vender = puede_vender  # Esto indica si esta editorial puede vender

    def vender(self):
        """este metodo vender es quien toma la decicion de venta"""
        if self.puede_vender:
            print(f"La editorial {self.nombre} está vendiendo libros.")
        else:
            print(f"La editorial {self.nombre} no tiene permiso para vender.")
            print("")

            # ****clase articulo online *****

class ArticuloOnline:
    """La clase articulo online representa un artilo en linea"""
    def __init__(self, tema):
        self.tema = tema

    def publicar(self):
        """este metodo es el encargado de imprimir que un articuko esta siendo publicado"""

        print(f"Publicando artículo online sobre: {self.tema}")
        print("")



  #************codigo principal ******************

                #***instancia servidor***
mi_servidor = Servidor("servidor_central" , "192.168.127.1")
mi_servidor.muestra_pagina("www.tiendaonline.com")
mi_servidor.envia_sugerencia("te interesa ver nuestros productos")
mi_servidor.envia_datos_de_compra(" produucto comprado zapatos $50.500")
mi_servidor.envia_datos_de_venta("2 productos vendidos")

                  # ****instancia indexador******

mi_indexador = Indexador("indexador_1")
mi_indexador.actualiza_almacen("actualización exitosa")
mi_indexador.envia_resultado_de_busqueda("resultados de buqueda fueron exitosos")

                  #***instancia procesador***

mi_procesador = Procesador("procesador_1")
mi_procesador.mandar_datos_de_venta("3 productos vendidos")
mi_procesador.mandar_articulo_online("nuevo articulo online")
mi_procesador.envia_sugerencia_administrador("sugerencia para administrador")
mi_procesador.modificar_stock("stock actualizado")
mi_procesador.realizar_cobro("cobro por $50.500")
mi_procesador.realizar_pago("pago por $10,000")
mi_procesador.actualiza_catalogo("nuevo catalogo 2025")
mi_procesador.realiza_busqueda("productos de la busqueda 4")


     #---- instancia de la clase usuario-------

usuario1 = Usuario(
    nombre="Carlos",
    apellido="Ramírez",
    numero_cuenta="00123456789",
    direccion="Calle 10 #45-67, Bogotá",
    login="carlos",
    password="segura123"
)

# Uso de métodos
usuario1.enviar_sugerencia("Agregar más opciones de pago.")
usuario1.leer("Política de privacidad")
usuario1.comprar("Celular Samsung Galaxy")
usuario1.vender("Audífonos Bluetooth")
usuario1.realizar_reclamacion("El producto no coincide con la descripción.")

#*****instancia  de la clase producto****
producto1 = Producto(
    precio=29.99,
    titulo="Introducción a la Programación",
    autor="Juan Perez",
    editorial="Editorial Python",
    fecha_de_edicion=2023,
    preferencias=["Tecnologia", "Educativo", "Programación"],
    vender=True,
    comprar=False
)

    #***Mostrar en pantalla el catálogo del producto***#
producto1.ver_catalogo()

    #*** instancia  de la clase libro **** #

libro_edition_2 = Libro(
    titulo = "Una guerra sin fin",
    autor = "Juan lozano"

)
    # ***mostrar en pantalla el libro***

libro_edition_2.mostrar_libro()

    #+++instancia  de la clase revista++++

revista01 = Revista(
    titulo = "nivea",
    tipo_revista = "farandula"
)

#*** mostrar en pantalla revista***
revista01.mostrar_revista()

 # ***** instancia   de la clase articulo de segugunda mano *****

articulo1 = ArticuloDeSegundaMano(
    clasificacion="Electrónica",
    tema="Gadgets antiguos",
    vendedor="Jean Hernandez"
)

articulo1.mostrar_info()

  #****instancia  de la clase novedadad*****

novedad1 = Novedades(clasificacion="Tecnología", tema="Lanzamiento de nuevos dispositivos")

novedad1.mostrar_info()

novedad1.cambiar_clasificacion("Innovación")

# Crear algunas novedades
n1 = Novedades("Tecnología", "Lanzamiento de nuevos dispositivos")
n2 = Novedades("Ciencia", "Descubrimiento de una nueva galaxia")
n3 = Novedades("Educación", "Nuevos métodos de enseñanza digital")

# Crear lista de novedades
lista_novedades = [n1, n2, n3]

# Instancia de la clase Hilo
hilo1 = Hilo("Hilo de Actualizaciones")

# Buscar por tema o clasificación
hilo1.buscar_novedades(lista_novedades, "tecnología")  # Coincide con n1
hilo1.buscar_novedades(lista_novedades, "nueva galaxia")  # Coincide con n2
hilo1.buscar_novedades(lista_novedades, "salud")  # No hay coincidencias

# instancia de la clase Recolector

mi_recolector = Recolector(envia_novedades=True)

# Agregar algunas novedades
mi_recolector.recolectar("Fallo en el sensor de humedad")
mi_recolector.recolectar("Nivel de batería crítico")

# Enviar las novedades explícitamente (opcional si quieres enviarlas en otro momento)
mi_recolector.enviar_novedades()

# instancia de la clase Editorial

# Crear una instancia de la clase Editorial
editorial1 = Editorial(
    nombre="Editorial Omega",
    direccion="Calle 8 #12-34, Ciudad Central",
    telefono="321-456-7890",
    puede_vender=True
)

# Uso del método vender()
editorial1.vender()

# intancia de la clase articulo

articulo_online1 = ArticuloOnline("Innovaciones en inteligencia artificial")

# Usar el método publicar
articulo_online1.publicar()
