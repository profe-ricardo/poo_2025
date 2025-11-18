import oracledb

class Conexionoracle:
    def __init__(self,usuario: str, password: str, url: str):
        self.usuario = usuario
        self.password = password
        self.url = url
        self.connection = None

    def conectar(self):
        try:
            self.connection = oracledb.connect(
                user = self.usuario,
                password = self.password,
                dsn = self.url
            )
            print ("[INFO]: Conectado a BD correctamente")
        except oracledb.DatabaseError as e:
             error, = e.args
             print(f"[ERROR]: No se pudo conectar a BD -> {error.message}")  

    def desconectar(self):
         if self.connection:
              self.connection.close()
              print(f"[INFO]: conexion a BD cerrada correctamente")

    def obtener_cursor(self):
            if not self.connection:
                self.conectar()

            return self.connection.cursor()