import oracledb

class ConexionOracle:
    """
    Clase encargada de gestionar la conexión a la base de datos Oracle.
    """

    def __init__(self, usuario: str, password: str, url: str):
        self.usuario = usuario
        self.password = password
        self.url = url
        self.connection = None

    def conectar(self):
        """
        Intenta establecer la conexión y la retorna.
        """
        try:
            self.connection = oracledb.connect(
                user=self.usuario,
                password=self.password,
                dsn=self.url
            )
            print("[INFO]: Conectado a BD correctamente.")
            return self.connection  # 🔹 IMPORTANTE
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"[ERROR]: No se pudo conectar a BD -> {error.message}")
            self.connection = None
            return None

    def desconectar(self):
        """
        Cierra la conexión activa si existe.
        """
        if self.connection:
            try:
                self.connection.close()
                print("[INFO]: Conexión a BD cerrada correctamente.")
            except Exception as e:
                print(f"[WARN]: Error al cerrar conexión -> {e}")
            finally:
                self.connection = None

    def obtener_cursor(self):
        """
        Retorna un cursor activo; si no hay conexión, intenta crearla.
        """
        if not self.connection:
            self.conectar()
        if self.connection:
            return self.connection.cursor()
        else:
            raise ConnectionError("No se pudo obtener cursor: sin conexión activa.")
