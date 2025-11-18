from config.dbconfig import ConexionOracle

class BoletaModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear_boleta(self, cliente_id: int, usuario_id: int) -> bool:
        cursor = self.db.obtener_cursor()
        try:
            cursor.execute(
                "insert into boletas (cliente_id, usuario_id) values (:1, :2)",
                (cliente_id, usuario_id)
            )
            self.db.connection.commit()
            print(f"[INFO]: Boleta creada correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: Error al crear boleta -> {e}")
            return False
        finally:
            try: cursor.close()
            except Exception: pass
