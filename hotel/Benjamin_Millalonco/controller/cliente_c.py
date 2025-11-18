from model.cliente_m import ClienteModel

class ClienteController:
    def __init__(self, conexion):
        self.modelo = ClienteModel(conexion)

    def crear(self, nombre, telefono, nacionalidad, habitacion_numero):
        return self.modelo.crear_cliente(nombre, telefono, nacionalidad, habitacion_numero)

    def listar(self):
        clientes = self.modelo.mostrar_clientes()
        for c in clientes:
            print(f"Cliente: {c[1]} | Tel: {c[2]} | Nac: {c[3]} | Habitación: {c[4]}")
        return clientes

