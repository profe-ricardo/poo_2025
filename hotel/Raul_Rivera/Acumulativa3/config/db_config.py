import oracledb

class ConexionOracle:
    """
        Clase para conexion de BD.
    """
    def __init__(self, usuario: str, password: str, url: str):
        self.usuario = usuario
        self.password = password
        self.url = url
        self.connection = None

    def conectar(self):
        """
            Genera la conexión con la bd según datos recibidos.\n
        """
        try:
            self.connection = oracledb.connect(
                user=self.usuario,
                password=self.password,
                dsn=self.url
            )
            print("[INFO]: Conectado a BD correctamente.")
            
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"[ERROR]: No se pudo conectar a BD → {error.message}")

    def desconectar(self):
        """
            Si es que hay una conexión activa, la finaliza.
        """
        if self.connection:
            self.connection.close()
            print("[INFO]: Conexión a BD cerrada correctamente.")

    def obtener_cursor(self):
        """
            Genera el cursor para BD.
        """
        if not self.connection:
            self.conectar()

        return self.connection.cursor()
    # def crear_tablas(self):
    #     """
    #     Crea las tablas necesarias si no existen.
    #     """
    #     cursor = self.connection.cursor()
    #     try:
    #         # Tabla usuarios
    #         cursor.execute("""
    #             BEGIN
    #                 EXECUTE IMMEDIATE 'CREATE TABLE usuarios (
    #                     nombre VARCHAR2(100),
    #                     telefono NUMBER
    #                 )';
    #             EXCEPTION
    #                 WHEN OTHERS THEN
    #                     IF SQLCODE = -955 THEN NULL; -- tabla ya existe
    #                     ELSE RAISE;
    #                     END IF;
    #             END;
    #         """)

    #         # Tabla habitaciones
    #         cursor.execute("""
    #             BEGIN
    #                 EXECUTE IMMEDIATE 'CREATE TABLE habitaciones (
    #                     numero NUMBER PRIMARY KEY,
    #                     cantidad_personas NUMBER,
    #                     ubicacion VARCHAR2(100),
    #                     estado NUMBER(1)
    #                 )';
    #             EXCEPTION
    #                 WHEN OTHERS THEN
    #                     IF SQLCODE = -955 THEN NULL;
    #                     ELSE RAISE;
    #                     END IF;
    #             END;
    #         """)

    #         # Tabla boletas
    #         cursor.execute("""
    #             BEGIN
    #                 EXECUTE IMMEDIATE 'CREATE TABLE boletas (
    #                     folio NUMBER PRIMARY KEY,
    #                     cliente_nombre VARCHAR2(100),
    #                     usuario_nombre VARCHAR2(100)
    #                 )';
    #             EXCEPTION
    #                 WHEN OTHERS THEN
    #                     IF SQLCODE = -955 THEN NULL;
    #                     ELSE RAISE;
    #                     END IF;
    #             END;
    #         """)

    #         # Tabla feedback
    #         cursor.execute("""
    #             BEGIN
    #                 EXECUTE IMMEDIATE 'CREATE TABLE feedback (
    #                     cliente_nombre VARCHAR2(100),
    #                     mensaje VARCHAR2(500)
    #                 )';
    #             EXCEPTION
    #                 WHEN OTHERS THEN
    #                     IF SQLCODE = -955 THEN NULL;
    #                     ELSE RAISE;
    #                     END IF;
    #             END;
    #         """)

    #         self.connection.commit()
    #         print("[INFO]: Tablas verificadas/creadas correctamente.")
    #     except Exception as e:
    #         print(f"[ERROR]: No se pudieron crear las tablas → {e}")
    #     finally:
    #         cursor.close()