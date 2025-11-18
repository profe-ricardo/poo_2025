from config.dbconfig import ConexionOracle

class ClienteModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear_cliente(self, nombre: str, telefono: str, nacionalidad: str, habitacion_numero: int | None = None) -> int | None:
        # 🔹 Verificación previa: asegurar conexión y cursor válido
        if not self.db.connection:
            self.db.conectar()
        if not self.db.connection:
            print("[ERROR]: No se pudo establecer conexión con la base de datos.")
            return None

        cursor = self.db.obtener_cursor()
        if cursor is None:
            print("[ERROR]: No se pudo obtener cursor.")
            return None

        try:
            # Inserta el cliente
            cursor.execute(
                "INSERT INTO clientes (nombre, telefono, nacionalidad, habitacion_numero) VALUES (:1, :2, :3, :4)",
                (nombre, telefono, nacionalidad, habitacion_numero)
            )
            self.db.connection.commit()

            # Obtener ID más reciente
            cursor2 = self.db.connection.cursor()
            cursor2.execute("SELECT id FROM clientes ORDER BY id DESC FETCH FIRST 1 ROWS ONLY")
            row = cursor2.fetchone()
            new_id = row[0] if row else None

            cursor2.close()
            print(f"[INFO]: Cliente {nombre} creado con id {new_id}")
            return new_id

        except Exception as e:
            print(f"[ERROR]: Error al crear cliente -> {e}")
            if self.db.connection:
                self.db.connection.rollback()
            return None

        finally:
            try:
                cursor.close()
            except Exception:
                pass

    def mostrar_clientes(self) -> list:
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
            consulta = "SELECT id, nombre, telefono, nacionalidad, habitacion_numero FROM clientes"
            cursor.execute(consulta)
            datos = cursor.fetchall()
            return datos or []
        except Exception as e:
            print(f"[ERROR]: Error al obtener clientes -> {e}")
            return []
        finally:
            try:
                cursor.close()
            except Exception:
                pass
