import re
from hotel.profe_ricardo.model.objetos_m import InventarioModel

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class InventarioController:
    """
        Controlador del inventario, contiene métodos que utilizan el modelo.
    """

    def __init__(self, modelo: InventarioModel):
        self.modelo = modelo

    def registrar_inventario(self, nombre: str, tipo: str, cantidad: int, precio_costo: float):
        """
            Realiza registro dentro de BD usando funciones de modelo.

            params
            - nombre : nombre del item
            - tipo : tipo del item
            - cantidad : stock disponible
            - precio_costo : valor de compra

            returns Boolean
        """

        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(nombre, tipo, cantidad, precio_costo)