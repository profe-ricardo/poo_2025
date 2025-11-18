from hotel.camilo_hernandez.controller.personas_c import chef_c

class Chef(chef_c):
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list | None):
        super().__init__(nombre,id,locacion,pedidos)

    def recibir_pedidos(self, pedido: list)-> bool:
        return self.procesar_pedido(pedido)