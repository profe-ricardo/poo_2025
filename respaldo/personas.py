from hotel.luis_carrasco.objetos import habitacion, comida


class chef():
<<<<<<<< HEAD:respaldo/personas.py
    def __init__(self, nombre:str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
        
    def tomar_pedido():
========
    def __init__(self, nombre:str, id:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
    
    def tomar_pedidos():
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
        pass
    
class manager():
    def __init__(self, nombre:str, id:int, telefono:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion
<<<<<<<< HEAD:respaldo/personas.py
        
========
    
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
    def abastecer_inventario():
        pass
    
    def guardar_opinion():
        pass
    
    def gestionar_trabajadores():
        pass
<<<<<<<< HEAD:respaldo/personas.py
    
    
class recepcinista():
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        
========


class recepcionista():
    def __init__(self, nombre:str, id:int, telefono:int, locacion:str):
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion
<<<<<<<< HEAD:respaldo/personas.py
        
    def habitacion_disponible():
        pass
    
    def reservar_habitacion():
========

    def comprobar_disponabilidad():
        pass

    def reservar_cuarto():
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
        pass
    
    def generar_boleta():
        pass
    
<<<<<<<< HEAD:respaldo/personas.py
    def aceptar_comentarios():
        pass
    
class personalAseo():    
    def __init__(self, nombre: str, id: int, locacion: str):
        
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
        
    def limpiar_habitacion():
========
    def aceptar_comentario_cliente():
        pass

class personalAseo():
    def __init__(self, nombre:str, id:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion

    def limpiar_cuarto():
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
        pass
        
        
    
class cliente():
<<<<<<<< HEAD:respaldo/personas.py
    def __init__(self, nombre: str, id: int, telefono: int, direccion: str, habitacion: habitacion):
        
========
    def __init__(self, nombre:str, id:int, telefono:int, direccion:str, habitacion:habitacion):
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.habitacion = habitacion
        
    def check_in():
        pass
    
    def chack_out():
        pass
    
    def pagar_boleta():
        pass
<<<<<<<< HEAD:respaldo/personas.py
    
    def pedir_comida(self, pedido: list [comida]):
        for c in pedido: 
            print (c.id)
            print
    
    def subir_comentario():
        pass
    
    
        
========

    def pedir_comida(self, pedido:list[comida]):
        for c in pedido:
            print(c.id)
            print(c.nombre)

    def subir_comentarios():
        pass
>>>>>>>> 06ef96b14140f1e22f0efe533015fb7f6e1b3c6a:hotel/Benjamin_Millalonco/personas.py
