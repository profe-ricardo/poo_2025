class COMIDA():
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class HABITACIONES():
    def __init(self, numero: int,cantidad_personas: int, estado: str):
        self.numero = numero
        self.cantidad_personas = cantidad_personas
        self.estado = estado

class BOLETA():
    def __init__(self, folio: int, cliente: str):
        self.folio = folio
        self.cliente = cliente

class INVENTARIO():
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad 
        self.precio = precio_costo

    def revisarInventario(self):
        print(f"tipo: {self.tipo}")
        print(f"estado: {self.estado}")