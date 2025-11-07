# from view.personas import chef

# def main():
#     print("aplicacion iniciada")
#     chefcito = chef("Remi", 1, "paris", ["Ratatoullie"])

#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(["Bebida", "Completo", "Pie de limon"]))

#     print(chefcito.ver_pedidos())

# main()

from config.db_config import ConexionOracle
# from hotel.Luis_vicencio.model.personas import UsuarioModel
# from hotel.Luis_vicencio.controller.personas import UsuarioController
# from hotel.Luis_vicencio.view.personas import UsuarioView

def conectarBD():
    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarBD()

    print("Aplicacion iniciada")

    db.desconectar()
    
if __name__ == "__main__":
    main()
