#from controller.personas import Chef


# class chef(Chef):
#     def __init__(self,nombre: str, id: int, locacion: str, pedidos: list):
#         super().__init__(nombre, id, locacion, pedidos)

#     def recibir_pedido(self, pedido: list) -> bool:
#         return self.procesar_pedido(pedido)

class UsuarioView():
    """
        Vista del usuario, muestra información en pantalla.
    """
    @staticmethod
    def mostrar_usuarios(usuarios: list) -> None:
        """
            Recibe la lista de los usuarios.\n
            Si recibe al menos uno, mostrará la lista en consola.
        """
        if len(usuarios) > 0:
            print("\n- Lista de usuarios -")

            for u in usuarios:
                print(f"--- Nombre: {u['nombre']} | Telefono: {u['telefono']}")
        else:
            print("[ERROR]: Sin usuarios registrados")

class clienteview():

    @staticmethod

    def mostrar_clientes(clientes: list) -> None:
        if len(clientes) > 0:
            print("\n- Lista de clientes -")
            
            for u in clientes:
                print(f"--- Nombre: {u['nombre']} | telefono: {u['telefono']} | nacionalidad: {u['nacionalidad']} | habitacion: {u['habitacion']} ")
        else:
            print("[ERROR]: Sin clientes registrados")
    
class recepcionistaView():
    
    @staticmethod

    def mostrar_recepcionistas(recepcionistas: list) -> None:
        if len(recepcionistas) > 0:
            print("\n- Lista de recepcionistas -")
            
            for u in recepcionistas:
                print(f"--- Nombre: {u['nombre']} | telefono: {u['telefono']} | ubicacion: {u['ubicacion']}")
                
        else:
            print("[ERROR]: Sin recepcionistas registrados")   
            
class clienteview():
    
    @staticmethod

    def mostrar_clientes(clientes: list) -> None:
        if len(clientes) > 0:
            print("\n- Lista de clientes -")
            
            for u in clientes:
                print(f"--- Nombre: {u['nombre']} | telefono: {u['telefono']} | nacionalidad: {u['nacionalidad']} | habitacion: {u['habitacion']} ")
        else:
            print("[ERROR]: Sin clientes registrados")
                

