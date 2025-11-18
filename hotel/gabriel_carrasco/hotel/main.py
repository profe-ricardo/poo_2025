from personas import personalAseo, manager, cliente, chef, recepcionista
from objetos import comida, habitacion, inventario, boleta

def __main__():
    print("aplicacion ejecutandose")
     
    bebida = inventario("gaseosa", "recien llegada")
    controliventario(bebida)
    
def controliventario(obj: inventario):
    obj.revisarinventario()
    
__main__()