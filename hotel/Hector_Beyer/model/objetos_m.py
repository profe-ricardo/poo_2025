from hotel.Hector_Beyer.config.db_config import ConexionOracle

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
            datos = cursor.fetchall()

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

class HabitacionModel:
    """
        Modelo de Habitacion.\n
        Contiene métodos para creación, edición y muestra de Habitaciones, realizando conexión con BD.
    """
    def __init__(self, numero_habitacion: int, cantidad_personas: int, estado:str, conexion: ConexionOracle):
        self.numero_habitacion = numero_habitacion
        self.cantidad_personas = cantidad_personas
        self.estado = estado
        self.db = conexion

    def guardar_item(self, numero_habitacion, cantidad_personas, estado) -> bool:
        """
            Guarda el item actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """

        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from habitaciones where numero_habitacion = :1"
            cursor.execute(consulta_validacion, (numero_habitacion,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con el numero de habitacion {numero_habitacion}")

                return False
            else:
                consulta_insert = "insert into habitaciones (numero_habitacion, cantidad_personas, estado) values (:1, :2, :3)"
                cursor.execute(consulta_insert, (numero_habitacion, cantidad_personas, estado))
                self.db.connection.commit()
                print(f"[INFO]: {numero_habitacion} guardada correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar {numero_habitacion} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def editar_item(self, numero_habitacion: str, *datos: tuple) -> bool:
        """
            Edita el item indicado solo si existe en la BD.\n
            Si es que no existe, lanzará el mensaje correspondiente.\n

            params
            - numero_habitacion : Numero de habitacion a editar
            - datos : (cantidad personas, estado)

            returns Boolean
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from habitaciones where numero_habitacion = :1"
            cursor.execute(consulta_validacion, (numero_habitacion,))
            datos = cursor.fetchall()

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update habitaciones inventario set numero_habitacion = :1, cantidad_personas = :2, estado = :3 where numero_habitacion = :4"
                    cursor.execute(consulta_update, (numero_habitacion, datos[0], datos[1], numero_habitacion,))
                    self.db.connection.commit()
                    print(f"[INFO]: {numero_habitacion} editada correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {numero_habitacion}")

                    return False
            else:
                print(f"[ERROR]: {numero_habitacion} no existe en la tabla de habitaciones.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {numero_habitacion} -> {e}")

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
            consulta = "select numero_habitacion, cantidad_personas, estado from habitaciones"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para habitaciones.")

                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_item(self, numero_habitacion: str) -> bool:
        """
            Elimina el item indicado, validando que exista en la BD.

            params
            - numero_habitacion : item a eliminar

            return Boolean
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from habitaciones where nombre = :1"
            cursor.execute(consulta_validacion, (numero_habitacion,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from habitaciones where nombre = :1"
                cursor.execute(consulta_delete, (numero_habitacion,))
                self.db.connection.commit()
                print(f"[INFO]: {numero_habitacion} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {numero_habitacion} no existe en la tabla de habitaciones.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {numero_habitacion} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

class BoletaModel:
    """
        Modelo de boleta.\n
        Contiene métodos para creación, edición y muestra de boletas, realizando conexión con BD.
    """
    def __init__(self, folio: int, usuario: int, cliente:int, conexion: ConexionOracle):
        self.folio = folio
        self.usuario = usuario
        self.cliente = cliente
        self.db = conexion

    def guardar_item(self, folio, usuario, cliente) -> bool:
        """
            Guarda el item actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """

        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from boletas where folio = :1"
            cursor.execute(consulta_validacion, (folio,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con el numero de folio {folio}")

                return False
            else:
                consulta_insert = "insert into boletas (folio, usuario, cliente) values (:1, :2, :3)"
                cursor.execute(consulta_insert, (folio, usuario, cliente))
                self.db.connection.commit()
                print(f"[INFO]: {folio} guardado correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar {folio} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def editar_item(self, folio: str, *datos: tuple) -> bool:
        """
            Edita el item indicado solo si existe en la BD.\n
            Si es que no existe, lanzará el mensaje correspondiente.\n

            params
            - folio : Numero de boleto
            - usuario : Usuario que ingreso boleta
            - cliente : Cliente que recibio boleta

            returns Boolean
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from boletas where folio = :1"
            cursor.execute(consulta_validacion, (folio,))
            datos = cursor.fetchall()

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update inventario set folio = :1, usuario = :2, cliente = :3 where folio = :4"
                    cursor.execute(consulta_update, (folio, datos[0], datos[1], folio,))
                    self.db.connection.commit()
                    print(f"[INFO]: {folio} editada correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {folio}")

                    return False
            else:
                print(f"[ERROR]: {folio} no existe en la tabla de boletas.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {folio} -> {e}")

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
            consulta = "select folio, usuario, cliente from boletas"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para boletas.")

                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_item(self, folio: str) -> bool:
        """
            Elimina el item indicado, validando que exista en la BD.

            params
            - numero_habitacion : item a eliminar

            return Boolean
        """

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from boletas where folio = :1"
            cursor.execute(consulta_validacion, (folio,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from boletas where nombre = :5"
                cursor.execute(consulta_delete, (folio,))
                self.db.connection.commit()
                print(f"[INFO]: {folio} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {folio} no existe en la tabla de boletas.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {folio} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()