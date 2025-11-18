class InventarioView:
    """
    Vista del inventario: muestra información en pantalla.
    """
    @staticmethod
    def mostrar_item(item: dict) -> None:
        print("\n- Datos del inventario -")
        print(f"Nombre: {item['nombre']} | Tipo: {item['tipo']} | Cantidad: {item['cantidad']} | Precio costo: {item['precio_costo']}")

    @staticmethod
    def mostrar_items(items: list) -> None:
        if items:
            print("\n- Lista de inventario -")
            for i in items:
                print(f"{i['nombre']} | {i['tipo']} | Cantidad: {i['cantidad']} | Precio costo: {i['precio_costo']}")
        else:
            print("[INFO]: No hay ítems registrados.")


class HabitacionView:
    """
    Vista de habitaciones: muestra información en pantalla.
    """
    @staticmethod
    def mostrar_habitacion(habitacion: dict) -> None:
        print("\n- Datos de la habitación -")
        print(f"Número: {habitacion['numero']}")
        print(f"Capacidad: {habitacion['cantidad_personas']}")
        print(f"Ubicación: {habitacion['ubicacion']}")
        print(f"Estado: {'Disponible' if habitacion['estado'] else 'Ocupada'}")

    @staticmethod
    def mostrar_estado(numero: int, disponible: bool) -> None:
        estado = "disponible" if disponible else "ocupada"
        print(f"[INFO]: Habitación {numero} está {estado}.")


class BoletaView:
    """
    Vista de boletas: muestra información en pantalla.
    """
    @staticmethod
    def mostrar_boleta(boleta: dict) -> None:
        print("\n- Datos de la boleta -")
        print(f"Folio: {boleta['folio']}")
        print(f"Cliente: {boleta['cliente']}")
        print(f"Usuario: {boleta['usuario']}")

    @staticmethod
    def mostrar_boletas(boletas: list) -> None:
        if boletas:
            print("\n- Lista de boletas -")
            for b in boletas:
                print(f"Folio: {b['folio']} | Cliente: {b['cliente']} | Usuario: {b['usuario']}")
        else:
            print("[INFO]: No hay boletas registradas.")
