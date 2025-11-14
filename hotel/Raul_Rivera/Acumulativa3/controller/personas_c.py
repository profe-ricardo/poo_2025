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
    """
        Controlador del recepcionista.
        Maneja operaciones relacionadas con recepcionistas.
    """
    def __init__(self, modelo: recepcionistaModel):
        self.modelo = modelo

    def registrar_recepcionista(self, nombre: str, telefono: int, ubicacion: str, conexion: ConexionOracle) -> recepcionistaModel:
        if not nombre or not telefono or not ubicacion:
            print("[ERROR]: Datos faltantes para registro de recepcionista.")
            return None
        recepcionista = recepcionistaModel(nombre, telefono, ubicacion, conexion)
        print(f"[INFO]: Recepcionista '{nombre}' registrado correctamente en ubicación {ubicacion}.")
        return recepcionista

    def verificar_disponibilidad(self, recepcionista: recepcionistaModel, habitacion) -> bool:
        disponible = recepcionista.check_room_availability(habitacion)
        estado = "disponible" if disponible else "ocupada"
        print(f"[INFO]: Habitación {habitacion.numero} está {estado}.")
        return disponible
    