# Main.py
from model.Personas import chef

class Chef(chef):
    def __init__(self, nombre, id, locacion, pedido):
        super().__init__(nombre, id, locacion, pedido)

chefcito = Chef("Rata", 1, "Paras", ["Fideos"])

print(chefcito.ver_pedido())


