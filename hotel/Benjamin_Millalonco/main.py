from config.dbconfig import ConexionOracle
from controller.habitacion_c import HabitacionController
from controller.cliente_c import ClienteController

if __name__ == "__main__":
    conexion = ConexionOracle("USUARIO", "PASSWORD", "localhost:1521/xe")
    conexion.conectar()

    habitacion_c = HabitacionController(conexion)
    cliente_c = ClienteController(conexion)

    print("\n--- Creando habitación ---")
    habitacion_c.crear(101, 2, "disponible")

    print("\n--- Listando habitaciones ---")
    habitacion_c.listar()

    print("\n--- Creando cliente ---")
    cliente_c.crear("Juan Pérez", "999999999", "Chilena", 101)

    print("\n--- Listando clientes ---")
    cliente_c.listar()

    conexion.desconectar()
