from config.db_config import ConexionOracle
#from hotel.Luis_carrasco.model.personas_m import UsuarioModel
#from hotel.Luis_carrasco.controller.personas_c import UsuarioController
#from hotel.Luis_carrasco.view.personas_v import UsuarioView

def conectarBD():
    db = ConexionOracle("system", "Inacap2025", "localhost:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarBD()
    #modelo = UsuarioModel(db)
    #controlador = UsuarioController(modelo)
    #vista = UsuarioView()

    print("Aplicacion iniciada")

    # ingreso = controlador.registrar_usuario('system', "Ina2025", "Localhost:1521/xe" )

    #if ingreso:
 #       usuarios = controlador.listar_usuarios()
  #      vista.mostrar_usuarios(usuarios)

    db.desconectar()

if __name__ == "__main__":
    main()


