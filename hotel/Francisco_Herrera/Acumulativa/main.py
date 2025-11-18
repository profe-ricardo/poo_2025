from config.db_config import ConexionOracle
from model.personas_m import UsuarioModel
from controller.personas_c import UsuarioController
from view.personas_v import UsuarioView


def conectarBD():
    """
        Realiza conexión a BD utilizando función predefinida.
    """
    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    return db


def main():
    """
        Genera registro de usuario en BD conectada.\n
        Debe existir tabla 'usuarios' con las columnas 'nombre' y 'telefono'.\n
        Tabmién devuelve una lista de los usuarios registrados.
    """
    db = conectarBD()
    modelo = UsuarioModel(db)
    controlador = UsuarioController(modelo)
    vista = UsuarioView()

    print("Aplicacion iniciada")

    ingreso = controlador.registrar_usuario('Ricardo', 912345678)

    if ingreso:
        usuarios = controlador.listar_usuarios()
        vista.mostrar_usuarios(usuarios)

    db.desconectar()

if __name__ == "__main__":
    main()