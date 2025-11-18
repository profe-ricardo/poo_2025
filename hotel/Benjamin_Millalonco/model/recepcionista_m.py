from config.dbconfig import ConexionOracle
from model.usuario_m import UsuarioModel

class RecepcionistaModel(UsuarioModel):
    def __init__(self, conexion: ConexionOracle):
        super().__init__(conexion)

    def registrar_recepcionista(self, nombre: str, telefono: str, ubicacion: str) -> bool:
        id_usuario = self.crear_usuario(nombre, telefono, ubicacion)
        if not id_usuario:
            return False
        cursor = self.db.obtener_cursor()
        try:
            cursor.execute("insert into recepcionistas (id) values (:1)", (id_usuario,))
            self.db.connection.commit()
            print(f"[INFO]: Recepcionista '{nombre}' registrado correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo registrar recepcionista -> {e}")
            return False
        finally:
            try: cursor.close()
            except Exception: pass
