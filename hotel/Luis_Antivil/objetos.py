class comida():
<<<<<<< HEAD
    def __init__(self, id: int, nombre : str):
        self.id = id
        self.nombre = nombre
    
class habitacion():
    def __init__(self, numero: int, locacion: str):

        self.numero = numero
        self.locacion = locacion
    
class boletas():
    def __init__(self, folio: int, cliente: str):
        self.folio = folio
        self.cliente = cliente
        
    
class inventario():
    def __init__(self, tipo: str, estado: str):
        
        self.tipo = tipo
        self.estado = estado
        
=======
    def __init__(self, nombre:str, tipo:str, precio:float):
        self.nombre = nombre #nombre del plato
        self.tipo = tipo #tipo desayuno almuerzo cena
        self.precio = precio #precio del plato
        

class habitacion():
    def __init__(self, nunmero:int, locacion:str, estado.str):
        self.numero = nunmero #numero de habitacion
        self.locacion = locacion #piso 
        self.estado = estado #ocupado / libre


class boleta():
    def __init__(self, folio:int, cliente:str):
        self.folio = folio #dolio de la boleta
        self.cliente = cliente #cliente asociado a la boleta


class inventarios():
    def _init__(self, tipo:str, estado:int):
        self.tipo = tipo
        self.estado = estado


    def RevisarInventarios(self):
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")

        return self
>>>>>>> 528edc0a12dab429fd3dccef81d7fb173cc1bc84
