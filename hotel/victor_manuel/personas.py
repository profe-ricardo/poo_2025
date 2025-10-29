from objetos import comida, habitacion, boleta, inventario


class chef():
    def _init_(self, nomnbre:str,  id:str, int:str, locacion:str):
        self.nombre = nomnbre     #nombre del chef
        self.id = id              #identificacion del chef
        self.int = int            #¿que es int?
        self.locacion = locacion  #ubicacion del chef en el hotel
    
    def preparar_comida():
        pass

class manager():
    def _init_(self, nombre:str, id:str, int:str, telefono:str, locacion:str):
        self.nombre = nombre     #nombre del manager
        self.id = id             #identificacion del manager
        self.int = int           #¿que es int?
        self.telefono = telefono
        self.locacion = locacion
    
    def abastecer_inventario():
        pass

    def guardar_opinion():
        pass

    def gestionar_personal():
        pass
   

class recepcionistas():
    def _init_(self, nombre:str, id:str, telefono:str, locacion:str):
        self.nomrbre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion
    
    def comprobar_habitacion():
        pass

    def asignar_habitacion():
        pass

    def generar_boleta():
        pass

    def aceptar_criticas():
        pass


class personalAseo():
    def _init_(self, nombre:str, id:str, int:str, locacion:str):
        self.nombre = nombre
        self.id = id 
        self.int = int 
        self.locacion = locacion
    
    def limpiar_habitacion():
        pass


class cliente():
    def _init_ (self, nombre:str, id:str, int:str, telefono:str, direccion:str, habitacion:str):
        self.nombre  = nombre #nombre del cliente
        self.id = id #identificacion del cliente
        self.int = int
        self.telefono = telefono #numero del cliente
        self.dereccion = direccion #direccion del cliente
        self.habitacion = habitacion #habitacion asignada al cliente 
    
    def chek_in():
        pass

    def chek_out():
        pass

    def pedir_comida(self, pedido:list[comida]): # pedido es una lista de comidas 
        for c in pedido:
            print (c.id) 
            print (c.nombre)

    def pedir_boleta():
        pass

    def pagar_boleta():
        pass

    def agregar_criticas():
        pass

    