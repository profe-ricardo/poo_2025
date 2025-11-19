# from view.Personas_V import chef

# def main():
#     print("Aplicacion Inicial")

#     chefcito = chef("remi", 1 , "Paris", ["Rata"])
    
#     print(chefcito.ver_pedidos())

#     print(chefcito.recibir_pedido(["Bebida","Completo", "Pie de limon"]))

#     print(chefcito.ver_pedidos())

# main()
import bcrypt

from config.db_confing import ConexionOracle

def conectarBD():
    db = ConexionOracle("system", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    return db

def main():
    db = conectarBD()

    print("Inicio de sesion, Ingrese sus credenciales\n")
    
    id_u = int(input("ingrese ID\n"))
    Usuario = str(input("Ingrese su nombre de usuario\n"))
    Clave = str(input("Ingrese su contraseña\n"))
    Clave = bytes(Clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(Clave, salt)

    print(clave_encriptada)

    cursor = db.obtener_cursor()

    consulta = "select clave from usuario where nombre_usuario = :1"
    cursor.execute(consulta, (Usuario), str(clave_encriptada))
    db.connection.commit()

    Usuario = str(input("Ingrese su nombre de usuario\n"))
    Clave = str(input("Ingrese su contraseña\n"))
    Clave = bytes(Clave, encoding="utf-8")

    if Clave == clave_encriptada:
        print("Clave valida")
    else:
        print("Clave invalida")


    

    db.desconectar()

if __name__ == "__main__":
    main()