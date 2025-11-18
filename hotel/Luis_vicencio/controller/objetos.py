from model.objetos import InventarioModel, HabitacionModel, BoletaModel

class HabitacionController():
    def __init__(self, modelo: HabitacionModel):
        self.modelo = modelo
    
    def registrar_habitacion(self, numero: int, cantidad_de_personas: int, estado: str) -> bool:
        if not numero or not cantidad_de_personas or not estado :
            print ("[ERROR]: Datos faltantes para registro de Habitacion")
            return False
        return self.modelo.crear(numero, cantidad_de_personas, estado)
    
    def listas_Habitaciones(self) -> list:
        habitaciones = self.modelo.mostrar_todos()
        if len(habitaciones) > 0:
            return [{"numero": u[0], "cantidad_de_personas": u[1], "estado": u[2]} for u in habitaciones]
        else:
            return []
        
class InventarioController():
    def __init__(self, modelo:InventarioModel):
        self.modelo = modelo
        
    def registrar_inventario(self, nombre: str, tipo: str, cantidad: int, precio_costo: int ) -> bool:
        if not nombre or not tipo or not cantidad or not precio_costo:
            print("[ERROR]: Datos faltantes para registro de inventario")
            return False
        return self.modelo.crear(nombre, tipo, cantidad, precio_costo)
    
    def listar_inventario(self) -> list:
        inventario = self.modelo.mostrar_todos()
        if len(inventario) > 0:
            return [{"nombre": u[0], "tipo": u[1], "cantidad" : u[2], "precio costo": u[3]} for u in inventario]
        else:
            return[]
        
class BoletaController():
    def __init__(self, modelo: BoletaModel):
        self.modelo = modelo
        
    def registrar_boleta(self, folio: int, cliente: str) -> bool:
        if not folio or not cliente:
            print("[ERROR]: Datos faltantes para emitir boleta")
            return False
        return self.modelo.crear(folio, cliente)
    
    def listar_Boletas(self) -> list:
        boletas = self.modelo.mostrar_todos()
        if len(boletas) > 0:
            return [{"folio": u[0], "cliente": u[1]} for u in boletas]
        else:
            return []