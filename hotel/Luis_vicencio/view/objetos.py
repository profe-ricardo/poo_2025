from model.objetos import Inventario

class inventario(Inventario):
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int):
        super().__init__(nombre, tipo, cantidad, precio_costo)

    def ver_inventario(self, productos: list) -> bool:
        return self.productos(productos) 