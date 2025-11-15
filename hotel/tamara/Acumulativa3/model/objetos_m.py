from config.db_config import ConexionOracle

class InventarioModel():
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

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con el nombre {nombre}")

                return False
            else:
                consulta_insert = "insert into inventario(nombre, tipo, cantidad, precio_costo)" \
                "values (:1, :2, :3, :4)"
                cursor.execute(consulta_insert, (nombre, tipo, cantidad, precio_costo))
                self.db.connection.commit()
                print(f"[INFO]:{nombre} Guardado correctamente")

            return True
        finally:
            if cursor:
                    cursor.close()

    def editar_item(self, nombre: str, datos: tuple):

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from inventario where nombre = :1" 
            cursor.execute(consulta_validacion, (nombre,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update inventario set nombre = :1, tipo = :2, cantidad = :3, precio_costo = :4 where nombre = :5"
                    cursor.execute(consulta_update, (datos[0], datos[1], datos[2], datos[3], nombre))
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

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from inventario where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from inventario where nombre = :1"
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

class HabitacionModel():
    def __init__(self, numero: int, huespedes: int, estado: str, conexion: ConexionOracle):
        self.numero = numero
        self.huespedes = huespedes
        self.estado = estado
        self.db = conexion

    def guardar_item(self, numero, huespedes, estado) -> bool:

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from habitacion where numero = :1"
            cursor.execute(consulta_validacion, (numero,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con el numero de habitacion {numero}")

                return False
            else:
                consulta_insert = "insert into habitacion(numero, huespedes, estado)" \
                "values (:1, :2, :3)"
                cursor.execute(consulta_insert, (numero, huespedes, estado))
                self.db.connection.commit()
                print(f"[INFO]: {numero} Guardado correctamente")

            return True
        finally:
            if cursor: 
                cursor.close()

    def editar_item(self, numero: int, datos: tuple) -> bool:
        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from habitacion where numero = :1"
            cursor.execute(consulta_validacion, (numero,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update habitacion set numero = :1, huespedes = :2, estado = :3 where numero = :4"
                    cursor.execute(consulta_update, (datos[0], datos[1], datos[2], numero)) 
                    self.db.connection.commit()
                    print(f"[INFO]:{numero} editado correctamente")

                    return True
                else: 
                    print(f"[ERROR]: Sin datos ingresados para habitación n°{numero}")

                    return False
            else:
                print(f"[ERROR]: {numero} no existe en la tabla de habitacion.")
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {numero} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:
        
        cursor = self.db.obtener_cursor()

        try:
            consulta = "select numero, huespedes, estado from habitacion"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para habitacion.")

                return[]
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return[]
        finally:
            if cursor:
                cursor.close()

    def eliminar_item(self, numero: int) -> bool:

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from habitacion where numero = :1"
            cursor.execute(consulta_validacion, (numero,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from habitacion where numero = :1"
                cursor.execute(consulta_delete, (numero,))
                self.db.connection.commit()
                print(f"[INFO]:Habitación n°{numero} eliminada correctamente.")

                return True
            else:
                print(f"[ERROR]: Habitación n°{numero}, no existe")

                return False
        finally: 
            if cursor:
                cursor.close()



class BoletaModel():
    def __init__(self, folio: int, cliente: str, usuario: str, conexion: ConexionOracle):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario
        self.db = conexion

    def guardar_item(self, folio, cliente, usuario) -> bool:

        cursor = self.db.obtener_cursor()

        try: 
            consulta_validacion = "select * from boleta where folio = :1"
            cursor.execute(consulta_validacion, (folio,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con el número de folio {folio}")

                return False
            else:
                consulta_insert = "insert into boleta(folio, cliente, usuario)" \
                "values (:1, :2, :3)"
                cursor.execute(consulta_insert, (folio, cliente, usuario))
                self.db.connection.commit()
                print(f"[INFO]: Folio {folio} guardado correctamente")

            return True
        finally:
            if cursor:
                cursor.close()

    def editar_item(self, folio: int, datos:tuple) -> bool:
        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from boleta where folio = :1"
            cursor.execute(consulta_validacion, (folio,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update boleta set folio = :1, cliente = :2, usuario =:3 where folio = :4"
                    cursor.execute(consulta_update, (datos[0], datos[1], datos[2], folio))
                    self.db.connection.commit()
                    print(f"[INFO]:{folio} editado correctamente")

                    return True
                else: 
                    print(f"[ERROR]: Sin datos ingresados para boleta {folio}")

                    return False
            else:
                print(f"[ERROR]: {folio} no existe en la tabla de boleta.")
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {folio} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:
        
        cursor = self.db.obtener_cursor()

        try:
            consulta = "select folio, cliente, usuario from boleta"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para boleta.")

                return[]
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return[]
        finally:
            if cursor:
                cursor.close()

    def eliminar_item(self, folio: int) -> bool:

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from boleta where folio = :1"
            cursor.execute(consulta_validacion, (folio,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from boleta where folio = :1"
                cursor.execute(consulta_delete, (folio,))
                self.db.connection.commit()
                print(f"[INFO]:Boleta folio {folio} eliminada correctamente.")

                return True
            else:
                print(f"[ERROR]: Folio {folio}, no existe")

                return False
        finally: 
            if cursor:
                cursor.close()