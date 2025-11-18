from model.habitacion_m import HabitacionModel

class HabitacionController:
    def __init__(self, conexion):
        self.modelo = HabitacionModel(conexion)

    def crear(self, numero, capacidad, estado="disponible"):
        return self.modelo.crear_habitacion(numero, capacidad, estado)

    def listar(self):
        habitaciones = self.modelo.mostrar_habitaciones()
        for h in habitaciones:
            print(f"N°{h[0]} | Capacidad: {h[1]} | Estado: {h[2]}")
        return habitaciones

    def actualizar_estado(self, numero, nuevo_estado):
        return self.modelo.actualizar_estado(numero, nuevo_estado)
