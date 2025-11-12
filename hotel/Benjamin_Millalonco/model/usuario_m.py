from config.dbconfig import ConexionOracle

class UsuarioModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear_usuario(self, nombre: str, telefono: str, ubicacion: str) -> int | None:
        cursor = self.db.obtener_cursor()
        try:
            cursor.execute(
                "insert into usuarios (nombre, telefono, ubicacion) values (:1, :2, :3)",
                (nombre, telefono, ubicacion)
            )
            self.db.connection.commit()
            cursor2 = self.db.connection.cursor()
            cursor2.execute("select id from usuarios order by id desc fetch first 1 rows only")
            row = cursor2.fetchone()
            return row[0] if row else None
        except Exception as e:
            print(f"[ERROR]: No se pudo crear usuario -> {e}")
            return None
        finally:
            try: cursor.close()
            except Exception: pass
