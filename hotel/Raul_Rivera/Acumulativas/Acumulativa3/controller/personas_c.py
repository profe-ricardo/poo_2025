from config.db_config import ConexionOracle
from model.personas_m import UsuarioModel, clienteModel, recepcionistaModel


class UsuarioController:
    """
        Controlador del usuario.
        Métodos para registrar y mostrar usuarios.
    """
    def __init__(self, modelo: UsuarioModel):
        self.modelo = modelo

    def registrar_usuario(self, nombre: str, telefono: int) -> bool:
        if not nombre or not telefono:
            print("[ERROR]: Datos faltantes para registro de usuario.")
            return False
        return self.modelo.crear(nombre, telefono)

    def listar_usuarios(self) -> list:
        usuarios = self.modelo.mostrar_todos()
        if usuarios:
            return [{"nombre": u[0], "telefono": u[1]} for u in usuarios]
        return []


class ClienteController:
    """
        Controlador del cliente.
        Maneja operaciones relacionadas con clientes.
    """
    def __init__(self, modelo: clienteModel):
        self.modelo = modelo

    def registrar_cliente(self, nombre: str, telefono: int, nacionalidad: str, habitacion) -> clienteModel:
        if not nombre or not telefono or not nacionalidad or not habitacion:
            print("[ERROR]: Datos faltantes para registro de cliente.")
            return None
        cliente = clienteModel(nombre, telefono, nacionalidad, habitacion)
        print(f"[INFO]: Cliente '{nombre}' registrado correctamente en habitación {habitacion.numero}.")
        return cliente

    def mostrar_cliente(self, cliente: clienteModel) -> dict:
        return {
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "nacionalidad": cliente.nacionalidad,
            "habitacion": cliente.habitacion.numero
        }


class RecepcionistaController:
    def __init__(self, modelo: recepcionistaModel):
        self.modelo = modelo

    def registrar_recepcionista(self) -> bool:
        return self.modelo.guardar()

    def mostrar_recepcionista(self) -> dict:
        return {
            "nombre": self.modelo.nombre,
            "telefono": self.modelo.telefono,
            "ubicacion": self.modelo.ubicacion
        }

    def verificar_disponibilidad(self, habitacion) -> bool:
        return self.modelo.check_room_availability(habitacion)

    def reservar_habitacion(self, cliente: clienteModel) -> bool:
        return self.modelo.reservar_habitacion(cliente)

    def generar_boleta(self, folio: int, cliente: clienteModel) -> bool:
        return self.modelo.generar_boleta(folio, cliente)

    def aceptar_feedback(self, cliente: clienteModel, mensaje: str) -> bool:
        return self.modelo.accept_customer_feedback(cliente, mensaje)