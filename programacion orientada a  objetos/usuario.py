"""clase usuario"""
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

        #---- instancia de la clase usuario-------
#creo la instancia
usuario1 = Usuario("Jean", "hernandez", "88-569-58", "calle 8 21-0", "python","zeus76547")

# Uso de metodos
usuario1.enviar_sugerencia()
usuario1.leer()
usuario1.comprar()
usuario1.vender()
usuario1.realizar_reclamacion()
