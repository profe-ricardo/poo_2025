import re 
from acumulativa3.model.objetos_m import InventarioModel


sus_keys = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(sus_keys), re.IGNORECASE)

class InventarioController:
    def __init__(self, modelo: InventarioModel):
        self.modelo = modelo

    def registrar_inventario(self, nombre: str, tipo: str, cantidad: int, precio_costo: float):

        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(nombre, tipo, cantidad, precio_costo)
