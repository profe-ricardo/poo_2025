from config.db_config import ConexionOracle

class chef():
    def __init__(self, nombre: str, id: int, locacion: str, pedidos: list ):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
        self.pedidos = pedidos

    def tomar_pedido(self, pedido: list) -> bool:
        for p in pedido:
            self.pedidos.append(p)
        
        return True
    
    def ver_pedidos(self) -> list:
        return self.pedidos
    
class clienteModel():
    def __init__(self, nombre: str, telefono: int, nacionalidad: str, habitacion: int):
        self.nombre = nombre
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.habitacion = habitacion

    def guardar_item(self, nombre: str, telefono: int, nacionalidad: str, habitacion: int) -> bool:
        
        cursor = self.conexion.obtener_cursor()

        try:
            validacion = "select * from clientes where nombre = :1"
            cursor.execute(validacion, (nombre,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: {nombre} ya esta asignado")
                return False
            else:
                consulta_insert = "insert into clientes(nombre, telefono, nacionalidad, habitacion) values (:1, :2, :3, :4)"
                cursor.execute(consulta_insert, (nombre, telefono, nacionalidad, habitacion))
                self.conexion.connection.commit()
                print(f"[INFO]: {nombre} agregado correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al ingresar a {nombre} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_item(self, nombre: int, *datos: tuple) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from clientes where nombre = :1"
            cursor.execute(validacion, (nombre,))
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update clientes set nombre = :1, telefono = :2, nacionalidad = :3, habitacion = :4 where nombre = :4"
                    cursor.execute(consulta_update,(nombre,datos[0], datos[1], datos[2], datos [3] nombre,))
                    print(f"[INFO]: {nombre} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos para {nombre}")

                    return False
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla Boletas")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar a {nombre} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:

        cursor = self.conexion.obtener_cursor()
        
        try:
            consulta = "select nombre, telefono, nacionalidad, habitacion from Boletas"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para clientes")
                return []
        except Exception as e:
            print(f"[ERROR]: error al obtener items desde BD -> {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
    def eliminar_item(self, nombre: str) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from clientes where numero = :1"
            cursor.execute(validacion,(nombre,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from clientes where nombre = :5"
                cursor.execute(consulta_delete, (nombre,))
                self.conexion.connection.commit()
                print(f"[INFO]:cliente {nombre} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]:cliente {nombre} no existe en la tabla Boletas")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar cliente {nombre} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()
    
        
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

class recepcionistaModel(UsuarioModel):
    def __init__(self,nombre: str, telefono:int, ubicacion: str):
        super().__init__(nombre, telefono, ubicacion)

    def guardar_item(self, nombre: str, telefono: int, ubicacion: str) -> bool:
        
        cursor = self.conexion.obtener_cursor()

        try:
            validacion = "select * from recepcionistas where nombre = :1"
            cursor.execute(validacion, (nombre,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: {nombre} ya esta asignado")
                return False
            else:
                consulta_insert = "insert into recepcionistas(nombre, telefono, ubicacion) values (:1, :2, :3)"
                cursor.execute(consulta_insert, (nombre, telefono, ubicacion))
                self.conexion.connection.commit()
                print(f"[INFO]: {nombre} agregado correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al ingresar a {nombre} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_item(self, nombre: int, *datos: tuple) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from recepcionistas where nombre = :1"
            cursor.execute(validacion, (nombre,))
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update recepcionistas set nombre = :1, telefono = :2, ubicacion = :3 where nombre = :4"
                    cursor.execute(consulta_update,(nombre,datos[0], datos[1], datos[2], nombre,))
                    print(f"[INFO]: {nombre} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos para {nombre}")

                    return False
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla recepcionistas")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar a {nombre} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:

        cursor = self.conexion.obtener_cursor()
        
        try:
            consulta = "select nombre, telefono, ubicacion from recepcionistas"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para recepcionistas")
                return []
        except Exception as e:
            print(f"[ERROR]: error al obtener items desde BD -> {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
    def eliminar_item(self, nombre: str) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from clientes where numero = :1"
            cursor.execute(validacion,(nombre,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from clientes where nombre = :5"
                cursor.execute(consulta_delete, (nombre,))
                self.conexion.connection.commit()
                print(f"[INFO]:recepcionista {nombre} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]:recepcionista {nombre} no existe en la tabla recepcionistas")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar recepcionista {nombre} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()
        