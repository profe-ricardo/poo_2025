from model.objetos import Inventario
<<<<<<< HEAD

class inventario(Inventario):
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int):
        super().__init__(nombre, tipo, cantidad, precio_costo)

    def ver_inventario(self, productos: list) -> bool:
        return self.productos(productos) 
=======
from config.db_config import ConexionOracle

class inventario(Inventario):
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int, conexion: ConexionOracle):
        super().__init__(nombre, tipo, cantidad, precio_costo, conexion)
        

    def ver_inventario(self) -> bool:
        try:
            self.productos.sort()
            return True
        
>>>>>>> ea8d887638b4be4adf2a66cbe5502ba5324ed06f
