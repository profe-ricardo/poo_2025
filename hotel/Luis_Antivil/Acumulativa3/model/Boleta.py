from model.usuario import UsuarioModel
from model.Clienteliente import cliente
class boleta():
    def __init__(self,folio:int,cliente:cliente,usuario:(UsuarioModel)):
        self.folio=folio
        self.cliente=cliente
