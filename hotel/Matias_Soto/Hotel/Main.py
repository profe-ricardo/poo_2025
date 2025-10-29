from Personas import Personal_Aseo, Manager, Clientes, Recepcionista
from Objetos import Habitacion,Comida, Inventario, Boleta 

def _main_():
    print("Aplicacion ejecutandose")

    bebida = Inventario("gaseosa", "Restock")
    controlInventario(bebida)

def controlInventario(obj: Inventario):
    obj.revisarInventario()

_main_()
