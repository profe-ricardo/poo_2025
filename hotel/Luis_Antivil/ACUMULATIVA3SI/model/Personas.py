from Usuario import UsuarioModel
from hotel.Luis_Antivil.ACUMULATIVA3SI.config.db_config1 import ConexionOracle


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
        
    def Crear(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Modificar(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Eliminar(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Mostrar(self,nombre,telefono,ubicacion,conexion):
        """"""
        
        
        
class cliente():
    """
    se debe crear,modificar,eliminar y leer los datos del cliente
    """
    def __init__(self,nombre:str, telefono:int,nacionalidad:str,habitacion:int):
        self.nombre=nombre
        self.telefono=telefono
        self.nacionalidad=nacionalidad
        self.habitacion=habitacion
        
    def Crear(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Modificar(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Eliminar(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Mostrar(self,nombre,telefono,ubicacion,conexion):
        """"""
        