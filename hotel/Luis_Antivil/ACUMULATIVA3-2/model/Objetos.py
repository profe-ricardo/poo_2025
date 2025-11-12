from model.Usuario import UsuarioModel
from Personas import cliente


class boleta():
    """
    se debe poder generar una boleta, actualizar, eliminar o leer lo de la boleta
    """
    def __init__(self,folio:int,cliente:cliente,usuario:(UsuarioModel)):
        self.folio=folio
        self.cliente=cliente
        
class inventario():
    """
    se debe poder generar un inventario, actualizar, eliminar o leer lo del inventario
    """
    def __init__(self,nombre:str,precio:int,cantidad:int,precio_costo:int):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.precio_costo=precio_costo