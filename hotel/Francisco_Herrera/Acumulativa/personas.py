class CLIENTE():
    def __init__(self, nombre: str, telefono: int,nacionalidad: str, habitacion: int):
        self.nombre = nombre
        self.telefono = telefono
        self.habitacion = habitacion
        self.nacionalidad = nacionalidad


class RECEPCIONISTA():
    def __init__(self, nombre: str, telefono: int, locacion: str):
        self.nombre = nombre
        self.telefono = telefono
        self.locacion = locacion


class PERSONALASEO():
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion

    def limpiar_habitacion():
        pass

class CHEF():
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.locacion = locacion

    def tomar_pedidos():
        pass

class manager():
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.locacion = locacion