from db.conexion import ConexionDB

class Usuario:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def guardar(self):
        db = ConexionDB()
        db.conectar()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO usuario(nombre, telefono) VALUES (:n, :t)",
            {"n": self.nombre, "t": self.telefono}
        )
        db.commit()
        db.cerrar()
