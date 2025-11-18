class InventarioView:
   
    @staticmethod
    def View_inventory(inventory: list) -> None:

        if len(inventory) > 0:
            print("\n[INFO]:- Inventario -")

            for i in inventory:
                print(f"[INFO]:--- Nombre: {i['Name']} | Tipo: {i['Type']} | Cantidad: {i['Quantity']} | Precio: {i['Cost_Price']}")
        else:
            print("[ERROR]: Sin registro en inventario.")

class RoomView: 

    @staticmethod
    def View_room(rooms: list) -> None:

        if len(rooms) > 0:
            print("[####] -Habitaciones- ")

            for r in rooms:
                print(f"[####]--- Numero: {r['Number']} | Numero_Personas: {r['Number_of_People']} | Tipe: {r['Tipe']}")

        else:
            print("[ERROR]: Sin registro de habitaciones.")

class TicketView:

    @staticmethod
    def View_ticket(Ticket: list) -> None:


        if len(Ticket) > 0:
            print("\n[####] -Tickets- ")

            for t in Ticket:
                print(f"[####]--- Folio: {t['Folio']} | Clientes: {t['Client']} | Usuario: {t['User']}")

        else:
            print("[ERROR]: Sin registro de tickets.")
