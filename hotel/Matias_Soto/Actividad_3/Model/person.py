from config.db_confing import Conexionoracle

class clientMoldel:
    def __init__(self, Name: str, Phone: int, Location:str, Room: str, connection = Conexionoracle):
       self.Name = Name
       self.Phone = Phone
       self.Location = Location
       self.Room = Room
       self.connection = connection

    def register_client(self, Name: str, Phone: int, Location: str, Room: str) -> bool:

        cursor = self.connection.get_cursor()

        try:
            Client = "inset into clients (Name, Phone, Location, Room) values (:1, :2, :3, :4)"
            cursor.execute(Client, (Name, Phone, Location, Room))
            self.connection.connection.commit()

            if cursor.fetchall() == 0:

class UsuarioModel:
    """
        Modelo del usuario.\n
        Métodos de creación y muestra de usuarios, realizando conexión con BD.
    """
    def __init__(self, conexion: Conexionoracle):
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

class Reception(UsuarioModel):
    def __init__(self, Name: str, Phone: int, location: str, conexion):
        super().__init__(conexion)

