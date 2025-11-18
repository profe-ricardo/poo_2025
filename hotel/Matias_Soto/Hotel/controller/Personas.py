
from model.Personas import chef

class Chef(chef):
    def __init__(self, nombre, id, locacion, pedidos):
        super().__init__(nombre, id, locacion, pedidos)

    def procesar_pedido(self, pedido: list) -> bool:
        self.Tomar_Pedidos(pedido)
        self.pedido.sort()
        return True
        

