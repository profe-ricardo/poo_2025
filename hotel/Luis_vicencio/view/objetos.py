from model.objetos import Inventario
from config.db_config import ConexionOracle

class inventario(Inventario):
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int, conexion: ConexionOracle):
        super().__init__(nombre, tipo, cantidad, precio_costo, conexion)
        

    def ver_inventario(self) -> bool:
        try:
            self.productos.sort()
            return True
        