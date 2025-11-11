from Habitacion import habitacion
class cliente():

    def __init__(self,nombre:str, telefono:int,nacionalidad:str, habitacion:habitacion):
        super().__init__(habitacion)
        self.nombre=nombre
        self.telefono=telefono
        self.nacionalidad=nacionalidad
        self.habitacion=habitacion
        