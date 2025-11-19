<<<<<<< HEAD:hotel/Chr_vargas/aaa/personas.py
from objetos import habitacion, comida
=======
<<<<<<< Updated upstream
from hotel.Luis_Antivil.clases.objetos import habitacion, comida
=======
from objetos import habitacion, comida
>>>>>>> Stashed changes
>>>>>>> 04591e085533c427693f7e9ddff3f6e5970edea6:hotel/Chr_vargas/personas.py

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
        pass

    def reservar_habitaciones():
        pass

    def generar_boleta():
        pass

    def aceptar_comentarios():
        pass



class personal_aseo():
    def __init__(self,nombre:str,id:int,locacion:str):
        self.nombre=nombre
        self.id=id
        self.locacion=locacion

    def limpiar_habitacion():
        pass




class cliente():
    def __init__(self,nombre:str,id:int,telefono:int,direccion:str,habitacion:habitacion):
        self.nombre=nombre
        self.id = id
        self.telefono=telefono
        self.direccion=direccion
        self.habitacion=habitacion 

    def check_in():
        pass

    def check_out():
        pass

    def pagar_boleta():
        pass

    def pedir_comida(self,pedido: list[comida]):
        for c in pedido:
            print(c.nombre)

    def subir_comentario():
        pass
