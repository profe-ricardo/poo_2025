from model.personas import chef
from model.personas import UsuarioModel, clienteModel, recepcionistaModel


class Chef(chef):
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list):
        super().__init__(nombre, id, locacion, pedidos)

    def procesar_pedido(self, pedido: list) -> bool:
        self.tomar_pedido(pedido)
        self.pedidos.sort()
        return True 

class UsuarioController:
    """
        Controlador del usuario.\n
        Métodos para registrar y mostrar usuarios.
    """
    def __init__(self, modelo: UsuarioModel):
        self.modelo = modelo

    def registrar_usuario(self, nombre: str, telefono: int) -> bool:
        """
            Recibe nombre y telefono, realiza registro en BD.\n
            returns Boolean
        """
        if not nombre or not telefono:
            print("[Error]: Datos faltantes para registro de usuario.")
            return False
        
        return self.modelo.crear(nombre, telefono)
        
    def listar_usuarios(self) -> list:
        """
            Muestra los usuarios registrados en BD.\
            returns Lista vacía si es que no hay usuarios, o lista de usuarios registrados.
        """
        usuarios = self.modelo.mostrar_todos()

        if len(usuarios) > 0:
            return [{ "nombre": u[0], "telefono": u[1] } for u in usuarios]
        else:
            return []
        
class clienteController():
    def __init__(self, modelo: clienteModel):
        self.modelo = modelo

    def registrar_cliente(self, nombre:str, telefono: int, nacionalidad: str, habitacion: str) -> bool:
        if not nombre or telefono or not nacionalidad or not habitacion :
            print("[ERROR]: Datos faltantes para registro de clientes ")
            return False
        return self.modelo.crear(nombre, telefono, nacionalidad, habitacion)
    
    def listar_clientes(self) -> list:

        clientes = self.modelo.mostrar_todos()

        if len(clientes) > 0:
            return[{"nombre": u[0], "telefono": u[1], "nacionalidad": u[2], "habitacion": u[3]} for u in clientes]
        else:
            return []
        
class recepcionistaController():
    def __init__(self, modelo: recepcionistaModel):
        self.modelo = modelo

    def registrar_recepcionista(self, nombre:str, telefono: int, ubicacion: str) -> bool:
        if not nombre or not telefono or not ubicacion:
            print("[ERROR]: Datos faltantes para registro de recepcionista")

        
        
    