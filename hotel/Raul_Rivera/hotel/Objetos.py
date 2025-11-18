class Comida():
    """"""
    def __init__(self, nombre: str, id:int):
        self.nombre=nombre
        self.id=id
    
class Habitacion():
    """"""
    def __init__(self, numero:int, locacion:str):
        self.numero=numero
        self.locacion=locacion

class boleta():
    """"""
    def __init__(self, folio:int, cliente:str):
        self.folio=folio
        self.cliente=cliente
        

class Inventario():
    """"""
    def __init__(self, tipo: str, estado:str):
        self.tipo=tipo
        self.estado=estado
        
    def revisarInventario(self):
        print(f"Tipo : {self.tipo}")
        print(f"Estado: {self.estado}")
        return self