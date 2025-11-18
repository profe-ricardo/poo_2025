from db.conexion import ConexionDB

class Inventario:
    def __init__(self, nombre, tipo, cantidad, precio_costo):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo

    def guardar(self):
        db = ConexionDB()
        db.conectar()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO inventario(nombre, tipo, cantidad, precio_costo) VALUES (:n, :t, :c, :p)",
            {"n": self.nombre, "t": self.tipo, "c": self.cantidad, "p": self.precio_costo}
        )
        db.commit()
        db.cerrar()
