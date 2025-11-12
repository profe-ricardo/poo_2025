
from config.db_confing import Conexionoracle
class InventoryModel:
    
    # Crear la conexion


    def __init__(self, Name: str, Tipe: str, Quantity: str, Cost_price: float, connection = Conexionoracle):
        self.Name = Name
        self.Tipe = Tipe
        self.Quantity = Quantity
        self. Cost_price = Cost_price      
        self.connection = connection

    def   Add_Product(self, Name, Tipe,Quantity, Cost_price) -> bool:
         
         cursor = self.connection.Get_cursor()

         try:
              Validation = "select * from inventory where Name = :1"
              cursor.execute(Validation, (Name,))

              if cursor.fetchall() > 0:
                   print(f"[####] El producto {Name} ya existe en el inventario")

                   return False
              else:
                   insert = "insert into inventory (Name, Tipe, Quantity, Cost_price) values (:1, :2, :3, :4)"
                   cursor.execute(insert, (Name, Tipe, Quantity, Cost_price))
                   self.connection.conecction.commit()
                   print(f"[####] El producto {Name} fue agregado correctamente")
               
                   return True
         except Exception as e:
              print(f"[####] Error al guardar el producto {Name} en el inventario → {e}")

              return False
         finally:
               if cursor:
                    cursor.close()
     
    def edit_Product(self, Name: str, *Data: tuple) -> bool:
         
         cursor = self.connection.get_cursor()

         try:
              Validation = "select * from inventory where Name = :1"
              cursor.execute(Validation, (Name,))

              if cursor.fetchall() == 0:
                   print(f"[####] El producto {Name} no existe en el inventario")

                   return False
              else:
                   update = "update inventory set Name = :1, Tipe = :2, Quantity = :3, Cost_price = :4 where Name = :5"
                   cursor.execute(update, (Name, Data[0], Data[1], Data[2], Name))
                   self.connection.conecction.commit()
                   print(f"[####] El producto {Name} fue actualizado correctamente")
               
                   return True
         except Exception as e:
              print(f"[####] Error al actualizar el producto {Name} en el inventario → {e}")

              return False
         finally:
               if cursor:
                    cursor.close()

    def Visual_product(self) -> list:
         
         cursor = self.connection.get_cursor()

         try:
              Visual = "select Name, Tipe, Quantity, Cost_price from inventory"
              cursor.execute(Visual)
              data = cursor.fetchall()

              if len(data) == 0:
                   print(f"[####] No hay productos en el inventario")

                   return []
              else:
                   print(f"[####] Productos obtenidos correctamente")

                   return data
         except Exception as e:
              print(f"[####] Error al obtener los productos del inventario → {e}")

              return []
         finally:
               if cursor:
                    cursor.close()

    def delete_product(self, Name:str) -> bool: 
         
          cursor = self.connection.get_cursor()

          try:
              Validation = "selec* from inventory where Name = :1 "
              cursor.execute(Validation, (Name,))     

              if len(cursor.fetchall()) == 0:
                   print(f"[####] El producto {Name} no existe en el inventario")

                   return False
              
              else:
                   
                   delete = "delete from inventory where Name =:5"
                   cursor.execute(delete, (Name,))
                   self.connection.conecction.commit()
                   print(f"[####] El producto {Name} fue eliminado correctamente")
               
                   return True
              
          except Exception as e:
                print(f"[####] Error al eliminar el producto {Name} del inventario → {e}")

                return False
              
          finally: 
               if cursor:
                    cursor.close()

         
         
