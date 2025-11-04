from model.personas import chef

class chef_c(chef):
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list):
        super().__init__(nombre, id, locacion, pedidos)


    def procesar_pedido(self, pedido: list) -> bool:
        self.tomar_pedidos(pedido)
        self.pedidos.sort()
        return True