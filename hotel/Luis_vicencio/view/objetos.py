class InventarioView():
    
    @staticmethod

    def mostrar_inventario(inventario: list) -> None:
        if len(inventario) > 0:
            print("\n- Lista de inventario -")
            
            for u in inventario:
                print(f"--- Nombre: {u['nombre']} | tipo: {u['tipo']} | cantidad: {u['cantidad']} | precio_costo: {u['precio_costo']}")
                
        else:
            print("[ERROR]: Sin productos registrados") 
            
class HabitacionView():
    
    @staticmethod

    def mostrar_habitacion(habitaciones: list) -> None:
        if len(habitaciones) > 0:
            print("\n- Lista de habitaciones -")
            
            for u in habitaciones:
                print(f"--- Numero: {u['numero']} | cantidad_de_personas: {u['cantidad_de_personas']} | estado: {u['estado']} ")
                
        else:
            print("[ERROR]: Sin habitaciones registrados")
            
    class BoletasView():
        
    @staticmethod

    def mostrar_boletas(Boletas: list) -> None:
        if len(Boletas) > 0:
            print("\n- Lista de Boletas -")
            
            for u in Boletas:
                print(f"--- Folio: {u['folio']} | cliente: {u['cliente']} | usuario: {u['usuario']}")
                
        else:
            print("[ERROR]: Sin Boletas registrados")