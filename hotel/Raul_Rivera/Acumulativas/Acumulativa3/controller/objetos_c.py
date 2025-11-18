import re
from model.objetos_m import InventarioModel, habitacionModel, BoletaModel

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

class HabitacionController:
    """
        Controlador de habitaciones, coordina acciones sobre habitacionModel.
    """
    def __init__(self, modelo: habitacionModel):
        self.modelo = modelo

    def registrar_habitacion(self) -> bool:
        return self.modelo.guardar()

    def cambiar_estado(self, nuevo_estado: bool) -> bool:
        return self.modelo.cambiar_estado(nuevo_estado)

    def mostrar_habitacion(self) -> dict:
        return self.modelo.mostrar()

    def es_disponible(self) -> bool:
        return self.modelo.es_disponible()


from model.objetos_m import BoletaModel

class BoletaController:
    """
    Controlador de boletas. Coordina la visualización de boletas.
    """
    def __init__(self, modelo: BoletaModel):
        self.modelo = modelo

    def mostrar_boleta(self) -> dict:
        """
        Devuelve los datos de la boleta como diccionario.
        """
        return self.modelo.mostrar()

    def imprimir_boleta(self) -> None:
        """
        Muestra los datos de la boleta en consola.
        """
        self.modelo.imprimir()
