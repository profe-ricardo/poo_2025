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
    
    def agregar_productos(self, producto:list) -> bool:
        for p in producto:
            self.producto.append(p)
        self.cantidad = len(self.agregar_productos)
        print(f"Modelo: productos {producto} agregados")
        return True
    
    def eliminar_producto(self,producto_a_eliminar:list) -> bool:
        for p in producto_a_eliminar:
            try:
                self.producto.remove(p)
            except ValueError:
                print(f"ADVERTENCIA, el producto {p} no se encuentra en el inventario")
                
        return True
    
class Habitacion():
    def __init__(self,numero: int, cantidad_de_personas: int, estado: str):

        self.numero = numero
        self.cantidad_de_personas = cantidad_de_personas
        self.estado = estado
        conexion = conexion

    def guardar_item(self,numero: int, cantidad_de_personas: int, estado: str) -> bool:

        cursor = self.conexion.obtener_cursor()

        try:
            validacion = "select * from Habitacion where nombre = :1"
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
        
class Boleta():
    def __init__(self, folio: int, cliente:str, usuario:str):
        self.folio = folio
        self.cliente = cliente
        self.usuario = usuario
