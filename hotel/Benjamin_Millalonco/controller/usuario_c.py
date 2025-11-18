# controller/usuario_c.py
from model.usuario_m import UsuarioModel

class UsuarioController:
    def __init__(self, db):
        self.model = UsuarioModel(db)

    def crear(self, nombre: str, telefono: str, ubicacion: str, password: str) -> int | None:
        # Validaciones básicas antes de crear
        if not nombre or not telefono or not password:
            print("[WARN] nombre, telefono y password son obligatorios.")
            return None

        # Podrías comprobar aquí si ya existe un usuario con ese teléfono
        existente = self.model.obtener_por_telefono(telefono)
        if existente:
            print("[WARN] Ya existe un usuario con ese teléfono.")
            return None

        nuevo_id = self.model.crear_usuario(nombre, telefono, ubicacion, password)
        if nuevo_id:
            print(f"[INFO] Usuario creado con id={nuevo_id}")
        else:
            print("[ERROR] No se pudo crear el usuario.")
        return nuevo_id

    def login(self, telefono: str, password: str) -> bool:
        if not telefono or not password:
            print("[WARN] telefono y password son obligatorios.")
            return False

        ok = self.model.verificar_password(telefono, password)
        if ok:
            print("[INFO] Login correcto.")
        else:
            print("[INFO] Login inválido.")
        return ok
