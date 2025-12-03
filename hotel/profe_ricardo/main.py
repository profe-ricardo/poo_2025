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

    validar_tablas(db)

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
    id_u = int(input("Ingrese su id: "))
    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))
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