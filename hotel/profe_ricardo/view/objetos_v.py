class InventarioView:
    """
        Vista del inventario
    """
    @staticmethod
    def mostrar_inventario(inventario: list) -> None:
        """
            Recibe la lista del inventario y muestra lo que contiene.
        """

        if len(inventario) > 0:
            print("\n[INFO]:- Inventario -")

            for i in inventario:
                print(f"[INFO]:--- Nombre: {i['nombre']} | Tipo: {i['tipo']} | Cantidad: {i['cantidad']} | Precio: {i['precio_costo']}")
        else:
            print("[ERROR]: Sin registro en inventario.")