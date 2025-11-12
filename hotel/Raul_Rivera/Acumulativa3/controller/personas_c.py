from model.personas_m import UsuarioModel
class UsuarioController:
    """
        Controlador del usuario.\n
        Métodos para registrar y mostrar usuarios.
    """
    def __init__(self, modelo: UsuarioModel):
        self.modelo = modelo

    def registrar_usuario(self, nombre: str, telefono: int) -> bool:
        """
            Recibe nombre y telefono, realiza registro en BD.\n
            returns Boolean
        """
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