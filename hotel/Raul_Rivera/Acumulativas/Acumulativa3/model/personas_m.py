from config.db_config import ConexionOracle
from model.objetos_m import habitacionModel

class UsuarioModel:
    """
        Modelo del usuario.
        Métodos de creación y muestra de usuarios, realizando conexión con BD.
    """
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


class clienteModel:
    """
        Modelo del cliente.
        Contiene datos personales y la habitación asignada.
    """
    def __init__(self, nombre: str, telefono: int, nacionalidad: str, habitacion: 'habitacionModel'):
        self.nombre = nombre
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.habitacion = habitacion



class recepcionistaModel(UsuarioModel):
    """
        Modelo del recepcionista.
        Contiene métodos específicos para la gestión de clientes y habitaciones.
    """
    def __init__(self, nombre: str, telefono: int, ubicacion: str, conexion: ConexionOracle):
        super().__init__(conexion)
        self.nombre = nombre
        self.telefono = telefono
        self.ubicacion = ubicacion
        
    def guardar(self) -> bool:
        cursor = self.db.obtener_cursor()
        try:
            consulta = "INSERT INTO recepcionistas (nombre, telefono, ubicacion) VALUES (:1, :2, :3)"
            cursor.execute(consulta, (self.nombre, self.telefono, self.ubicacion))
            self.db.connection.commit()
            print(f"[INFO]: Recepcionista '{self.nombre}' guardado correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar recepcionista → {e}")
            return False
        finally:
            cursor.close()

    def ver_habitacion_disponible(self, habitacion: 'habitacionModel') -> bool:
        cursor = self.db.obtener_cursor()
        consulta = "select estado from habitaciones where numero = :1"
        try:
            cursor.execute(consulta, (habitacion.numero,))
            resultado = cursor.fetchone()
            if resultado:
                disponible = bool(resultado[0])
                estado = "disponible" if disponible else "ocupada"
                print(f"[INFO]: Habitación {habitacion.numero} está {estado}.")
                return disponible
            print(f"[ERROR]: Habitación {habitacion.numero} no encontrada.")
            return False
        except Exception as e:
            print(f"[ERROR]: No se pudo verificar disponibilidad → {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def reservar_habitacion(self, cliente: clienteModel) -> bool:
        cursor = self.db.obtener_cursor()
        consulta = "update habitaciones set estado = :1 where numero = :2"
        try:
            cursor.execute(consulta, (False, cliente.habitacion.numero))
            self.db.connection.commit()
            print(f"[INFO]: Habitación {cliente.habitacion.numero} asignada a {cliente.nombre}.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo asignar habitación → {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def generar_boleta(self, folio: int, cliente: clienteModel) -> bool:
        cursor = self.db.obtener_cursor()
        consulta = "insert into boletas (folio, cliente_nombre, usuario_nombre) values (:1, :2, :3)"
        try:
            cursor.execute(consulta, (folio, cliente.nombre, self.nombre))
            self.db.connection.commit()
            print(f"[INFO]: Boleta {folio} generada para cliente {cliente.nombre}.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo generar boleta → {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def aceptar_comentarios_cliente(self, cliente: clienteModel, mensaje: str) -> bool:
        cursor = self.db.obtener_cursor()
        consulta = "insert into feedback (cliente_nombre, mensaje) values (:1, :2)"
        try:
            cursor.execute(consulta, (cliente.nombre, mensaje))
            self.db.connection.commit()
            print(f"[INFO]: Feedback de {cliente.nombre} registrado correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo registrar feedback → {e}")
            return False
        finally:
            if cursor:
                cursor.close()
