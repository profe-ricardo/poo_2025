from config.db_config import ConexionOracle
# from view.personas_v import chef

def conectarDB():
    db=ConexionOracle('system','Ina.2025','localhost:1521/xe')
    db.conectar()

    return db

def main():
    db= conectarDB()

    print('Aplicacion Iniciada')

    db.desconectar()

# def __main__():
#     print('Aplicacion iniciada')
#     chefcito = chef('Remi',1,'Paris',['Ratatoullie'])

#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(['Bebida','Completo', 'Pie de limon']))

#     print(chefcito.ver_pedidos())

main()