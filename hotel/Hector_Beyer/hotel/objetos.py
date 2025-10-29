class comida():
    def __init__(self, id:int, nombre:str):
        self.id = id
        self.nombre = nombre

class habitacion():
    def __init__(self, numero:id, locacion:str):
        self.numbero = numero
        self.locacion = locacion

class boleta():
    def __init__(self, numero:int, nombre:str):
        self.numbero = numero
        self.nombre = nombre

class inventarios():
    def __init__(self, tipo:str, estado:str):
        self.tipo = tipo
        self.estado = estado

    def revisarInventario(self):
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")

        return self

