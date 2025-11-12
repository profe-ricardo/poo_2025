# from personas import personalAseo, manager, cliente, chef, recepcionista
# from objetos import comida, habitacion,inventarios, boleta

from config.db_config import ConexionOracle

def conectarBD():
    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar() 

    return db

def main():
    db = conectarBD()

    print("Aplicacion iniciada")

    db.desconectar()

if __name__ == "__main__":
    main()