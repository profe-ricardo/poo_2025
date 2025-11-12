from config.db_config import ConexionOracle
from model.objetos_m import habitacionModel

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



class clienteModel():

    def __init__(self,nombre:str, telefono:int,nacionalidad:str, habitacion:habitacionModel):
        super().__init__(habitacion)
        self.nombre=nombre
        self.telefono=telefono
        self.nacionalidad=nacionalidad
        self.habitacion=habitacion
        

class recepcionistaModel(UsuarioModel):

    def __init__(self, nombre:str, telefono:int, ubicacion:str, conexion:ConexionOracle):
        super().__init__(conexion)
        self.nombre=nombre
        self.telefono=telefono
        self.ubicacion=ubicacion
        self.conexion=UsuarioModel.conexion


