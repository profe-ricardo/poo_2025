import oracledb

class ConexionDB:
    def __init__(self):
        self.conn = None

    def conectar(self):
        try:
            self.conn = oracledb.connect(
                user="USUARIO",
                password="CLAVE",
                dsn="localhost/XEPDB1"
            )
            print("Conexión exitosa a Oracle")
        except Exception as e:
            print("Error al conectar a Oracle:", e)

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def cerrar(self):
        if self.conn:
            self.conn.close()
