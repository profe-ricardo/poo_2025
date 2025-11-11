from Cliente import cliente
from Usuario import UsuarioModel
class boleta():
    def __init__(self, folio:int, cliente:cliente, usuario:UsuarioModel):
        self.folio=folio
        self.cliente=cliente
        self.usuario=usuario