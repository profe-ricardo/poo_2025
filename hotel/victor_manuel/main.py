from personas import personalAseo, manager, recepcionistas, chef, cliente
from objetos import comida, habitacion, boleta , inventario

def _main_():
    print("aplicaciones ejecutandose...")

    bebidas = inventario('gaseosas', 'recien llegadas')

def controlInventario(obj: inventario):
    obj.revisarInventario()


_main_