# from hotel.Francisco_Herrera.personas import personalAseo, manager, cliente, chef, recepcionista
# from hotel.Francisco_Herrera.objetos import comida, habitacion, inventario, boleta
from view.personas import chef

def __main__():
    print("Aplicacion Iniciada")
    chefcito = chef ("Remi", 1, "Paris", ["Ratatoullie"])

    print(chefcito.ver_pedidos())

    print(chefcito.procesar_pedido(["Bebida", "Completo", "Pie de Limon"]))

    print(chefcito.ver_pedidos())

__main__()

#    bebida = inventario("Gaseosa","Recien llegada")

#def controlInventario(obj: inventario) :
#    obj.revisarInventario() 