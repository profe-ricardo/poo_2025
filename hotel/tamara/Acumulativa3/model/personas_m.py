from config.db_config import ConexionOracle

class ClienteModel:
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear(self, nombre: str, telefono: int, nacionalidad: str, habitacion: int) -> bool:

        cursor = self.db.obtener_cursor()
        consulta = "insert into clientes (nombre, telefono, nacionalidad, habitacion) values (:1, :2, :3, :4)"

        try:
            cursor.execute(consulta,  (nombre, telefono, nacionalidad, habitacion))
            self.db.connection.commit()
            print(f"[INFO]: Cliente '{nombre}' insertado correctamente.")

            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo insertar cliente → {e} ")

            return False
        finally:
            if cursor:
                cursor.close()
        
    def mostrar_todos(self) -> list:

        cursor = self.db.obtener_cursor()
        consulta = "select nombre, telefono, nacionalidad, habitacion from clientes"

        try:
            cursor.execute(consulta)
            datos = cursor.fetchall()
            print("[INFO]: Clientes obtenidos correctamente.")

            return datos
        except Exception as e:
            print(f"[ERROR]: Error al obtener clientes → {e}")
            return []

        finally:
            if cursor:
                cursor.close()
        


      
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

class RecepcionistaModel(UsuarioModel):
    def __init__(self, conexion: ConexionOracle):
        super().__init__(conexion)
        self.db = conexion
        
    def crear(self, nombre: str, telefono: int, ubicacion: str, conexion) -> bool:

        cursor = self.db.obtener_cursor()
        consulta = "insert into recepcionistas(nombre, telefono, ubicacion) values (:1, :2, :3)"

        try:
            cursor.execute(consulta, (nombre, telefono, ubicacion))
            self.db.connection.commit()
            print(f"[INFO]: Recepcionista '{nombre}' insertado correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo insertar -> {e}")
            return False
        
        finally:
            if cursor:
                cursor.close()

    def mostrar_todos(self) -> list:

        cursor = self.db.obtener_cursor()
        consulta = "select nombre, telefono, ubicacion from recepcionistas"

        try:
            cursor.execute(consulta)
            datos = cursor.fetchall()
            print("[INFO]: Recepcionistas obtenidos correctamente.")
            return datos
        
        except Exception as e:
            print(f"[ERROR: Error al obtener recepcionistas -> {e}]")
            return[]
        
        finally:
            if cursor:
                cursor.close()
        