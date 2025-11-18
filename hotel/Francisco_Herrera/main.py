# from hotel.Francisco_Herrera.personas import personalAseo, manager, cliente, chef, recepcionista
# from hotel.Francisco_Herrera.objetos import comida, habitacion, inventario, boleta
from view.personas import chef
from config.db_config import ConexionOracle

def conectarBD():
    db = ConexionOracle("system","Ina.2025","localhost:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarBD()

    print("Aplicacion Iniciada")

    db.desconectar()  

if __name__ == "__main__":
    main()

# def __main__():
#     print("Aplicacion Iniciada")
#     chefcito = chef ("Remi", 1, "Paris", ["Ratatoullie"])

#     print(chefcito.ver_pedidos())

#     print(chefcito.procesar_pedido(["Bebida", "Completo", "Pie de Limon"]))

#     print(chefcito.ver_pedidos())

# __main__()

#    bebida = inventario("Gaseosa","Recien llegada")

#def controlInventario(obj: inventario) :
#    obj.revisarInventario() 