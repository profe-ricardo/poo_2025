from controller.personas import CHEF

class chef(CHEF):
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list):
        super().__init__(nombre, id, locacion, pedidos)

def recibir_pedido(self, pedido: list) -> bool:
    return self.procesar_pedido(pedido)
