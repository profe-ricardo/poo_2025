from db.conexion import ConexionDB

class Cliente:
    def __init__(self, nombre, telefono, nacionalidad, habitacion):
        self.nombre = nombre
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.habitacion = habitacion

    def guardar(self):
        db = ConexionDB()
        db.conectar()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO cliente(nombre, telefono, nacionalidad, habitacion) VALUES (:n, :t, :na, :h)",
            {"n": self.nombre, "t": self.telefono, "na": self.nacionalidad, "h": self.habitacion}
        )
        db.commit()
        db.cerrar()
