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
    
    usuario = str(input("ingrese su nombre de usuario: "))
    clave = str(input("ingrese su Clave: "))
    clave = bytes(clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(clave, salt)
    clave_encriptada = clave_encriptada.decode("utf-8")

    cursor = db.obtener_cursor()

    consulta = "insert into usuarios ( nombre_usuario, clave) values (:1, :2)"
    cursor.execute(consulta, ( usuario, clave_encriptada,))

    db.connection.commit()
    
    usuario = str(input("ingrese su nombre de usuario: "))
    clave = str(input("ingrese su Clave: "))

    consulta = "select clave from usuarios where nombre_usuario = :1"
    clave_data = cursor.execute(consulta, (usuario,))
    clave_db = cursor.fetchone()
    clave_bytes = bytes(clave, encoding="utf-8")
    clave_test = bytes(clave_db[0], encoding="utf-8")
    

    validacion_clave = bcrypt.checkpw(clave_bytes, clave_test)

    if validacion_clave:
        print("ingreso Correcto")
    else:
        print("credenciales Incorrectas")


    db.desconectar()

if __name__ == "__main__":
    main()




