# from view.personas import chef

# def __main__():

#     print("Aplicacion iniciada")
#     chefcito = chef('Remi', 1, 'Paris', ['Ratatoullie'])

#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(['Bebida', 'Completo', 'Pie de Limon']))

#     print(chefcito.ver_pedido())

# __main__()

from config.db_config import ConexionOracle
# from config.db_config import UsuarioModel
# from config.db_config import UsuarioController
# from config.db_config import UsuarioView

def conectarBD():
    db = ConexionOracle("system","Ina.2025","localhost:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarBD()

    print("Aplicacion iniciada")

    db.desconectar()

if __name__ == "__main__":
    main()