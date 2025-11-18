from objetos import inventario, habitacion, boleta

class cliente ():
    def __init__(self, nombre: str, telefono: int, nacionalidad: str, habitacion: int):
        self.nombre = nombre
        self. telefono = telefono
        self.nacionalidad = nacionalidad
        self.habitacion = habitacion

class recepcionista():
    def __init__(self, nombre: str, telefono: int, ubicacion: str):
        self.nombre = nombre
        self.telefono = telefono
        self. ubicacion = ubicacion