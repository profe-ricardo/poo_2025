from config.dbconfig import ConexionOracle
from utils.hash import HashUtil


class Usuario:
    """
    Modelo de Usuario para autenticación.
    """

    def __init__(self, db: ConexionOracle, usuario_id=None, username=None, password_hash=None, rol=None):
        self.db = db
        self.usuario_id = usuario_id
        self.username = username
        self.password_hash = password_hash
        self.rol = rol

    # -----------------------------------------
    # GUARDAR USUARIO (REGISTRO)
    # -----------------------------------------
    def save(self) -> bool:
        """
        Guarda el usuario en la BD. Asume que password_hash ya está hasheado.
        """
        try:
            cursor = self.db.obtener_cursor()

            sql = """
                INSERT INTO usuarios (username, password_hash, rol)
                VALUES (:1, :2, :3)
            """

            cursor.execute(sql, (self.username, self.password_hash, self.rol))
            self.db.connection.commit()
            return True
        
        except Exception as e:
            print("[ERROR Usuario.save]:", e)
            return False

    # -----------------------------------------
    # CARGAR UN USUARIO POR USERNAME
    # -----------------------------------------
    def load_by_username(self, username: str):
        """
        Carga un usuario desde la BD por el username.
        """
        try:
            cursor = self.db.obtener_cursor()

            sql = """
                SELECT usuario_id, username, password_hash, rol
                FROM usuarios
                WHERE username = :1
            """

            cursor.execute(sql, [username])
            row = cursor.fetchone()

            if row:
                return Usuario(
                    db=self.db,
                    usuario_id=row[0],
                    username=row[1],
                    password_hash=row[2],
                    rol=row[3]
                )
            return None
        
        except Exception as e:
            print("[ERROR Usuario.load_by_username]:", e)
            return None

    # -----------------------------------------
    # LISTAR TODOS LOS USUARIOS
    # -----------------------------------------
    def list(self):
        """
        Retorna una lista de todos los usuarios en la BD.
        """
        usuarios = []

        try:
            cursor = self.db.obtener_cursor()

            cursor.execute("""
                SELECT usuario_id, username, password_hash, rol 
                FROM usuarios
            """)

            for row in cursor.fetchall():
                usuarios.append(
                    Usuario(
                        db=self.db,
                        usuario_id=row[0],
                        username=row[1],
                        password_hash=row[2],
                        rol=row[3]
                    )
                )

            return usuarios

        except Exception as e:
            print("[ERROR Usuario.list]:", e)
            return []

    # -----------------------------------------
    # VALIDAR LOGIN
    # -----------------------------------------
    def verify_login(self, username: str, password: str) -> "Usuario | None":
        """
        Verifica si username + password coinciden.
        Devuelve el Usuario o None.
        """
        user = self.load_by_username(username)

        if not user:
            print("[INFO] Usuario no encontrado.")
            return None

        # comparar hash
        if HashUtil.verify_password(password, user.password_hash):
            print("[INFO] Login correcto.")
            return user

        print("[INFO] Password incorrecto.")
        return None
