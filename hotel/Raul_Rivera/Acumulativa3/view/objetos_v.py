class BoletaView:
    """
        Vista de las boletas, muestra información en pantalla.
    """
    @staticmethod
    def mostrar_boleta(boleta) -> None:
        """
            Recibe una boleta y muestra sus datos en consola.
        """
        print("\n- Datos de la boleta -")
        print(f"Folio: {boleta.folio}")
        print(f"Cliente: {boleta.cliente.nombre}")
        print(f"Usuario: {boleta.usuario.nombre}")
