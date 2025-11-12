from config.dbconfig import ConexionOracle

class HabitacionModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear_habitacion(self, numero: int, capacidad: int, estado: str = "disponible") -> bool:
        # 🔹 Verificar conexión y cursor
        if not self.db.connection:
            self.db.conectar()
        if not self.db.connection:
            print("[ERROR]: No se pudo establecer conexión con la base de datos.")
            return False

        cursor = self.db.obtener_cursor()
        if cursor is None:
            print("[ERROR]: No se pudo obtener cursor.")
            return False

        try:
            consulta_validacion = "SELECT 1 FROM habitaciones WHERE numero = :1"
            cursor.execute(consulta_validacion, (numero,))
            if cursor.fetchone():
                print(f"[ERROR]: La habitación {numero} ya existe.")
                return False

            consulta_insert = "INSERT INTO habitaciones (numero, capacidad, estado) VALUES (:1, :2, :3)"
            cursor.execute(consulta_insert, (numero, capacidad, estado))
            self.db.connection.commit()
            print(f"[INFO]: Habitación {numero} creada correctamente.")
            return True

        except Exception as e:
            print(f"[ERROR]: Error al crear habitación -> {e}")
            if self.db.connection:
                self.db.connection.rollback()
            return False

        finally:
            try:
                cursor.close()
            except Exception:
                pass

    def mostrar_habitaciones(self) -> list:
        if not self.db.connection:
            self.db.conectar()
        if not self.db.connection:
            print("[ERROR]: No se pudo establecer conexión con la base de datos.")
            return []

        cursor = self.db.obtener_cursor()
        if cursor is None:
            print("[ERROR]: No se pudo obtener cursor.")
            return []

        try:
            consulta = "SELECT numero, capacidad, estado FROM habitaciones"
            cursor.execute(consulta)
            datos = cursor.fetchall()
            return datos or []
        except Exception as e:
            print(f"[ERROR]: Error al obtener habitaciones -> {e}")
            return []
        finally:
            try:
                cursor.close()
            except Exception:
                pass

    def actualizar_estado(self, numero: int, nuevo_estado: str) -> bool:
        if not self.db.connection:
            self.db.conectar()
        if not self.db.connection:
            print("[ERROR]: No se pudo establecer conexión con la base de datos.")
            return False

        cursor = self.db.obtener_cursor()
        if cursor is None:
            print("[ERROR]: No se pudo obtener cursor.")
            return False

        try:
            consulta_validacion = "SELECT 1 FROM habitaciones WHERE numero = :1"
            cursor.execute(consulta_validacion, (numero,))
            if cursor.fetchone():
                consulta_update = "UPDATE habitaciones SET estado = :1 WHERE numero = :2"
                cursor.execute(consulta_update, (nuevo_estado, numero))
                self.db.connection.commit()
                print(f"[INFO]: Habitación {numero} actualizada a {nuevo_estado}.")
                return True
            else:
                print(f"[ERROR]: La habitación {numero} no existe.")
                return False

        except Exception as e:
            print(f"[ERROR]: Error al actualizar habitación -> {e}")
            if self.db.connection:
                self.db.connection.rollback()
            return False

        finally:
            try:
                cursor.close()
            except Exception:
                pass
