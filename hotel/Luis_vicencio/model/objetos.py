from config.db_config import ConexionOracle

class InventarioModel():
    def __init__(self,nombre: str, tipo: str, cantidad: int, precio_costo: int, conexion:ConexionOracle):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio_costo = precio_costo
        self.conexion = conexion
        
    def guardar_item(self,nombre, tipo, cantidad, precio_costo) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            validacion = "select * from Inventario where nombre = :1"
            cursor.execute(validacion, (nombre,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]:Ya existe un item con el nomnre{nombre}")
                return False
            else:
                consulta_insert = "insert into inventario(nombre, tipo, cantidad, precio_costo) values (:1, :2, :3, :4)"
                cursor.execute(consulta_insert, (nombre, tipo, cantidad, precio_costo))
                self.conexion.connection.commit()
                print(f"[INFO]: {nombre} guardado correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar {nombre} ->{e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_item(self, nombre: str, *datos: tuple) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * froom inventario where nombre = :1"
            cursor.execute(validacion, (nombre,))
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update inventario set nombre = :1, tipo = :2, cantidad = :3, precio_costo = :4 where nombre = :5"
                    cursor.execute(consulta_update,(nombre,datos[0], datos[1], datos[2], datos[3], nombre,))
                    print(f"[INFO]: {nombre} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos para {nombre}")

                    return False
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla inventaro")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {nombre} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:

        cursor = self.conexion.obtener_cursor()
        
        try:
            consulta = "select nombre, tipo, cantidad, precio_costo from Inventario"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para inventario")
                return []
        except Exception as e:
            print(f"[ERROR]: error al obtener items desde BD -> {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
    def eliminar_item(self,nombre: str) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from inventraio where nombre = :1"
            cursor.execute(validacion,(nombre,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from inventario where nombre = :5"
                cursor.execute(consulta_delete, (nombre,))
                self.conexion.connection.commit()
                print(f"[INFO]: {nombre} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla inventario")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {nombre} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()





    
class HabitacionModel():

    def __init__(self,numero: int, cantidad_de_personas: int, estado: str, conexion: ConexionOracle):
    
        self.numero = numero
        self.cantidad_de_personas = cantidad_de_personas
        self.estado = estado
        self.conexion = conexion
    
    def guardar_item(self,numero: int, cantidad_de_personas: int, estado: str) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            validacion = "select * from Habitacion where numero = :1"
            cursor.execute(validacion, (numero,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Habitacion {numero} ya esta asignada")
                return False
            else:
                consulta_insert = "insert into habitacion(numero, cantidad_de_personas, estado) values (:1, :2, :3)"
                cursor.execute(consulta_insert, (numero, cantidad_de_personas, estado))
                self.conexion.connection.commit()
                print(f"[INFO]: Habitacion {numero} asignada correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al asignar habitacion {numero} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_item(self, numero: int, *datos: tuple) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from habitacion where nombre = :1"
            cursor.execute(validacion, (numero,))
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update habitacion set numero = :1, cantidad_de_personas = :2, estado = :3 where nombre = :4"
                    cursor.execute(consulta_update,(numero,datos[0], datos[1], datos[2], numero,))
                    print(f"[INFO]: {numero} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos para {numero}")

                    return False
            else:
                print(f"[ERROR]: {numero} no existe en la tabla Habitacion")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {numero} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:

        cursor = self.conexion.obtener_cursor()
        
        try:
            consulta = "select numero, cantidad_de_personas, estado from habitacion"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para habitacion")
                return []
        except Exception as e:
            print(f"[ERROR]: error al obtener items desde BD -> {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
    def eliminar_item(self,numero: int) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from habitacion where numero = :1"
            cursor.execute(validacion,(numero,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from habitacion where nombre = :5"
                cursor.execute(consulta_delete, (numero,))
                self.conexion.connection.commit()
                print(f"[INFO]:Habitacion {numero} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {numero} no existe en la tabla habitacion")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {numero} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()
        
class Boleta():
    def __init__(self, folio: int, cliente:str, usuario:str, conexion:ConexionOracle):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario
        self.conexion = conexion

    def guardar_item(self, folio: int, cliente: str, usuario: str) -> bool:
    
        cursor = self.conexion.obtener_cursor()

        try:
            validacion = "select * from boletas where folio = :1"
            cursor.execute(validacion, (folio,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Boleta {folio} ya esta asignada")
                return False
            else:
                consulta_insert = "insert into boletas(folio, cliente , usuario) values (:1, :2, :3)"
                cursor.execute(consulta_insert, (folio, cliente, usuario))
                self.conexion.connection.commit()
                print(f"[INFO]: Boleta {folio} asignada correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al asignar boleta {folio} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_item(self, folio: int, *datos: tuple) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from boletas where nombre = :1"
            cursor.execute(validacion, (folio,))
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update boletas set folio = :1, cliente = :2, usuario = :3 where nombre = :4"
                    cursor.execute(consulta_update,(folio,datos[0], datos[1], datos[2], folio,))
                    print(f"[INFO]: {folio} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos para {folio}")

                    return False
            else:
                print(f"[ERROR]: {folio} no existe en la tabla Boletas")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar boleta n° {folio} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()

    def mostrar_items(self) -> list:

        cursor = self.conexion.obtener_cursor()
        
        try:
            consulta = "select folio, cliente, usuario from Boletas"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para Boletas")
                return []
        except Exception as e:
            print(f"[ERROR]: error al obtener items desde BD -> {e}")
            return []
        
        finally:
            if cursor:
                cursor.close()
    def eliminar_item(self,folio: int) -> bool:
        cursor = self.conexion.obtener_cursor()
        try:
            validacion = "select * from Boletas where numero = :1"
            cursor.execute(validacion,(folio,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from Boletas where nombre = :5"
                cursor.execute(consulta_delete, (folio,))
                self.conexion.connection.commit()
                print(f"[INFO]:Boleta n° {folio} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]:boleta n° {folio} no existe en la tabla Boletas")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar Boleta n° {folio} -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()