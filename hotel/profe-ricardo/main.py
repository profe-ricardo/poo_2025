# from personas import personalAseo, manager, cliente, chef, recepcionista
from objetos import comida, habitacion, inventarios, boleta

def __main__():
    print("Aplicacion ejecutandose")

    bebida = inventarios('Gaseosa', 'Recien  llegada')
    controlInventario(bebida)

def controlInventario(obj: inventarios):
    obj.revisarInventario()

__main__() 