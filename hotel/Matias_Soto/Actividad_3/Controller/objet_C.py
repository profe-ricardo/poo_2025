import re
from Model.objet_M import Inventorymodel,RoomModel,TicketModel
SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class inventoryController:
    def __init__(self, Model: Inventorymodel):
        self.Model = Model
    
    def register_inventory(self, Name: str, Tipe: str, Quantity: int, Cost_price: float):

        if patron.search(Name) or patron.search(Tipe):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(Name,Tipe,Quantity,Cost_price)

class RoomController:

    def __init__(self,Model: RoomModel ):
        self.Model = Model

    def register_room(self,Numer: int, Number_of_people: int , Tipe: str):
            
        if patron.search(Numer) or patron.search(Number_of_people):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(Numer,Number_of_people,Tipe)

class TicketController:
    
    def __init__(self,Model: TicketModel):
        self.Model = Model

    def Register_Ticket(self, Folio: int, Client: str, Usuario: str):

        if patron.search(Folio) or patron.search(Client):
            print("[ERROR]: No se puede ingresar código SQL en los string.")

            return False
        
        else:
            return self.modelo.guardar_item(Folio, Client, Usuario)

    
