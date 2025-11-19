class comida():
    def _init_(self, nombre:str, tipo:str, precio:float):
        self.nombre = nombre #nombre del plato
        self.tipo = tipo #tipo desayuno almuerzo cena
        self.precio = precio #precio del plato
        

class habitacion():
    def _init_(self, nunmero:int, locacion:str, estado:str):
        self.numero = nunmero #numero de habitacion
        self.locacion = locacion #piso 
        self.estado = estado #ocupado / libre


class boleta():
    def _init_(self, folio:int, cliente:str):
        self.folio = folio #dolio de la boleta
        self.cliente = cliente #cliente asociado a la boleta


class inventario():
    def __init__(self, tipo:str, cantidad:int):
        self.items = tipo #tipo de objeto
        self.cantidad = cantidad #cantidades del objeto

    def revisarInventario(self):
        print(f"tipo: {self.tipo}")
        print(f"cantidad: {self.cantidad}")
        
        return self