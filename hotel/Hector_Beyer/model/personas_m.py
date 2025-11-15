from hotel.Hector_Beyer.config.db_config import ConexionOracle

class UsuarioModel:
    """
        Modelo del usuario.\n
        Métodos de creación y muestra de usuarios, realizando conexión con BD.
    """
    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear(self, nombre: str, telefono: int) -> bool:
        """
            Recibe nombre y telefono de usuario a registrar.\n
            Genera cursor de manejo de BD para ejecución de consulta.\n
            returns Boolean
        """
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
        """
            Genera cursor de manejo de BD para ejecución de consulta.\n
            returns lista de usuarios registrados en BD.
        """
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

class ClienteModel:

    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear(self, nombre: str, telefono: int, nacionalidad:str, habitacion:int) -> bool:

        cursor = self.db.obtener_cursor()
        consulta = "insert into clientes (nombre, telefono, nacionalidad, habitacion) values (:1, :2, :3, :4)"

        try:
            cursor.execute(consulta, (nombre, telefono, nacionalidad, habitacion))
            self.db.connection.commit()
            print(f"[INFO]: Cliente '{nombre}' insertado correctamente.")

            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo insertar cliente → {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_todos(self) -> list:
        """
            Genera cursor de manejo de BD para ejecución de consulta.\n
            returns lista de clientes registrados en BD.
        """
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

class RecepcionistaModel:

    def __init__(self, conexion: ConexionOracle):
        self.db = conexion

    def crear(self, nombre: str, telefono: int, nacionalidad:str, habitacion:int) -> bool:

        cursor = self.db.obtener_cursor()
        consulta = "insert into clientes (nombre, telefono, nacionalidad, habitacion) values (:1, :2, :3, :4)"

        try:
            cursor.execute(consulta, (nombre, telefono, nacionalidad, habitacion))
            self.db.connection.commit()
            print(f"[INFO]: Cliente '{nombre}' insertado correctamente.")

            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo insertar cliente → {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_todos(self) -> list:
        """
            Genera cursor de manejo de BD para ejecución de consulta.\n
            returns lista de clientes registrados en BD.
        """
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