class RoomModel:
     def __init__(self, Number: str, Number_of_people: int, Tipe: str, connection = Conexionoracle):
            self.Number = Number
            self.Number_of_peole = Number_of_people
            self.Tipe = Tipe
            self.connection = connection

     def Add_room(self, Number: str, Number_of_people: int, Tipe: str) -> bool:
          
          cursor = self.connection.get_cursor()

          try:
               Validation = "select * from rooms where Number = :1"
               cursor.execute(Validation, (Number,))

               if cursor.fetchall() > 0:
                    print(f"[####] La habitación {Number} ya existe")

                    return False
               else:
                    insert = "insert into rooms (Number, Number_of_people, Tipe) values (:1, :2, :3)"
                    cursor.execute(insert, (Number, Number_of_people, Tipe))
                    self.connection.conecction.commit()
                    print(f"[####] La habitación {Number} fue agregada correctamente")
                
                    return True
          except Exception as e:
               print(f"[####] Error al guardar la habitación {Number} → {e}")

               return False
          finally:
                if cursor:
                     cursor.close()
     
     def Visual_room(self) -> list:

          cursor = self.connection.get_cursor()

          try:
               Visual = "select Number, Number_ of_people, Tipe from rooms"
               cursor.execute(Visual)
               data = cursor.fetchall()

               if len(data) == 0:
                    print(f"[####] No hay habitaciones registradas")

                    return []
               else: 
                    print(f"[####] Habitaciones obtenidas correctamente")
          except Exception as e:
               print(f"[####] Error al obtener las habitaciones → {e}")
          
          finally:
               if cursor: 
                    cursor.close()
     def edit_room(self, Number: str, *Data: tuple) -> bool: 

          cursor = self.connection.get_cursor()

          try:
               Validation = "select * from rooms where Number = :1"
               cursor.execute(Validation, (Number,))

               if cursor.fetchall() == 0:
                    print(f"[####] La habitación {Number} no existe")

                    return False
               else:
                    update = "update rooms set Number = :1, Number_of_people = :2, Tipe = :3 where Number = :4"
                    cursor.execute(update, (Number, Data[0], Data[1], Number))
                    self.connection.conecction.commit()
                    print(f"[####] La habitación {Number} fue actualizada correctamente")
                
                    return True
          except Exception as e:
               print(f"[####] Error al actualizar la habitación {Number} → {e}")

               return False
          
          finally:
                if cursor:
                     cursor.close()
     
     def delete_room(self, Number:str) -> bool:

          cursor = self.connection.get_cursor()

          try:
               valdation = "select * from rooms where Number = :1"
               cursor.execute(valdation,(Number,))
               if len(cursor.fetchall()) == 0:
                    print(f"[####] La habitación {Number} no existe")

                    return False 
               else:
                    delete = "delete from rooms where Number = :1"
                    cursor.execute(delete, (Number,))
                    self.connection.connecction.commit()
                    print(f"[####] La habitación {Number} fue eliminada correctamente")
                    return True
          except Exception as e:
               print(f"[####] Error al eliminar la habitacion {Number} → {e}")
               return False
          
          finally:
               if cursor:
                    cursor.close()
               
class Ticket():
      def __init__(self,Folio: int, Client: str, Usuario: str, connection = Conexionoracle):
            self.Folio = Folio
            self.Client = Client
            self.Usuario = Usuario
            self.connection = connection

      def Add_Ticket(self, Folio: int, Client: str, Usuario: str) -> bool:
           
          cursor = self.connection.get_cursor()

          try:
               Validation = "select * from boleta where Folio = :1"
               cursor.execute(Validation, (Folio,))

               if cursor.fetchall() == 0:
                    insert = "insert into boletas(Folio, Client, Usuario) values (:1, :2, :3)"
                    cursor.execute(insert, (Folio, Client, Usuario))
                    self.connection.connection.commit()
                    print(f"[####] La boleta {Folio} fue agregada correctamente")

                    return  True
               else:
                    print(f"[####] La boleta {Folio} ya existe")

                    return False
               
          except Exception as e:
               print(f"[####] Error al guardar la boleta {Folio} -> {e}")
               return False
          
          finally:
               if cursor:
                    cursor.close()

      def Edit_Ticket(self, Folio: int, *Data: tuple) -> bool:
           
          cursor = self.connection.get_cursor()

          try:
               Validation = "select * from boletas where Folio =:1"
               cursor.execute(Validation,(Folio,))

               if cursor.fetchall() == 0:
                    print(f"[####] La boleta {Folio} no existe")

                    return False
               else: 
                    update = "update boletas set Folio = :1, Client = :2, Usuario = :3 where Folio = :4"
                    cursor.execute(update, (Folio, Data[0], Data[1], Folio))
                    self.connection.connection.commit()
                    print(f"[####] La boleta {Folio} fue actualizada correctamente")
                    return True
          except Exception as e:
               print(f"[####] Error al actualizar la boleta {Folio} -> {e}")
               return False
          
          finally:
               if cursor:
                    cursor.close()
     
      def Visual_Ticket(self) -> list:
           
          cursor = self.connection.get_cursor()
           
          try:
               Visual = "select Folio, Client, Usuario from boletas"
               cursor.execute(Visual)
               data = cursor.fetchall()
               
               if len(data) == 0:
                    print(f"[####] No hay boletas registradas")

                    return []
               else:

                    print(f"[####] Boletas obtenidas correctamente")
                    return data
          except Exception as e:
               print(f"[####] Error al obtener las boletas -> {e}")
               return []
          
          finally:
               if cursor:
                    cursor.close()
      
      def Delete_Ticket(self, Folio: int) -> bool: 
           
          cursor = self.connection.get_cursor()

          try:
               validation = "select * from boletas where Folio = :1"
               cursor.execute(validation, (Folio,))

               if len(cursor.fetchall()) == 0:
                    print(f"[####] la boletas {Folio} no existe")
                    return False
               else:
                    delete = "delete from boletas where Folio = :1"
                    cursor.execute(delete, (Folio,))
                    self.connection.connection.commit()
                    print(f"[####] La boleta {Folio} fue eliminada correctamente")
                    return True
          except Exception as e:
               print(f"[####] Error al eliminar la boleta {Folio} -> {e}")
               return False
          finally:
               if cursor:
                    cursor.close()



            




           
           








