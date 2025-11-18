import bcrypt

class HashUtil:
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Genera un hash seguro para la contraseña.
        """
        if not isinstance(password, str):
            raise TypeError("La contraseña debe ser un string")

        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        Verifica que una contraseña coincida con su hash.
        """
        if not isinstance(password, str) or not isinstance(hashed_password, str):
            return False

        password_bytes = password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')

        return bcrypt.checkpw(password_bytes, hashed_bytes)
