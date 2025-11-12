from acumulativa3.config.db_config import ConexionOracle

class UsuarioModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear(self, nombre: str, telefono: int) -> bool:

        cursor = self.db.obtener_cursor()
        consulta = "insert into usuarios (nombre, telefono) values (:1, :2)"

        try:
            cursor.execute(consulta, (nombre, telefono))
            self.db.connection.commit()
            print(f"[INFO]: Usuario '{nombre}' insertado correctamente.")

            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo insertar usuario → {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_todos(self) -> list:

        cursor = self.db.obtener_cursor()
        consulta = "select nombre, telefono from usuarios"

        try:
            cursor.execute(consulta)
            datos = cursor.fetchall()
            print("[INFO]: Usuarios obtenidos correctamente.")

            return datos
        except Exception as e:
            print(f"[ERROR]: Error al obtener usuarios → {e}")

            return []
        finally:
            if cursor:
                cursor.close()

class recepcionista(UsuarioModel):
    def __init__(self, nombre: str, telefono: int, ubicacion: str, conexion):
        super().__init__(conexion)  