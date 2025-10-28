class comida():
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class habitacion():
    def __init__(self, numero: int, locacion: str):
        self.numero = numero
        self.locacion = locacion

class boleta():
    def __init__(self, folio: int, cliente: str):
        self.folio = folio
        self.cliente = cliente

class inventario():
    def __init__(self, tipo: str, estado: str):
        self.tipo = tipo
        self.estado = estado