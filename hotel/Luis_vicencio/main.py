# from view.personas import chef

# def main():
#     print("aplicacion iniciada")
#     chefcito = chef("Remi", 1, "paris", ["Ratatoullie"])

#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(["Bebida", "Completo", "Pie de limon"]))

#     print(chefcito.ver_pedidos())

# main()

import bcrypt

from config.db_config import ConexionOracle
# #from model.personas import UsuarioModel
# #from controller.personas import UsuarioController
# #from view.personas import UsuarioView

def conectarBD():

    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()
    
    # validar_tablas(db)

    return db

# def main():
#     db = conectarBD()

#     print("Aplicacion iniciada")

#     db.desconectar()


#from model.objetos import ver_inventario

def main():
    db = conectarBD()
    
    print("Inicio de sesion, Ingrese sus credenciales\n")
    id_u = int(input("ingrese su ID: "))
    usuario = str(input("ingrese su nombre de usuario: "))
    clave = str(input("ingrese su Clave: "))
    clave = bytes(clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(clave, salt)

    cursor = db.obtener_cursor()

    consulta = "insert into usuarios (id, nombre_usuario, clave) values (:1, :2, :3)"
    cursor.execute(consulta, (id_u, usuario, clave_encriptada))
    db.connection.commit()
    
    db.desconectar()

if __name__ == "__main__":
    main()




