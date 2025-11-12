class BaseModel:
    def __init__(self, conexion):
        self.db = conexion

    def ejecutar_consulta(self, query: str, params: tuple = ()):
        cursor = self.db.obtener_cursor()
        try:
            cursor.execute(query, params)
            self.db.connection.commit()
            return True
        except Exception as e:
            print(f"[ERROR]: {e}")
            return False
        finally:
            try:
                cursor.close()
            except Exception:
                pass
