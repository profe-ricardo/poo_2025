class chef():
    
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list):
        self.nombre=nombre
        self.id=id
        self.locacion=locacion
        self.pedidos = pedidos

    
    def tomar_pedidos(self, pedido: list)-> bool:
        for p in pedido:
            self.pedidos.append(p)

        return True

    def ver_pedidos(self) -> list:
        return self.pedidos