from config.db_config import ConexionOracle
from model.personas_m import UsuarioModel
from controller.personas_c import UsuarioController
from view.personas_v import UsuarioView
def conectarBD():
    """
        Realiza conexión a BD utilizando función predefinida.
    """
    db = ConexionOracle("System", "Ina.2025", "localhost:1521/xe")
    db.conectar()
    # if db.connection:
    #     db.crear_tablas()  # asegura que las tablas estén listas
    # return db
    if not db.connection:
        print("[ERROR]: No se pudo establecer conexión con la BD.")
        return None

    return db

def main():
    """
        Genera registro de usuario en BD conectada.
        Debe existir tabla 'usuarios' con las columnas 'nombre' y 'telefono'.
        También devuelve una lista de los usuarios registrados.
    """
    db = conectarBD()
    if not db:
        return  # termina si no hay conexión

    modelo = UsuarioModel(db)
    controlador = UsuarioController(modelo)

    print("\n[INFO]: Aplicación iniciada")

    ingreso = controlador.registrar_usuario('Ricardo', 912345678)

    if ingreso:
        usuarios = controlador.listar_usuarios()
        UsuarioView.mostrar_usuarios(usuarios)

    db.desconectar()

if __name__ == "__main__":
    main()
