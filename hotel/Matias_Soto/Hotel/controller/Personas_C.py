
from model.Personas_M import chef

class Chef(chef):
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list):
        super().__init__(nombre, id, locacion, pedidos)

    def procesar_pedido(self, pedido: list) -> bool:
        self.Tomar_Pedidos(pedido)
        self.pedidos.sort()
        return True
        

