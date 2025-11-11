from config.db_config import ConexionOracle


class Inventario():
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int, conexion:):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo
    
    def agregar_productos(self,producto:list) -> bool:
        for p in producto:
            self.pedidos.append(p)
        return True
    
    def eliminar_producto(self,producto:list) -> bool:
        for p in producto:
            self.pedidos.delete(p)
        return True
    
class Habitacion():
    def __init__(self,numero: int, cantidad_de_personas: int, estado: str):
        self.numero = numero
        self.cantidad_de_personas = cantidad_de_personas
        self.estado = estado
    
    def asignar_habitacion(self, habitacion:int):
        pass

class Boleta():
    def __init__(self, folio: int, cliente:str, usuario:str):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario
