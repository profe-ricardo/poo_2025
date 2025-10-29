from personas import personalAseo, manager, cliente, chef, recepcionista
from objetos import comida, habitacion, inventario, boleta

def __main__():
    print("Aplicacion ejecutandose")

    bebida = inventario('Gaseosa','Recien llegada')
    dato = controlInventario(bebida)

def controlInventario(obj: inventario):
    obj.revisarInventario()

__main__()
