"""principal.py"""

from modelo_servidor import Servidor  # Importación al inicio del archivo
from modelo_procesador import Procesador # Importación al inicio del archivo
from modelo_indexador import Indexador  # Importación al inicio del archivo
from modelo_producto import Producto  # Importación al inicio del archivo
from modelo_editorial import Editorial # Importación al inicio del archivo
from modelo_recolector import Recolector # Importación al inicio del archivo
from modelo_usuario import Usuario # Importación al inicio del archivo
from modelo_libro import Libro # Importación al inicio del archivo
from modelo_revista import Revista # Importación al inicio del archivo
from modelo_articulo_online import ArticuloOnline # Impoarchivo
from modelo_articulo_de_segunda_mano import ArticuloDeSegundaMano
from modelo_novedades import Novedades # Importación al inicio del archivo
from modelo_hilo import Hilo # Importación al inicio del archivo

#metodo servidor
print("#" * 30)
servidor = Servidor()
servidor.muestra_pagina()

#metodo procesador
print("#" * 30)
procesador = Procesador()
procesador.mandar_datos_de_venta()

print("#" * 30)

#modelo indexador
print("#" * 30)
indexador = Indexador()
indexador.actualiza_almacen()

#modelo producto
print("#" * 30)
producto = Producto("40000", "python primeros pasos", "juan perez",
                   "editorial multitec", "2027-10-18", "programacion")

#modelo editorial
print("#" * 30)
editorial = Editorial("editorial omega", "Calle 8 #12-34, Ciudad Cucuta","321-456-7890")

#modelo recolector
print("#" * 30)
recolector = Recolector()
recolector.enviar_novedades()

#modelo usuario
print("#" * 30)
usuario = Usuario("Jean", "hernandez", "88-569-58", "calle 8 21-0", "python","zeus76547")

#modelo libro
print("#" * 30)
libro = Libro("el principito")

# modelo revista
print("#" * 30)
revista = Revista("ciencia y tecnologia")

#modelo articulo online
print("#" * 30)
articuloonline = ArticuloOnline("Innovaciones en inteligencia artificial")

# modelo articulo de segunda
print("#" * 30)
articulo = ArticuloDeSegundaMano("electronica", "Jean Hernandez", "gagest antiguos")

#modelo novedades
print("#" * 30)
novedades = Novedades("Tecnologia", "Lanzamiento de nuevos dispositivos")

#modelo hilo
print("#" * 30)
hilo = Hilo()
hilo.buscar_novedades()
