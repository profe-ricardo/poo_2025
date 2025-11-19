from objetos import comida, habitacion, boleta, inventario


class chef():
    def _init_(self, nomnbre:str,  id:int, locacion:str):
        self.nombre = nomnbre     #nombre del chef
        self.id = id              #identificacion del chef
        self.locacion = locacion  #ubicacion del chef en el hotel
    
    def preparar_comida():
        pass

class manager():
    def _init_(self, nombre:str, id:int, telefono:str, locacion:str):
        self.nombre = nombre     #nombre del manager
        self.id = id             #identificacion del manager
        self.telefono = telefono
        self.locacion = locacion
    
    def abastecer_inventario(): #el manager se hace cargo de abastecer el inventario
        pass

    def guardar_opinion():
        pass

    def gestionar_personal():
        pass
   

class recepcionistas():
    def _init_(self, nombre:str, id:int, telefono:str, locacion:str):
        self.nomrbre = nombre    #nombre del recepcionista
        self.id = id             #identificacion del recepcionista 
        self.telefono = telefono #telefono del recepcionista 
        self.locacion = locacion #locacion de recepcionista en el hotel
    
    def comprobar_habitacion():  #comprobar si hay habitaciones disponibles
        pass

    def asignar_habitacion():    #asignar habitaciones a los clientes
        pass

    def generar_boleta():        #generar boleta de consumo
        pass

    def aceptar_criticas():      #aceptar criticas de los clientes
        pass


class personalAseo():
    def _init_(self, nombre:str, id:int, locacion:str):
        self.nombre = nombre     #nombre del personal de limpiesa
        self.id = id             #identificacion del personal de limpieza
        self.locacion = locacion #locacion del personal de limpiesa en el hotel
    
    def limpiar_habitacion():
        pass


class cliente():
    def _init_ (self, nombre:str, id:str, telefono:str, direccion:str, habitacion:str):
        self.nombre  = nombre         #nombre del cliente
        self.id = id                  #identificacion del cliente
        self.telefono = telefono      #numero del cliente
        self.dereccion = direccion    #direccion del cliente
        self.habitacion = habitacion  #habitacion asignada al cliente 
    
    def chek_in(): #registrar la entrada del cliente
        pass

    def chek_out(): #registrar la salida del cliente
        pass

    def pedir_comida(self, pedido:list[comida]): # pedido es una lista de comidas 
        for c in pedido: #el ciclo recorre cada comida en el pedido
            print (c.id)  #el print muestra el id de cada comida
            print (c.nombre) #el print muestra el nombre de la comida

    def pedir_boleta(): #se genera la boleta de consumo
        pass

    def pagar_boleta(): #el cliente paga la boleta generada
        pass

    def agregar_criticas(): #el cliente hace criticas o sugerencias sobre el servicio
        pass

    