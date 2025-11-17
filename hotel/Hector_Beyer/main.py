from config.db_config import ConexionOracle
from hotel.Hector_Beyer.model.personas_m import UsuarioModel
from hotel.Hector_Beyer.controller.personas_c import UsuarioController
from hotel.Hector_Beyer.view.personas_v import UsuarioView


def conectarBD():
    db=ConexionOracle("system", "Ina.2025", "127.0.0.1:1521/xe")
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

    ingreso = controlador.registrar_usuario('Hector', 912345678)

    if ingreso:
        usuarios = controlador.listar_usuarios()
        vista.mostrar_usuarios(usuarios)

    db.desconectar()

if __name__ == "__main__":
    main()