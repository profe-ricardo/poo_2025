from Usuario import UsuarioModel
from hotel.Luis_Antivil.config.db_config import ConexionOracle
class recepcionista(): 
<<<<<<< HEAD
=======
    """
    se debe poder crear, modificar, eliminar y leer \n
    los datos de la cuenta del recepcionista
    """
>>>>>>> 528edc0a12dab429fd3dccef81d7fb173cc1bc84
    def __init__(self, nombre:str, telefono:int, ubicacion:str, conexion:ConexionOracle):
        super().__init__(nombre,telefono,ubicacion, conexion)
        self.nombre=nombre
        self.telefono=telefono
        self.ubicacion=ubicacion
        self.conexion=conexion
<<<<<<< HEAD
    
    
=======
        
    def Crear_Recepcionista(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Modificar_Usuario(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Eliminar_Usuario(self,nombre,telefono,ubicacion,conexion):
        """"""
        
    def Mostrar_Usuario(self,nombre,telefono,ubicacion,conexion):
        """"""
>>>>>>> 528edc0a12dab429fd3dccef81d7fb173cc1bc84
