# from hotel.Chr_vargas.view.personas_v import chef

# def __main__():
#     print("Aplicacion iniciada")
#     chefcito = chef("remi", 1, "Paris", ["Ratatouille"])

#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedidos(['Bebida', 'Completo', 'Pie de limon']))

#     print(chefcito.ver_pedidos())

# __main__()

from config.db_config import ConexionOracle

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
