from config.db_config import ConexionOracle
import bcrypt

# from hotel.Luis_Antivil.model.personas import UsuarioModel
# from hotel.Luis_Antivil.controller.personas import UsuarioController
# from hotel.Luis_Antivil.view.personas import UsuarioView

def conectarBD():
    """
        Realiza conexión a BD utilizando función predefinida.
    """
    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    return db

# def main():
#     """
#         Genera registro de usuario en BD conectada.\n
#         Debe existir tabla 'usuarios' con las columnas 'nombre' y 'telefono'.\n
#         Tabmién devuelve una lista de los usuarios registrados.
#     """
#     db = conectarBD()
#     modelo = UsuarioModel(db)
#     controlador = UsuarioController(modelo)
#     vista = UsuarioView()

#     print("Aplicacion iniciada")

#     ingreso = controlador.registrar_usuario('Ricardo', 912345678)

#     if ingreso:
#         usuarios = controlador.listar_usuarios()
#         vista.mostrar_usuarios(usuarios)

#     db.desconectar()

def main():
    db= conectarBD()
    print("inicio de sesion, insgrese sus credenciales\n")
    id_u= int(input("ingrese su id"))
    usuario= str(input("ingrese nombre de usuario:  "))
    clave= str(input("ingrese clave de usuario:  "))
    clave=bytes(clave, encoding="utf-8")

    salt=bcrypt.gensalt()
    clave_encriptada=bcrypt.hashpw(clave, salt)

    cursor=db.obtener_cursor()

    consulta="insert into usuarios (id, nombre_usuario, clave) values (:1,:2,:3)"
    cursor.execute(consulta,(id_u,usuario,clave_encriptada))
    db.connection.commit()
    
    db.desconectar


    print(clave_encriptada)

if __name__ == "__main__":
    main()



