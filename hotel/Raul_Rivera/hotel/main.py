from Personas import Manager, cliente, Chef, personalAseo, Recepcionista
from Objetos import Comida, Habitacion, Inventario, boleta

def __main__():
    print ("Aplicacion ejecutandose")

    bebida= Inventario('Gaseosa','Recien Llegada')
    controlInventario(bebida)


def controlInventario(obj: Inventario):
    obj.revisarInventario()


__main__()