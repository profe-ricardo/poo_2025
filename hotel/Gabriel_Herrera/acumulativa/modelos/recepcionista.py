from modelos.usuario import Usuario
from db.conexion import ConexionDB

class Recepcionista(Usuario):
    def __init__(self, nombre, telefono, ubicacion):
        super().__init__(nombre, telefono)
        self.ubicacion = ubicacion

    def guardar(self):
        super().guardar()
        db = ConexionDB()
        db.conectar()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO recepcionista(id, ubicacion) VALUES ((SELECT MAX(id) FROM usuario), :u)",
            {"u": self.ubicacion}
        )
        db.commit()
        db.cerrar()
