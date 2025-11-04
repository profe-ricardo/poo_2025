

class chef:
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list ):
        self.nombre = nombre
        self.id = id
        self.Locacion = locacion
        self.pedidos = pedidos
    
    def Tomar_Pedidos(self, pedido: list) -> bool:
        for p in pedido:
            self.pedido.append(p)
        return True
    
    def ver_pedido(self) -> list:
        return self.pedido
