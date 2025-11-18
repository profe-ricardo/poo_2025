import re
from model.inventario_m import InventarioModel

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class InventarioController:
    def __init__(self, modelo: InventarioModel):
        self.modelo = modelo

    def registrar_inventario(self, nombre: str, tipo: str, cantidad: int, precio_costo: float):
        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar código SQL en los string.")
            return False
        return self.modelo.guardar_item(nombre, tipo, cantidad, precio_costo)

    def editar_inventario(self, nombre_original: str, nuevo_nombre: str, tipo: str, cantidad: int, precio_costo: float):
        if patron.search(nuevo_nombre) or patron.search(tipo):
            print("[ERROR]: Entradas inválidas.")
            return False
        return self.modelo.editar_item(nombre_original, nuevo_nombre, tipo, cantidad, precio_costo)

    def listar_inventario(self):
        return self.modelo.mostrar_items()

    def eliminar_inventario(self, nombre: str):
        return self.modelo.eliminar_item(nombre)
