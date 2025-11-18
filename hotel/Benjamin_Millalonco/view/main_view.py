from controller.habitacion_C import HabitacionController
from controller.cliente_C import ClienteController

def mostrar_menu():
    print("\n===== SISTEMA HOTEL - MENÚ PRINCIPAL =====")
    print("1. Crear habitación")
    print("2. Listar habitaciones")
    print("3. Crear cliente")
    print("4. Listar clientes")
    print("0. Salir")

def ejecutar_vista():
    habitacion_ctrl = HabitacionController()
    cliente_ctrl = ClienteController()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            print("\n--- Creando habitación ---")
            numero = input("Número de habitación: ")
            locacion = input("Ubicación o tipo: ")
            habitacion_ctrl.crear_habitacion(numero, locacion)

        elif opcion == "2":
            print("\n--- Listando habitaciones ---")
            habitacion_ctrl.listar_habitaciones()

        elif opcion == "3":
            print("\n--- Creando cliente ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            habitacion = input("Habitación asignada: ")
            cliente_ctrl.crear_cliente(nombre, telefono, direccion, habitacion)

        elif opcion == "4":
            print("\n--- Listando clientes ---")
            cliente_ctrl.listar_clientes()

        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\n[ERROR]: Opción inválida, intenta nuevamente.")
