class UsuarioView:
    """
        Vista del usuario, muestra información en pantalla.
    """
    @staticmethod
    def mostrar_usuarios(usuarios: list) -> None:
        """
            Recibe la lista de los usuarios.\n
            Si recibe al menos uno, mostrará la lista en consola.
        """
        if len(usuarios) > 0:
            print("\n- Lista de usuarios -")

            for u in usuarios:
                print(f"--- Nombre: {u['nombre']} | Telefono: {u['telefono']}")
        else:
            print("[ERROR]: Sin usuarios registrados")

class ClienteView:
    """
    Vista del cliente: muestra información en pantalla.
    """
    @staticmethod
    def mostrar_cliente(cliente: dict) -> None:
        print("\n- Datos del cliente -")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Nacionalidad: {cliente['nacionalidad']}")
        print(f"Habitación asignada: {cliente['habitacion']}")

    @staticmethod
    def mostrar_clientes(clientes: list) -> None:
        if clientes:
            print("\n- Lista de clientes -")
            for c in clientes:
                print(f"{c['nombre']} | {c['telefono']} | {c['nacionalidad']} | Habitación: {c['habitacion']}")
        else:
            print("[INFO]: No hay clientes registrados.")


class RecepcionistaView:
    """
    Vista del recepcionista: muestra información en pantalla.
    """
    @staticmethod
    def mostrar_recepcionista(recepcionista: dict) -> None:
        print("\n- Datos del recepcionista -")
        print(f"Nombre: {recepcionista['nombre']}")
        print(f"Teléfono: {recepcionista['telefono']}")
        print(f"Ubicación: {recepcionista['ubicacion']}")

    @staticmethod
    def mostrar_disponibilidad(habitacion_numero: int, disponible: bool) -> None:
        estado = "disponible" if disponible else "ocupada"
        print(f"[INFO]: Habitación {habitacion_numero} está {estado}.")

    @staticmethod
    def mostrar_reserva(cliente: dict, habitacion_numero: int) -> None:
        print(f"[INFO]: Habitación {habitacion_numero} asignada a cliente {cliente['nombre']}.")

    @staticmethod
    def mostrar_feedback(cliente: dict, mensaje: str) -> None:
        print(f"[INFO]: Feedback recibido de {cliente['nombre']}: '{mensaje}'")