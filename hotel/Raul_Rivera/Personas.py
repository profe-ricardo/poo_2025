from Objetos import Habitacion, Comida

class Chef():
    """"""
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre=nombre
        self.id=id
        self.locacion=locacion
    
    def tomar_pedidos():
        pass

class Manager():
    """"""
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre=nombre
        self.id=id
        self.telefono=telefono
        self.locacion=locacion
    
    def abastecer_inventario():
        pass

    def guardar_opinion():
        pass

    def gestionar_trabajadores():
        pass

class Recepcionista():
    """"""
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre=nombre
        self.id=id
        self.telefono=telefono
        self.locacion=locacion
    
    def ver_habitacion_disponible():
        pass

    def reservar_habitacion():
        pass

    def generar_boleta():
        pass

    def aceptar_comentarios():
        pass

class personalAseo():
    """"""
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre=nombre
        self.id=id
        self.locacion=locacion
    
    def limpiar_habitacion():
        pass

class cliente():
    """clase cliente"""
    def __init__(self, nombre: str, id: int, telefono: int, direccion: str, habitacion: Habitacion):
        self.nombre=nombre
        self.id=id
        self.telefono=telefono
        self.direccion=direccion
        self.habitacion= habitacion

    def check_in():
        pass

    def check_out():
        pass
    
    def pagar_boleta():
        pass
    
    def pedir_comida(self, pedido: list[Comida]):
        for c in pedido:
            print(c.id)
            print(c.nombre)

    def subir_comentarios():
        pass
