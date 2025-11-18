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

class ClientView:

    @staticmethod
    def View_client(Client: list) -> None:

        if len(Client) > 0:
            print(" - Lista de clientes -")

            for c in Client:
                print(f"--- Name: {c['Name']} | Phone: {c['Phone']} | Location: {c['Location']} | Room: {c['Room']}")
        
        else:
            print("[####] Sin clientes registrados")

class ReceptionView:

    @staticmethod
    def View_reception(Reception: list) -> None:

        if len(Reception) > 0:
            print(" - Lista de recepciones -")

            for r in Reception:
                print(f" --- Name: {r['Name']} | Phone: {r['Phone']} | Location: {r['Location']} | Room: {r['Room']} | Location: {r['Location']}")
        else:
            print("[####] Sin recepciones registradas")