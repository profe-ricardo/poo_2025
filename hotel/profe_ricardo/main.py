import bcrypt

from config.db_config import ConexionOracle, validar_tablas
# from hotel.profe_ricardo.model.personas_m import UsuarioModel
# from hotel.profe_ricardo.controller.personas_c import UsuarioController
# from hotel.profe_ricardo.view.personas_v import UsuarioView

def conectarBD():
    """
        Realiza conexión a BD utilizando función predefinida.
    """
    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    # validar_tablas(db)

    return db

# def main():
#     """
#         Genera registro de usuario en BD conectada.\n
#         Debe existir tabla 'usuarios' con las columnas 'nombre' y 'telefono'.\n
#         Tabmién devuelve una lista de los usuarios registrados.
#     """
#     db = conectarBD()
    
#     try:
#         modelo = UsuarioModel(db)
#         controlador = UsuarioController(modelo)
#         vista = UsuarioView()

#         print("Aplicacion iniciada")

#         ingreso = controlador.registrar_usuario('Ricardo', 912345678)

#         if ingreso:
#             usuarios = controlador.listar_usuarios()
#             vista.mostrar_usuarios(usuarios)
#     finally:
#         db.desconectar()

def main():
    db = conectarBD()

    print("Inicio de sesión, ingrese sus credenciales\n")
    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))
    clave = bytes(clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(clave, salt)
    clave_encriptada = clave_encriptada.decode(encoding="utf-8")

    cursor = db.obtener_cursor()

    consulta = "insert into usuarios (nombre_usuario, clave) values (:1, :2)"
    cursor.execute(consulta, (usuario, clave_encriptada,))
    db.connection.commit()

    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))

    consulta = "select clave from usuarios where nombre_usuario = :1"
    cursor.execute(consulta, (usuario,))
    clave_bd = cursor.fetchone()
    clave_bytes = bytes(clave, encoding="utf-8")
    clave_test = bytes(clave_bd[0], encoding="utf-8",)

    validacion_clave = bcrypt.checkpw(clave_bytes, clave_test)

    if validacion_clave:
        print("Ingreso correcto")
    else:
        print("Credenciales incorrectas")

    db.desconectar()

if __name__ == "__main__":
    main()