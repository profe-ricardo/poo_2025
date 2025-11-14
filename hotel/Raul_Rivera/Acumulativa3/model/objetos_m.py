from config.db_config import ConexionOracle

class InventarioModel:
    """
        Modelo de inventario.
        Contiene métodos para creación, edición y muestra de inventario, realizando conexión con BD.
    """
    def __init__(self, nombre: str, tipo: str, cantidad: int, precio_costo: float, conexion: ConexionOracle):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo
        self.db = conexion

    def guardar_item(self, nombre, tipo, cantidad, precio_costo) -> bool:
        cursor = self.db.obtener_cursor()
        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))
            if cursor.fetchall():
                print(f"[ERROR]: Ya existe un ítem con el nombre {nombre}")
                return False
            consulta_insert = "insert into inventario (nombre, tipo, cantidad, precio_costo) values (:1, :2, :3, :4)"
            cursor.execute(consulta_insert, (nombre, tipo, cantidad, precio_costo))
            self.db.connection.commit()
            print(f"[INFO]: {nombre} guardado correctamente")
            return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar {nombre} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def editar_item(self, nombre: str, *datos: tuple) -> bool:
        cursor = self.db.obtener_cursor()
        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))
            if cursor.fetchall():
                if datos:
                    consulta_update = "update inventario set nombre = :1, tipo = :2, cantidad = :3, precio_costo = :4 where nombre = :5"
                    cursor.execute(consulta_update, (nombre, datos[0], datos[1], datos[2], nombre))
                    self.db.connection.commit()
                    print(f"[INFO]: {nombre} editado correctamente")
                    return True
                print(f"[ERROR]: Sin datos ingresados para {nombre}")
                return False
            print(f"[ERROR]: {nombre} no existe en la tabla de inventario.")
            return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {nombre} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:
        cursor = self.db.obtener_cursor()
        try:
            consulta = "select nombre, tipo, cantidad, precio_costo from inventario"
            cursor.execute(consulta)
            datos = cursor.fetchall()
            if datos:
                return datos
            print("[INFO]: Sin datos encontrados para inventario.")
            return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_item(self, nombre: str) -> bool:
        cursor = self.db.obtener_cursor()
        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))
            if cursor.fetchall():
                consulta_delete = "delete from inventario where nombre = :1"
                cursor.execute(consulta_delete, (nombre,))
                self.db.connection.commit()
                print(f"[INFO]: {nombre} eliminado correctamente")
                return True
            print(f"[ERROR]: {nombre} no existe en la tabla de inventario.")
            return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {nombre} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()


class boletaModel:
    def __init__(self, folio: int, cliente, usuario):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario

    def calcular_total(self, cargos: list[float]) -> float:
        return sum(cargos)

    def imprimir_boleta(self):
        print(f"Folio: {self.folio}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Usuario: {self.usuario.nombre}")


class habitacionModel:
    def __init__(self, numero: int, cantidad_personas: int, ubicacion: str, estado: bool, conexion: ConexionOracle):
        self.numero = numero
        self.cantidad_personas = cantidad_personas
        self.ubicacion = ubicacion
        self.estado = estado
        self.conexion = conexion

    def cambiar_estado(self, nuevo_estado: bool):
        self.estado = nuevo_estado

    def es_disponible(self) -> bool:
        return self.estado
