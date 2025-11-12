from config.db_config import ConexionOracle
from model.personas_m import UsuarioModel
from controller.personas_c import UsuarioController
from vista.personas_v import UsuarioView

def conectarBD():

    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    return

def main():

    db = conectarBD()
    modelo = UsuarioModel(db)
    controlador = UsuarioController(modelo)
    vista = UsuarioView()

    print("Aplicacion Iniciada")

    ingreso = controlador.registrar_usuario('Tamara', 931737681)

    if ingreso:
        usuarios = controlador.listar_usuarios()
        vista.mostrar_usuarios(usuarios)
    
    db.desconectar()

if __name__ == "__main__":
    main()