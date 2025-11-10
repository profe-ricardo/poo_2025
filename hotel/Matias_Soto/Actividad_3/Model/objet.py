
class Inventory():
    def __init__(self, Name: str, Tipe: str, Quantity: str, Cost_price: float):
        self.Name = Name
        self.Tipe = Tipe
        self.Quantity = Quantity
        self. Cost_price = Cost_price      

    def   Add_Product(self,Tipe: str, Quantity: int) -> bool:
         if Tipe in self.Product:
              self.Product[Tipe] += Quantity
         else:
              self.Product[Tipe] = Quantity
         return True
              
              
               
class Room():
    def __init__(self, Number: str, Number_of_people: int, Tipe: str):
            self.Number = Number
            self.Number_of_peole = Number_of_people
            self.Tipe = Tipe

class Boleta():
      def __init__(self,Folio: int, Client: str, Usuario: str):
            self.Folio = Folio
            self.Client = Client
            self.Usuario = Usuario







