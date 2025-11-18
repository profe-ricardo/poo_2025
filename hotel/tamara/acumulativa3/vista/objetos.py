class inventario():
    def __init__(self, nombre: str, tipo: str, cantidad: int, precio_costo: int):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo

class habitacion():
    def __init__(self, numero: int, cantidad_personas: int, estado: str):
        self.numero = numero
        self.cantidad_personas = cantidad_personas
        self.estado = estado

class boleta():
    def __init__(self, folio: int, cliente: str, usuario: str):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario 
        