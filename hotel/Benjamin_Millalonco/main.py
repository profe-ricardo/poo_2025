from config.dbconfig import ConexionOracle
from controller.habitacion_c import HabitacionController
from controller.cliente_c import ClienteController
from controller.usuario_c import UsuarioController

if __name__ == "__main__":
    db = ConexionOracle("System", "Ina.2025", "localhost:1521/xe")
    db.conectar()

    habitacion_c = HabitacionController(db)
    cliente_c = ClienteController(db)
    usuario_c = UsuarioController(db)

    print("\n=== SISTEMA HOTEL - MENÚ PRINCIPAL ===")

    while True:
        print("\n1) Crear usuario")
        print("2) Login")
        print("3) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- CREAR USUARIO ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            ubicacion = input("Ubicación: ")
            password = input("Contraseña: ")

            creado_id = usuario_c.crear(nombre, telefono, ubicacion, password)
            if creado_id:
                print(f"[OK] Usuario creado con ID {creado_id}")
            else:
                print("[ERROR] No se pudo crear el usuario.")

        elif opcion == "2":
            print("\n--- LOGIN DE USUARIO ---")
            tel = input("Teléfono: ")
            password = input("Contraseña: ")

            login_ok = usuario_c.login(tel, password)
            if login_ok:
                print("[OK] Login exitoso 😊")
            else:
                print("[X] Login fallido ❌")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

    # Cerrar conexión
    try:
        db.cerrar()
    except AttributeError:
        try:
            db.desconectar()
        except:
            pass
