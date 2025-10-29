from hotel.Matias_Soto.Objetos import Habitacion, Comida

class Chef(): 
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.Locacion = locacion
    
    def Tomar_Pedidos():
        pass

class Manager():
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.Locacion = locacion
    
    def Abastecer_Inventario():
        pass
    
    def Guardar_Opinion():
        pass

    def Control_trabajadores():
        pass

class Recepcionista():
    def __init__(self, nombre: str, id: int, telefono: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.Locacion = locacion
    
    def Habitaciones_Disponibles():
        pass

    def Libro_Habitaciones():
        pass

    def Generar_Boleta():
        pass

    def Recibir_Opinion():
        pass


class Personal_Aseo():
    def __init__(self, nombre: str, id: int, locacion: str):
        self.nombre = nombre
        self.id = id
        self.Locacion = locacion
    
    def Limpiar_habitacion():
        pass

class Clientes():
    def __init__(self, nombre: str, id: int, telefono: int, direccion: str, habitacion: Habitacion):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.habitacion = habitacion
    
    def check_in ():
        pass
    
    def check_out():
        pass

    def PagarBoleta():
        pass
    
    def OrdenarComida(self, pedido: list[Comida]):
        for c in pedido:
            print(c.nombre)
    
    def Subir_Comentario():
        pass

    

