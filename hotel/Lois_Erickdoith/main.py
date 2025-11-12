from config.db_config import ConexionOracle
from models.models import Inventario, Habitacion, Cliente, Usuario, Recepcionista, Boleta
from hotel.Luis_carrasco.model.personas_m import UsuarioModel
from hotel.Luis_carrasco.controller.personas_c import UsuarioController
from hotel.Luis_carrasco.view.personas_v import UsuarioView




def conectarBD():
    
    db = ConexionOracle("system", "ina2025", "localhost:1521/xe")
    if not db.conectar():
        raise SystemExit("No se pudo conectar a la base de datos Oracle.")
    return db

def ejemplo():
    db = conectarBD()

    #habitación
    h = Habitacion(numero=101, capacidad=2, estado="disponible")
    try:
        h.save(db)
        print("Habitación creada:", h)
    except Exception as e:
        print("Error al crear habitación:", e)

    #usuario (recepcionista)
    u = Usuario(id_usuario=None, nombre="Lois Erickdoter", telefono="987654321", ubicacion="Recepción")
    u.save(db)
    print("Usuario creado:", u)

    #cliente
    c = Cliente(id_cliente=None, nombre="Kaisser", telefono="912345678", nacionalidad="Chile", habitacion_numero=101)
    c.save(db)
    print("Cliente creado:", c)

    #recepcionista (Usuario)
    recep = Recepcionista(id_usuario=u.id_usuario, nombre=u.nombre, telefono=u.telefono, ubicacion=u.ubicacion)
    recep.reservar_habitacion(db, numero_habitacion=101, id_cliente=c.id_cliente)

    #boleta
    bo = Boleta(folio=None, id_cliente=c.id_cliente, id_usuario=u.id_usuario)
    bo.save(db)
    print("Boleta generada:", bo.folio)

    #inventario
    inv = Inventario(id_inventario=None, nombre="Toallas", tipo="Limpieza", cantidad=30, precio_costo=500)
    inv.save(db)
    print("Inventario guardado:", inv)

    db.desconectar()

if __name__ == "__main__":    ejemplo()
