class comida():
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class habitacion():
    def __init__(self, numero_habitacion: int, locacion: str):
        self.numero_habitacion = numero_habitacion
        self.locacion = locacion

class boleta():
    def __init__ (self, numero_boleta: int, nombre_cliente: str):
        self.numero_boleta = numero_boleta
        self.nombre_cliente = nombre_cliente

class inventarios():
    def __init__(self, tipo: str, estado: str):
        self.tipo = tipo
        self.estado = estado

    def revisarInventario(self):
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")

        return self
        
