<<<<<<< HEAD
from hotel.Luis_Antivil.objetos import habitacion, comida

class chef():
    def __init__(self, nombre:str,id:int,locacion:str):
        self.nombre=nombre
        self.id=id
        self.locacion=locacion

    def tomar_pedidos():
        pass



class manager():
    def __init__(self, nombre: str, id:int, telefono:int, locacion:str):    
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




class recepcionista():
    def __init__(self,nombre:str,id:int,telefono:int,locacion:str):
        self.nombre=nombre
        self.id=id
        self.telefono=telefono
        self.locacion=locacion

    def comprobar_disponibilidad():
=======
from objetos import habitacion, comida

class chef():
    def __init__(self,nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion

    def tomar_orden():
        pass

class manager():
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion 
    
    def copiar_inventario():
        pass

    def registro_quejas():
        pass

    def control_trabajadores():
        pass

class recepcionista():
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion

    def habitaciones_disponibles():
>>>>>>> f04b3d3321f83c58da4f68ea72da9cd1194155eb
        pass

    def reservar_habitaciones():
        pass

    def generar_boleta():
        pass

<<<<<<< HEAD
    def aceptar_comentarios():
        pass



class personal_aseo():
    def __init__(self,nombre:str,id:int,locacion:str):
        self.nombre=nombre
        self.id=id
        self.locacion=locacion
=======
    def recibir_opinion():
        pass

class personalAseo():
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
>>>>>>> f04b3d3321f83c58da4f68ea72da9cd1194155eb

    def limpiar_habitacion():
        pass

<<<<<<< HEAD



class cliente():
    def __init__(self,nombre:str,id:int,telefono:int,direccion:str,habitacion:habitacion):
        self.nombre=nombre
        self.id = id
        self.telefono=telefono
        self.direccion=direccion
        self.habitacion=habitacion 
=======
class cliente():
    def __init__(self,nombre: str, id: int, telefono:int, direccion: str, habitacion: habitacion):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = habitacion 
        self.habitacion = habitacion 
>>>>>>> f04b3d3321f83c58da4f68ea72da9cd1194155eb

    def check_in():
        pass

    def check_out():
        pass

<<<<<<< HEAD
    def pagar_boleta():
=======
    def Pagar_boleta():
>>>>>>> f04b3d3321f83c58da4f68ea72da9cd1194155eb
        pass

    def pedir_comida(self,pedido: list[comida]):
        for c in pedido:
            print(c.nombre)

<<<<<<< HEAD
    def subir_comentario():
        pass
=======
    def subir_comentarios():
        pass
    
>>>>>>> f04b3d3321f83c58da4f68ea72da9cd1194155eb
