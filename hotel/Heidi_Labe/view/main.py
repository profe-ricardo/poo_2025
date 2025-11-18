

from hotel.Heidi_Labe.config.db_config import ConexionOracle
from hotel.Heidi_Labe.config.db_config import usuarioModel
from hotel.Heidi_Labe.config.db_config import UsuarioController
from hotel.Heidi_Labe.config.db_config import UsuarioView

def conectarBD():
    db = ConexionOracle("system","Ina.2025","localhost:1521/xe")
    db.conectar()

    return db

def main():                                          
    db = conectarBD()

    print("Aplicacion iniciada")

    db.desconectar()

    if __name__ == "__main__":
        main()