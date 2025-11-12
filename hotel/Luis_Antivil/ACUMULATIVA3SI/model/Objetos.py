from Usuario import UsuarioModel
from Personas import cliente


class boleta():
    """
    se debe poder generar una boleta, actualizar, eliminar o leer lo de la boleta
    """
    def __init__(self,folio:int,cliente:cliente,usuario:UsuarioModel):
        self.folio=folio
        self.cliente=cliente
        self.usuario=usuario
        
    def CrearBoleta (self,folio:int, cliente:cliente, usuario:UsuarioModel):
        cursor = self.db.obtener_cursor()
        """
        primero verificamos la existencia del cliente y del usuario en la base de datos
        segundo generamos la boleta
        """
        
        try:
            Validar_Cliente= "Select * from Personas where nombre= :1"
            cursor.Execute(Validar_Cliente)
            cliente_existe=len(cursor.fetchall())>0
            
            Validar_Usuario= "Select * from Usuario where nombre= :1"
            cursor.Execute(Validar_Usuario)
            usuario_existe=len(cursor.fetchall())>0
            
            if cliente_existe and usuario_existe:

                generar_boleta="insert into boleta (folio, cliente, usuario) values (:1 , :2 , :3)"
                cursor.execute(generar_boleta, (folio, cliente, usuario))
                self.db.connection.commit()
                print (f"boleta generada exitosamente")
                return True
        
            elif not cliente_existe:
                print (f"{cliente} no se encuentra ingresado")
                return False
            else:
                print (f"{usuario} no se encuentra la sesion")
                return False
        except Exception as e:
            print ("error al ingresar")
            return False
        finally:
            if cursor:
                cursor.close()
        
    def Editar_Boleta (self, folio:int, *datos:tuple)->bool:
        cursor=self.db.obtener_cursor()








class inventario():
    """
    se debe poder generar un inventario, actualizar, eliminar o leer lo del inventario
    """
    
    def __init__(self,nombre:str,precio:int,cantidad:int,precio_costo:int,):
        
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
        self.precio_costo=precio_costo
        
    def CrearItem (self, nombre, tipo, cantidad, precio_costo, )-> bool:
        cursor = self.db.obtener_cursor()
        
        try:
            Consulta_validacion = "select * from inventario where nombre= :1"
            cursor.Execute(Consulta_validacion,(nombre,))   
            """siempre se debe ir conectando con la base de datos creando el cursor"""
        
            if  len(cursor.fetchall()) >0:
                print (f"[ERROR]: ya existe este item en la lista{nombre}")
                return False
                
            else:
                consulta_insert="insert into inventario (nombre,precio,cantidad,precio_costo) values (1:, 2:, 3:, 4:)"
                cursor.Execute(consulta_insert)
                self.db.Connection.commit()
                print (f"[info]: {nombre} guardado correctamente ")
                return True 
            
        finally:
            if cursor:
                cursor.close()
                
    def EditarItem (self,nombre:str,*datos:tuple)-> bool:
        """debemos utilizar valores verdaderos y falsos para verificar si existe o no en la clase
        ademas debemos crear el cursor conectado a la db para verificarlos"""
        cursor= self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from inventario where nombre= :1"
            cursor.execute(consulta_validacion,(nombre,))
            
            if len(cursor.fetchall()) >0:
                if datos:
                    consulta_update = "update inventario set nombre = 1:, cantidad= 2:, tipo= 3:, precio_costo= 4: where nombre= 5:"
                    cursor.execute(consulta_update,(nombre,datos[0], datos[1],datos[2],nombre))
                    self.db.connection.commit()
                    print(f"[INFO]:{nombre} editado correctamente")
                    return True
                else:  
                    print (f"[ERROR]: sin datos ingresados para {nombre}")
                    return False 
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla de inventario ")
                return False
            
        except Exception as e:
            print (f"[ERROR]: Error al editar {nombre}->{e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def EliminarItem (self, nombre:str) -> bool:
        cursor=self.db.obtener_cursor()
        
        try:
            consulta_validacion=("select 1 from inventario where nombre = :1")
            cursor.execute(consulta_validacion, (nombre,))
            
            if len(cursor.fetchall)>0:
                consulta_delete="delete * from inventrario where nombre = :1"
                cursor.execute(consulta_delete (nombre,))
                self.db.Connection.commit()
                print(f"[INFO]: {nombre} se ha eliminado correctamente")
                return True
            else:
                print(f"[ERROR]: {nombre} no se ecuentra en la base de datos")
                return False
        except Exception as e:
            print(f"error al eliminar {nombre}->{e}")

            if cursor:
                cursor.close()
                