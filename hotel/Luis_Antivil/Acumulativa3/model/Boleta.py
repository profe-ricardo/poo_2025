from model.Usuario import UsuarioModel
from model.Cliente import cliente
class boleta():
    def __init__(self,folio:int,cliente:cliente,usuario:(UsuarioModel)):
        self.folio=folio
        self.cliente=cliente
