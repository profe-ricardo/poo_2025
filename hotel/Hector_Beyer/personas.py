from objetos import habitacion, comida

class chef():
    def __init__(self, nombre:str, id:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
    
    def tomar_pedidos():
        pass

class manager():
    def __init__(self, nombre:str, id:int, telefono:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion
    
    def abastecer_inventario():
        pass
    
    def guardar_opinion():
        pass
    
    def gestionar_trabajadores():
        pass


class recepcionista():
    def __init__(self, nombre:str, id:int, telefono:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion

    def comprobar_disponabilidad():
        pass

    def reservar_cuarto():
        pass

    def generar_boleta():
        pass
    
    def aceptar_comentario_cliente():
        pass

class personalAseo():
    def __init__(self, nombre:str, id:int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion

    def limpiar_cuarto():
        pass

class cliente():
    def __init__(self, nombre:str, id:int, telefono:int, direccion:str, habitacion:habitacion):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.habitacion = habitacion

    def check_in():
        pass

    def check_out():
        pass

    def pagar_boleta():
        pass

    def pedir_comida(self, pedido:list[comida]):
        for c in pedido:
            print(c.id)
            print(c.nombre)

    def subir_comentarios():
        pass