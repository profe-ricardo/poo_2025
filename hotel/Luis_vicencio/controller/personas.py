from model.personas import chef
from model.personas import UsuarioModel, cliente, recepcionista


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
        
    