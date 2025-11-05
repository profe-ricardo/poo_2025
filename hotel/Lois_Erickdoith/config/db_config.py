import oracledb

class ConexionOracle:
    def __init__(self, usuario: str, password: str, url: str):
        self.usuario = usuario
        self.password = password
        self.url = url
        self.connection = None

    def conectar(self):
        try:
            self.connection = oracledb.connect(
                user=self.usuario,
                password=self.password,
                dsn=self.url
            )
            print("[INFO]: Conectado a BD correctamente. Insecto..!")
            
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"[ERROR]: Insecto..! No se pudo conectar a BD → {error.message}")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("[INFO]: Conexión a BD cerrada correctamente. Insecto..!")

    def obtener_cursor(self):
        if not self.connection:
            self.conectar()

        return self.connection.cursor()