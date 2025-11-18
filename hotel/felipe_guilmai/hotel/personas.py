class chef():
    def __init__(self,nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion
        pass
    
class manager():
    def __init__(self, nombre: str, id: int, telefono: int, locacion:str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono 
        self.locacion = locacion

class personalAseo():
    """"""
class cliente():
    def __init__(self, nombre: str, id: int, telefono: int, direccion: str, habitacion: int):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.habitacion = habitacion
    def check_in():
        pass
    def check_out():
        pass
    def paybill():
        pass

class recepcionista():
    def __init__(self, name: str, id: int, telefono: int, locacion: str):
        self.name = name
        self.id = id 
        self.telefono = telefono
        self.locacion = locacion 

    def checkRoomAvalibility():
        pass

    def BookRoom():
        pass

    def GenerateBill():
        pass
    
    def AcceptCustomerFeedback():
        pass

print(cliente.__dict__)