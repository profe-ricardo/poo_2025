from Usuario import UsuarioModel
from hotel.Raul_Rivera.config.db_config import ConexionOracle

class recepcionista(UsuarioModel):

    def __init__(self, nombre:str, telefono:int, ubicacion:str, conexion:ConexionOracle):
        super().__init__(conexion)
        self.nombre=nombre
        self.telefono=telefono
        self.ubicacion=ubicacion
        self.conexion=UsuarioModel.conexion