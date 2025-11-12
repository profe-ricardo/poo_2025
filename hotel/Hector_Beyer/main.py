# from hotel.Hector_Beyer.a.view.personas_v import chef

# class __main__():
#     print("Aplicacion iniciada")
#     chefcito = chef("Remi", 1 , "Paris", ["Ratattouille"])

#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(["Bebida", "Completo", "Pie de limon"]))

#     print(chefcito.ver_pedidos())

# __main__()

from config.db_config import ConexionOracle

def conectarDB():
    db=ConexionOracle("system", "Ina.2025", "127.0.0.1:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarDB()

    print("Aplicacion iniciada")

    db.desconectar()

if __name__ == "__main__":
    main()