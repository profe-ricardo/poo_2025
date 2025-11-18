import re
from hotel.Hector_Beyer.model.objetos_m import InventarioModel, HabitacionModel, BoletaModel

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
        Controlador de habitacion, contiene métodos que utilizan el modelo.
    """

    def __init__(self, modelo: HabitacionModel):
        self.modelo = modelo

    def registrar_habitacion(self, numero_habitacion:int, cantidad_personas:int, estado:str):
        """
            Realiza registro dentro de BD usando funciones de modelo.

            params
            - numero_habitacion : Numero de habitacion
            - cantidad_personas : Cantidad de personas en habitacion
            - estado : Disponible / No disponibe

            returns Boolean
        """

        if patron.search(numero_habitacion) or patron.search(cantidad_personas) or patron.search(estado):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(numero_habitacion, cantidad_personas, estado)
        
class BoletaController:
    """
        Controlador de boleta, contiene métodos que utilizan el modelo.
    """

    def __init__(self, modelo: BoletaModel):
        self.modelo = modelo

    def registrar_boleta(self, folio:int, usuario:int, cliente:str):
        """
            Realiza registro dentro de BD usando funciones de modelo.

            params
            - folio : Numero de boleto
            - usuario : Usuario que ingreso boleta
            - cliente : Cliente que recibio boleta

            returns Boolean
        """

        if patron.search(folio) or patron.search(usuario) or patron.search(cliente):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(folio, usuario, cliente)
    
    def editar(self):
        self.modelo.editar_item()

