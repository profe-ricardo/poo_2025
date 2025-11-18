from hotel.Heidi_Labe.config.db_config import ConexionOracle
class InventarioModel:
      def __init__(self, nombre: str, tipo: str, cantidad: int,precio_costo: float, conexion: ConexionOracle):
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
         print(f"[ERROR]:ya existe un item con el nombre {nombre}")

         return False
      else:
         consulta_insert = "insert into inventario (nombre, tipo, cantidad, precio_costo) values(:1, :2, :3, :4)"
         cursor.execute(consulta_insert,(nombre, tipo, cantidad, precio_costo))
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
         consultar_validacion = "select * from inventario where nombre = :1" 
         cursor.execute(consultar_validacion,(nombre,)) 
         if len(cursor.fetchall()) > 0: 
            if datos:
               consulta_update = "update inventario set nombre = :1, tipo =:2, cantidad = :3, precio_costo = :4 where nombre = :5"
               cursor.execute(consulta_update,(nombre, datos[0],datos[1],datos[2],datos[3], nombre,))
               self.db.connection.commit()
               print(f"[INFO]:{nombre}editado correctamente") 
               return True
            else:
               print(f"[ERROR]: sin datos ingresados para {nombre}")
               return False
         else:
            print(f"[ERROR]: {nombre} no existe en la tabla de inventario.")
            return False
      except Exception as e :
         print(f"[ERROR]: Error al editar{nombre} ->{e}") 
         return False
      finally:
         if cursor:
            cursor.close()

            def mostrar_items(self) ->list:
               cursor = self.db.obtener_cursor()
               try:
                  consulta = "select nombre, tipo, cantidad, precio_costo from inventario"
                  cursor.execute(consulta)
                  datos = cursor.fetchall()

                  if len(datos) > 0:
                     return datos
                  else:
                     print("[INFO] sin datos para el inventario . ")
                     return[]
               except Exception as e:
                  print(f"[ERROR]:Error al obtener items desde bd -> {e}")
                  return[]
               finally:
                  if cursor:
                     cursor.close()
                     def eliminar_item(self,nombre: str )-> bool:
                        cursor = self.db.obtener_cursor()
                        try:
                           consulta_validacion = "select * from inventario where nombre = :1"
                           cursor.execute(consulta_validacion,(nombre,))
                           if len(cursor.fetchall()) > 0:
                              consulta_delete = "delete from inventario where nombre = :5"
                              cursor.execute(consulta_delete,(nombre,))
                              self.db.connection.comit()
                              print(f"[INFO]: {nombre}eliminado correctamente")
                              return True
                           else:
                              print(f"[ERROR]:{nombre} no existe en la tabla de inventario.")
                              return False
                        except Exception as e:
                           print(f"[ERROR]: Error al eliminar {nombre} ->{e}")
                           return False
                        finally:
                           if cursor:
                              cursor.close()

                              class UsuarioModel:
                                 def _init__(self,nombre:str, telefono: str, conexion: ConexionOracle):
                                    self.nombre = nombre
                                    self.telefono = telefono
                                    self.db = conexion
                                    def crear(self, nombre: str,telefono:str)-> bool:
                                       cursor = self.db.obtener_cursor()
                                       try:
                                          consulta_insert = "insert into usuarios (nombre, telefono) values(:1, :2)"
                                          cursor.execute(consulta_insert,(nombre, telefono))
                                          self.db.connection.comit()
                                          print(f"[INFO]:usuario {nombre} creado correctamente.")
                                          return True
                                       except Exception as e:
                                          print(f"[ERROR]: Error al crear usuario {nombre} ->{e}")
                                          return False
                                       finally:
                                          if cursor:
                                             cursor.close()
                                             def mostrar_todos(self)-> list:
                                                cursor = self.db.obtener_cursor()
                                                try:
                                                   consulta = "select nombre, telefono from  usuarios"
                                                   cursor.execute(consulta)
                                                   return cursor.fetchall()
                                                except Exception as e:
                                                   print(f"[ERROR]:Error al obtener usuarios -> {e}")
                                                   return[]
                                                finally:
                                                   if cursor:
                                                      cursor.close()

                                                      class RecepcionitaModel(UsuarioModel):
                                                         def __int__(self, nombre:str, telefono: str, ubicacion: str, conexion: ConexionOracle):
                                                            super().__init__(nombre, telefono, conexion)
                                                            self.ubicacion = ubicacion
                                                            def crear_tabla_oracle(db_conexion: ConexionOracle):
                                                               sql = """"
                                                               create table recepcionistas(
                                                               nombre varchar2(100)PRIMARY KEY,
                                                               telefono varchar2(20) not null,
                                                               ubicacion varchar2(50)
                                                               )
                                                               """
                                                               cursor = db_conexion.obtener_cursor()
                                                               try:
                                                                  cursor.execute(sql)
                                                                  db_conexion.connection.commit()
                                                                  print("[INFO]:Tabla recepcionistas creada correctamente.")
                                                               except Exception as e:
                                                                  print(f"[ERROR]:Error al crear tabla recepcionistas -> {e}")
                                                               finally:
                                                                  if cursor:
                                                                     cursor.close()
                                                                     def guardar(self) -> bool:
                                                                        cursor = self.db.obtener_cursor()
                                                                        try:
                                                                           consulta_insert = "insert into recepcionistas (nombre, telefono, ubicacion) values( :1, :2, :3)"
                                                                           cursor.execute(consulta_insert,(self.nombre, self.telefono, self.ubicacion))
                                                                           self.db.connection.cmmit()
                                                                           print(f"[INFO]: Recepcionista {self.nombre} guardado con exito.")
                                                                           return True
                                                                        except Exception as e:
                                                                           print(f"[ERROR]: Error al guardar recepcionista {self.nombre} -> {e}")
                                                                           return False
                                                                        finally:
                                                                           if cursor:
                                                                              cursor.close()
                                                                              class habitacionModel:
                                                                                 def __init__(self, numero: int, cantidad_personas: int, estado: str, conexion: ConexionOracle):
                                                                                    self.numero = numero
                                                                                    self.cantidad_personas = cantidad_personas
                                                                                    self.estado = estado
                                                                                    self.db = conexion
                                                                                    @staticmethod
                                                                                    def crear_tabla_oracle(db_conexion: ConexionOracle):
                                                                                       sql = """"
                                                                                       create table habitaciones(
                                                                                       numero number PRIMARY KEY,
                                                                                       cantidad_personas number not null,
                                                                                       estado varchar2(20)default "disponible"


                                                                                       )"""
                                                                                       cursor = db_conexion.obtener_cursor()
                                                                                       try:
                                                                                          cursor.execute(sql)
                                                                                          db_conexion.connection.commit()
                                                                                          print("[INFO]: Tabla habitaciones creada correctamentamente.")
                                                                                       except Exception as e:
                                                                                          print(f"[ERROR]: Error al crear tabla habitaciones -> {e}")
                                                                                       finally:
                                                                                          if cursor:
                                                                                             cursor.close()
                                                                                             def guardar(self) -> bool:
                                                                                                cursor = self.db.obtener_cursor()
                                                                                                try:
                                                                                                   consulta_insert = "insert into habitaciones (numero, cantidad_personas, estado) values(:1, :2, :3)"
                                                                                                   cursor.execute(consulta_insert,(self.numero, self.cantidad_personas, self.estado))
                                                                                                   self.db.connetion.commit()
                                                                                                   print(f"[INFO]: Habitaciones {self.numero} guardada correctamente.")
                                                                                                   return True
                                                                                                except Exception as e:
                                                                                                   print(f"[ERROR]: Error al guardar habitacion {self.numero} -> {e}")
                                                                                                   return False
                                                                                                finally:
                                                                                                   if cursor:
                                                                                                      cursor.close()
                                                                                                      def actualizar_estado(self,nuevo_estado: str) -> bool:
                                                                                                         cursor = self.db.obtener_cursor()
                                                                                                         try:
                                                                                                            consulta_update = "update habitaciones set estado = :1 where numero = :2"
                                                                                                            cursor.execute(consulta_update,(nuevo_estado, self.numero))
                                                                                                            self.db.connetion.commit()
                                                                                                            print(f"[INFO]: Estado de habitacion {self.numero} actualizado a {nuevo_estado}.")
                                                                                                            return True
                                                                                                         except Exception as e:
                                                                                                            print(f"[ERROR]: Error al actualizar estado de habitacion {self.numero} -> {e}")
                                                                                                            return False
                                                                                                         finally:
                                                                                                            if cursor:
                                                                                                               cursor.close()
                                                                                                               class clienteModel:
                                                                                                                  def __init__(self, nombre: str, telefono: str, nacionalidad: str, habitacion: int, conexion: ConexionOracle):
                                                                                                                     self.nombre = nombre
                                                                                                                     self.telefono = telefono
                                                                                                                     self.nacionaliadad = nacionalidad
                                                                                                                     self.habitacion = habitacion
                                                                                                                     self.db = conexion
                                                                                                                     @staticmethod
                                                                                                                     def crear_tabla_oracle(db_conexion: ConexionOracle):
                                                                                                                        sql = """"
                                                                                                                        create table clientes(
                                                                                                                        id_cliente number generated by default as identity PRIMARY KEY,
                                                                                                                        nombre varchar2(100) not null,
                                                                                                                        telefono varchar2(20),
                                                                                                                        nacionalidad varchar2(50),
                                                                                                                        habitacion_numero number,
                                                                                                                        FOREIGN KEY (habitacion_numero) references habitaciones(numero)
                                                                                                                        )"""
                                                                                                                        cursor = db_conexion.obtener_cursor()
                                                                                                                        try:
                                                                                                                           cursor.execute(sql)
                                                                                                                           db_conexion.connection.commit()
                                                                                                                           print("[INFO]: Tabla clientes cresada.")
                                                                                                                        except Exception as e:
                                                                                                                           print(f"[ERROR]: Error al crear tabla clientes -> {e}")
                                                                                                                        finally:
                                                                                                                           if cursor:
                                                                                                                              cursor.close()
                                                                                                                              def guardar(self) -> bool:
                                                                                                                                 cursor = self.db.obtener_cursor()
                                                                                                                                 try:
                                                                                                                                    consulta_insert = "insert into clientes (nombre, telefono, nacionalidad, habitacion_numero) values(:1, :2, :3, :4)"
                                                                                                                                    cursor.execute(consulta_insert,(self.nombre, self.telefono, self.nacionalidad, self.habitacion))
                                                                                                                                    self.db.connection.commit()
                                                                                                                                    print(f"[INFO]: Cliente {self.nombre}guardado y asignacion a habitacion {self.habitacion}.")
                                                                                                                                    return True
                                                                                                                                 except Exception as e:
                                                                                                                                    print(f"[ERROR]: Error al guardar cliente {self.nombre} -> {e}")
                                                                                                                                    return False
                                                                                                                                 finally:
                                                                                                                                    if cursor:
                                                                                                                                       cursor.close()
                                                                                                                                       class BoletaModel:
                                                                                                                                          def __init_(self, folio: int, cliente: str,clienteModel, usuario: str,RecepcionistaModel, total: float, conexion: ConexionOracle):
                                                                                                                                             self.folio = folio
                                                                                                                                             self.cliente = cliente
                                                                                                                                             self.usuario = usuario
                                                                                                                                             self.total = total 
                                                                                                                                             self.db = conexion
                                                                                                                                             @staticmethod
                                                                                                                                             def crear_tabla_oracle(db_conexion: ConexionOracle):
                                                                                                                                                sql = """"
                                                                                                                                                create tabla boletas(
                                                                                                                                                folio number PRIMARY KEY,
                                                                                                                                                total  number(10,2) not null,
                                                                                                                                                cliente_id number,
                                                                                                                                                usuario_nombre varchar2(100),
                                                                                                                                                fecha_emision date default sisdate,

                                                                                                                                              
                                                                                                                                                
                                                                                                                                                )"""
                                                                                                                                                cursor = db_conexion.obtener_cursor()
                                                                                                                                                try:
                                                                                                                                                   cursor.execute(sql)
                                                                                                                                                   db_conexion.connection.commit()
                                                                                                                                                   print("[INFO]: Tabla boletas creada.")
                                                                                                                                                except Exception as e:
                                                                                                                                                   print(f"[ERROR]: Error al crear tabla boletas -> {e}")
                                                                                                                                                finally:
                                                                                                                                                   if cursor:
                                                                                                                                                      cursor.close()
                                                                                                                                                      def guardar(self) -> bool:
                                                                                                                                                         cursor = self.db.obtener_cursor()
                                                                                                                                                         try:
                                                                                                                                                            cliente_id_ejemplo = 1
                                                                                                                                                            usuario_nombre = self.usuario.nombre
                                                                                                                                                            consulta_insert = """
                                                                                                                                                            insert into boletas (folio, total, cliente_id, usuario_nombre)
                                                                                                                                                            values(:1, :2, :3, :4)
                                                                                                                                                            """
                                                                                                                                                            cursor.execute(consulta_insert,(self.folio,self.total, cliente_id_ejemplo, usuario_nombre))
                                                                                                                                                            self.db.connection.commit()
                                                                                                                                                            print(f"[INFO]:Boleta folio {self.folio} emitida y guardada.Total: {self.total}")
                                                                                                                                                            return True
                                                                                                                                                         except Exception as e:
                                                                                                                                                            print(f"[ERROR]: Error al guardar boleta {self.folio} -> {e}")
                                                                                                                                                            return False
                                                                                                                                                         finally:
                                                                                                                                                            if cursor:
                                                                                                                                                               cursor.close()


                                                                                                                                             

                                                                                                                                 
                                                                                                                                 
                                                                                                                  




                                                                                                                        
                                                                                                      
                                                                                                                     
                                                                                                      

                                                                                                  
                                                                        
                                                                                                                  

                                                                                 
                                                                                    



                                                                  

                                                                
                                                                   
                                                                  
                           
                        
                                                               



            
                                                               
                                                                  



                                                                  
                                                                  
                                                            
                                                            
                                                   

                                                               
                                                                  




                                 


                                                
                     





                           

                  

