from hotel.profe_ricardo.config.db_config import ConexionOracle

class InventarioModel:
    """
        Modelo de inventario.\n
        Contiene métodos para creación, edición y muestra de usuarios, realizando conexión con BD.
    """
    def __init__(self, nombre: str, tipo: str, cantidad: int, precio_costo: float,  conexion: ConexionOracle):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo
        self.db = conexion

    def guardar_item(self, nombre, tipo, cantidad, precio_costo) -> bool:
        """
            Guarda el item actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """

        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con el nombre {nombre}")

                return False
            else:
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
        """
            Edita el item indicado solo si existe en la BD.\n
            Si es que no existe, lanzará el mensaje correspondiente.\n

            params
            - nombre : nombre del item a editar
            - datos : (tipo, cantidad, precio)

            returns Boolean
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update inventario set nombre = :1, tipo = :2, cantidad = :3, precio_costo = :4 where nombre = :5"
                    cursor.execute(consulta_update, (nombre, datos[0], datos[1], datos[2], nombre,))
                    self.db.connection.commit()
                    print(f"[INFO]: {nombre} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {nombre}")

                    return False
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla de inventario.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {nombre} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:
        """
            Muestra los items actuales en la BD.

            returns List
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta = "select nombre, tipo, cantidad, precio_costo from inventario"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para inventario.")

                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_item(self, nombre: str) -> bool:
        """
            Elimina el item indicado, validando que exista en la BD.

            params
            - nombre : item a eliminar

            return Boolean
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from inventario where nombre = :5"
                cursor.execute(consulta_delete, (nombre,))
                self.db.connection.commit()
                print(f"[INFO]: {nombre} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla de inventario.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {nombre} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()