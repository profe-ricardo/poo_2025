import re 
from model.objetos_m import InventarioModel
from model.objetos_m import HabitacionModel
from model.objetos_m import BoletaModel


sus_keys = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(sus_keys), re.IGNORECASE)

class InventarioController:
    def __init__(self, model: InventarioModel):
        self.model = model

    def registrar_inventario(self, nombre: str, tipo: str, cantidad: int, precio_costo: float):

        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.model.guardar_item(nombre, tipo, cantidad, precio_costo)

class HabitacionController:
    def __init__(self, model: HabitacionModel):
        self.model = model

    def registrar_habitacion(self, numero: int, huespedes: int, estado: str):
        
        if patron.search(estado):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.model.guardar_item(numero, huespedes, estado)
        
class BoletaModel:
    def __init__(self, model : BoletaModel):
        self.model = model

    def registrar_boleta(self, folio: int, cliente: str, usuario:str):

        if patron.search(cliente) or patron.search(usuario):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.model.guardar_item(folio, cliente, usuario)