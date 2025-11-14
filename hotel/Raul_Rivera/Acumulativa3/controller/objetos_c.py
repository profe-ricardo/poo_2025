import re
from model.objetos_m import InventarioModel, habitacionModel, boletaModel

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

    def registrar_inventario(self, nombre: str, tipo: str, cantidad: int, precio_costo: float) -> bool:
        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar código SQL en los string.")
            return False
        return self.modelo.guardar_item(nombre, tipo, cantidad, precio_costo)


class HabitacionController:
    """
        Controlador de habitaciones, coordina acciones sobre habitacionModel.
    """
    def __init__(self, modelo: habitacionModel):
        self.modelo = modelo

    def registrar_habitacion(self, numero: int, cantidad_personas: int, ubicacion: str, estado: bool) -> bool:
        cursor = None
        try:
            cursor = self.modelo.conexion.obtener_cursor()
            consulta = "insert into habitaciones (numero, cantidad_personas, ubicacion, estado) values (:1, :2, :3, :4)"
            cursor.execute(consulta, (numero, cantidad_personas, ubicacion, estado))
            self.modelo.conexion.connection.commit()
            print(f"[INFO]: Habitación {numero} registrada correctamente.")
            return True
        except Exception as e:
            print(f"[ERROR]: No se pudo registrar habitación {numero} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_habitaciones(self) -> list:
        cursor = None
        try:
            cursor = self.modelo.conexion.obtener_cursor()
            consulta = "select numero, cantidad_personas, ubicacion, estado from habitaciones"
            cursor.execute(consulta)
            datos = cursor.fetchall()
            return datos
        except Exception as e:
            print(f"[ERROR]: Error al obtener habitaciones -> {e}")
            return []
        finally:
            if cursor:
                cursor.close()


class BoletaController:
    """
        Controlador de boletas, coordina acciones sobre boletaModel.
    """
    def __init__(self, modelo: boletaModel):
        self.modelo = modelo

    def generar_boleta(self) -> str:
        return (
            f"Folio: {self.modelo.folio}\n"
            f"Cliente: {self.modelo.cliente.nombre}\n"
            f"Usuario: {self.modelo.usuario.nombre}"
        )
    def mostrar_boleta(self) -> dict:
        return {
            "folio": self.modelo.folio,
            "cliente": self.modelo.cliente.nombre,
            "usuario": self.modelo.usuario.nombre
        }