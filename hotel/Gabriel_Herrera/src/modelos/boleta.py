from db.conexion import ConexionDB

class Boleta:
    def __init__(self, folio, cliente, usuario):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario

    def guardar(self):
        db = ConexionDB()
        db.conectar()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO boleta(folio, cliente, usuario) VALUES (:f, :c, :u)",
            {"f": self.folio, "c": self.cliente, "u": self.usuario}
        )
        db.commit()
        db.cerrar()
