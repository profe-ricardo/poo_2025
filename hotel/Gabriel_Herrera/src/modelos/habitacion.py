from db.conexion import ConexionDB

class Habitacion:
    def __init__(self, numero, cant_personas, estado):
        self.numero = numero
        self.cant_personas = cant_personas
        self.estado = estado

    def guardar(self):
        db = ConexionDB()
        db.conectar()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO habitacion(numero, cant_personas, estado) VALUES (:n, :c, :e)",
            {"n": self.numero, "c": self.cant_personas, "e": self.estado}
        )
        db.commit()
        db.cerrar()
