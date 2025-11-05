# from view.Personas_V import chef

# def main():
#     print("Aplicacion Inicial")

#     chefcito = chef("remi", 1 , "Paris", ["Rata"])
    
#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(["Bebida","Completo", "Pie de limon"]))

#     print(chefcito.ver_pedidos())

# main()

from config.db_confing import Conexionoracle

def conectarBD():
    db = Conexionoracle("System", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarBD()

    print("Aplicacion Iniciada")

    db.desconectar()
if __name__ == "_main_":
    main()