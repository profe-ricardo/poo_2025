import re 
from model.personas_m import UsuarioModel
from model.personas_m import RecepcionistaModel
from model.personas_m import ClienteModel

class ClienteController:
    def __init__(self, model: ClienteModel):
        self.model = model

    def registrar_cliente(self, nombre: str, telefono: int, nacionalidad: str, habitacion: int) -> bool:
        if not nombre or not telefono or not nacionalidad or not habitacion:
            print("[ERROR]: Datos faltantes para registro de cliente.")
            return False
        
        return self.model.crear(nombre, telefono, nacionalidad, habitacion)
        
    def listar_clientes(self) -> list:
        clientes = self.model.mostrar_todos()

        if len(clientes) > 0:
            return [{"nombre": u[0], "telefono": u[1], "nacionalidad": u[2], "habitacion": u[3]} for u in clientes]
        else:
            return[]
        
class UsuarioController:
    def __init__(self, model: UsuarioModel):
        self.model = model

    def registrar_usuario(self, nombre: str, telefono: int) -> bool:

        if not nombre or not telefono:
            print("[Error]: Datos faltantes para registro de usuario.")
            return False
        
        return self.model.crear(nombre, telefono)
    
    def listar_usuarios(self) -> list:
        usuarios = self.model.mostrar_todos()

        if len(usuarios) > 0:
            return [{"nombre": u[0], "telefono": u[1]} for u in usuarios]
        else: 
            return[]
        
class RecepcionistaController:
    def __init__(self, model: RecepcionistaModel):
        self.model = model

    def registrar_recepcionista(self, nombre: str, telefono: int, ubicacion: str) ->bool:

        if not nombre or not telefono or not ubicacion:
            print("[Error]: Datos faltantes para registro de recepcionista.")
            return False
        
        return self.model.crear(nombre, telefono, ubicacion)
    
    def listar_recepcionista(self) -> list:
        recepcionistas = self.model.mostrar_todos()

        if len(recepcionistas) > 0:
            return [{"nombre": u[0], "telefono": u[1], "ubicacion": u[2]} for u in recepcionistas]
        else:
            return[]        
