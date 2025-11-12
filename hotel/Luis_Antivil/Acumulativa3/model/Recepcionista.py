from Usuario import UsuarioModel
from hotel.Luis_Antivil.config.db_config import ConexionOracle
class recepcionista(): 
    """
    se debe poder crear, modificar, eliminar y leer \n
    los datos de la cuenta del recepcionista
    """
    def __init__(self, nombre:str, telefono:int, ubicacion:str, conexion:ConexionOracle):
        super().__init__(nombre,telefono,ubicacion, conexion)
        self.nombre=nombre
        self.telefono=telefono
        self.ubicacion=ubicacion
        self.conexion=conexion
        
    
    
    
