from Model.person_M import UsuarioModel,clientMoldel,Reception,ReceptionModel

class UsuarioController:
    """
        Controlador del usuario.\n
        Métodos para registrar y mostrar usuarios.
    """
    def __init__(self, model: UsuarioModel):
        self.model = model

    def registrar_usuario(self, nombre: str, telefono: int) -> bool:

        if not nombre or not telefono:
            print("[Error]: Datos faltantes para registro de usuario.")
            return False
        
        return self.modelo.crear(nombre, telefono)
        
    def listar_usuarios(self) -> list:
        """
            Muestra los usuarios registrados en BD.\
            returns Lista vacía si es que no hay usuarios, o lista de usuarios registrados.
        """
        usuarios = self.modelo.mostrar_todos()

        if len(usuarios) > 0:
            return [{ "nombre": u[0], "telefono": u[1] } for u in usuarios]
        else:
            return []
        
class Clientcontroller:

    def __init__(self, Model: clientMoldel):
        self.Model = Model

    def Register_Client(self, Name: str, Phone: int, Location: str, Room: str) -> bool:

        if not Name or not Phone or not Location or not Room:
            print("[####] Hacen Falta datos en el cliente")
            return False
        
        return self.Model.register_client(Name, Phone, Location, Room)

    def List_Client(self) -> list:

        Client = self.model.display_all()
    
        if len(Client) > 0:
            return [{"Name": c[0],"Phone": c[1], "Location": c[2], "Room": c[3]} for c in Client]
        
        else:
            return []
