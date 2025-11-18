from config.dbconfig import ConexionOracle

class InventarioModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def agregar_item(self, nombre: str, tipo: str, cantidad: int, precio_costo: float) -> bool:
        cursor = self.db.obtener_cursor()
        try:
            cursor.execute(
                "insert into inventario (nombre, tipo, cantidad, precio_costo) values (:1, :2, :3, :4)",
                (nombre, tipo, cantidad, precio_costo)
            )
            self.db.connection.commit()
            print(f"[INFO]: Ítem '{nombre}' agregado correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo agregar ítem -> {e}")
            return False
        finally:
            try: cursor.close()
            except Exception: pass

    def mostrar_items(self):
        cursor = self.db.obtener_cursor()
        try:
            cursor.execute("select id, nombre, tipo, cantidad, precio_costo from inventario")
            return cursor.fetchall()
        except Exception as e:
            print(f"[ERROR]: No se pudieron obtener ítems -> {e}")
            return []
        finally:
            try: cursor.close()
            except Exception: pass
