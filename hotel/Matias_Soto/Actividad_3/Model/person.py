from config.db_confing import Conexionoracle

class clientMoldel:
    def __init__(self, Name: str, Phone: int, Location:str, Room: str, connection = Conexionoracle):
       self.Name = Name
       self.Phone = Phone
       self.Location = Location
       self.Room = Room
       self.connection = connection

    def register_client(self, Name: str, Phone: int, Location: str, Room: str) -> bool:

        cursor = self.connection.get_cursor()

        try:
            Validation = "select * from Client where Name = :1"
            cursor.execute(Validation, (Name,))

            if len(cursor.fetchall()) == 0:
                Client = "inset into clients (Name, Phone, Location, Room) values (:1, :2, :3, :4)"
                cursor.execute(Client, (Name, Phone, Location, Room))
                self.connection.connection.commit()
                print(f"Se ha subido su {Name} insertado Correctamente")

                return True
            else:
                print(f"[###] Ya existe el {Name} que inserta ")

                return False
            
        except Exception as e:
            print("[####] Error al insgresar su cliente -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def Edit_Client(self, Name: str, *Date: tuple) -> bool:

        cursor = cursor.get_cursor()

        try:

            Validation =  "select * from Client where Name = :1 "
            cursor.execute(Validation,(Name,))

            if len(cursor.fetall()) == 0:
                print(f" El archivo que usted quiere editar no existe")

                return False
            
            else:
                Update = "update Client set Name = :1, Phone = :2, Location = :3, Room = :4 where Name = :5"
                cursor.execute(Update, (Name, Date[0],Date[1],Date[2],Name))
                self.connection.conection.commit()
                print(f"[####] El Cliente {Name} fue actualizado correctamente")
                
                return True


        except Exception as e:
            print("[####] No se pudo Guardar su {Name} ")
            
            return False
        
        finally:
            if cursor:
                cursor.close()

    def Delete_Client(self, Name: str) -> bool:

            cursor = self.connection.get_cursor()

            try:
               validation = "select * from Client where Name = :1"
               cursor.execute(validation, (Name,))

               if len(cursor.fetchall()) == 0:
                    print(f"[####] la boletas {Name} no existe")
                    return False
               else:
                    delete = "delete from Client where Name = :1"
                    cursor.execute(delete, (Name,))
                    self.connection.connection.commit()
                    print(f"[####] El cliente {Name} fue eliminado correctamente")
                    return True
            except Exception as e:
               print(f"[####] Error al eliminar El cliente {Name} -> {e}")
               return False
            finally:
               if cursor:
                    cursor.close()
    def Visual_Client(self) -> bool:

            cursor = self.connection.get_cursor()
           
            try:
               Visual = "select Name, Phone, Location, Room from Client"
               cursor.execute(Visual)
               data = cursor.fetchall()
               
               if len(data) == 0:
                    print(f"[####] No hay Clientes registradas")

                    return []
               else:

                    print(f"[####] Clientes obtenidos correctamente")
                    return data
               
            except Exception as e:
               print(f"[####] Error al obtener los clientes -> {e}")
               return []
          
            finally:
               if cursor:
                    cursor.close()
            
class UsuarioModel:
    """
        Modelo del usuario.\n
        Métodos de creación y muestra de usuarios, realizando conexión con BD.
    """
    def __init__(self, conexion: Conexionoracle):
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

class Reception(UsuarioModel):
    def __init__(self, Name: str, Phone: int, location: str, conexion):
        super().__init__(conexion)

        self.Name = Name
        self.Phone= Phone
        self.location= location
        self.conexion = conexion
    
    def create_reservation(self, Name: str, Phone: int, location: str) -> bool:
        
        cursor = self.conexion.get_cursor()

        try:
            Validation = "select * from reservation where Name = :1"
            cursor.execute(Validation, (Name,))

            if len(cursor.fetchall()) == 0:
                Client = "inset into reservation (Name, Phone, location) values (:1, :2, :3)"
                cursor.execute(Client, (Name, Phone, location))
                self.conexion.conexion.commit()
                print(f"Se ha inserado su reserva {Name} Correctamente")

                return True
            
            else:
                print(f"[###] Ya existe la reserva {Name} ")

                return False
            
        except Exception as e:
            print("[####] Error al insgresar su reservacion -> {e}")

            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def edit_reservation(self, Name: str, *Date: tuple) -> bool:

        cursor = self.conexion.get_cursor()

        try:

            Validation =  "select * from Reservation where Name = :1 "
            cursor.execute(Validation,(Name,))

            if len(cursor.fetall()) == 0:
                print(f" la reservacion que usted quiere editar no existe")

                return False
            
            else:
                Update = "update Reservation set Name = :1, Phone = :2, Location = :3 where Name = :4"
                cursor.execute(Update, (Name, Date[0],Date[1],Name))
                self.conexion.conexion.commit()
                print(f"[####] La reservacion {Name} fue actualizado correctamente")
                
                return True


        except Exception as e:
            print("[####] No se pudo Guardar su reservacion {Name} ")
            
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    def delete_reservation(self, Name: str) -> bool:
         
            cursor = self.conexion.get_cursor()

            try:
                validation = "select * from Reservation where Name = :1"
                cursor.execute(validation, (Name,))

                if len(cursor.fetchall()) == 0:
                    print(f"[####] la Reservacion {Name} no existe")
                    return False
                else:
                    delete = "delete from Reservation where Name = :1"
                    cursor.execute(delete, (Name,))
                    self.conexion.conexion.commit()
                    print(f"[####] La reservacion {Name} fue eliminado correctamente")
                    return True
            except Exception as e:
               print(f"[####] Error al eliminar la reservacion {Name} -> {e}")
               return False
            finally:
               if cursor:
                    cursor.close()
    
    def visual_reservation(self):

            cursor = self.conexion.get_cursor()
           
            try:
               Visual = "select Name, Phone, Location from Reservation"
               cursor.execute(Visual)
               data = cursor.fetchall()
               
               if len(data) == 0:
                    print(f"[####] No hay Reservaciones registradas")

                    return []
               else:

                    print(f"[####] Reservaciones obtenidas correctamente")
                    return data
               
            except Exception as e:
               print(f"[####] Error al obtener las reservaciones -> {e}")
               return []
          
            finally:
               if cursor:
                    cursor.close()



    

