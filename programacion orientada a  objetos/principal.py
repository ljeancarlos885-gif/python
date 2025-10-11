"""principal.py"""

from modelo_servidor import Servidor  # Importación al inicio del archivo
from modelo_procesador import Procesador # Importación al inicio del archivo
from modelo_indexador import Indexador  # Importación al inicio del archivo
from modelo_producto import Producto  # Importación al inicio del archivo




print("Inicio del programa")

s = Servidor()
s.iniciar()  # pylint: disable=no-member  # Opcional, para evitar falso positivo de Pylint

# modelo_procesador

print("Inicio del programa")

s = Procesador()
s.iniciar()  # pylint: disable=no-member  # Opcional, para evitar falso positivo de Pylint

# modelo_indexador

print("Inicio del programa")

s = Indexador()
s.iniciar()  # pylint: disable=no-member  # Opcional, para evitar falso positivo de Pylint

# modelo_producto

print("Inicio del programa")

s = Producto()
s.iniciar()  # pylint: disable=no-member  # Opcional, para evitar falso positivo de Pylint
