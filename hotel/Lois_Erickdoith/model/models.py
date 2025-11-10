from dataclasses import dataclass
from typing import Optional, List
from config.db_config import ConexionOracle
import datetime

@dataclass 
class Inventario:
    id_inventario: Optional[int]
    nombre: str
    tipo: str
    cantidad: int
    precio_costo: float

    @staticmethod
    def create_table_if_not_exists(db: ConexionOracle):
        
        pass

    def save(self, db: ConexionOracle):
        cur = db.cursor()
        sql = """
        INSERT INTO inventario (id_inventario, nombre, tipo, cantidad, precio_costo)
        VALUES (:id_inventario, :nombre, :tipo, :cantidad, :precio_costo)
        """
        cur.execute(sql, {
            "id_inventario": self.id_inventario,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "precio_costo": self.precio_costo
        })
        db.commit()
        
        try:
            cur.execute("SELECT seq_inventario.CURRVAL FROM dual")
            row = cur.fetchone()
            if row:
                self.id_inventario = row[0]
        except Exception:
            pass
        cur.close()
        return self

    @staticmethod
    def get_all(db: ConexionOracle) -> List['Inventario']:
        cur = db.cursor()
        cur.execute("SELECT id_inventario, nombre, tipo, cantidad, precio_costo FROM inventario")
        rows = cur.fetchall()
        cur.close()
        return [Inventario(*r) for r in rows]

    @staticmethod
    def get_by_id(db: ConexionOracle, id_inventario: int) -> Optional['Inventario']:
        cur = db.cursor()
        cur.execute("SELECT id_inventario, nombre, tipo, cantidad, precio_costo FROM inventario WHERE id_inventario = :id", {"id": id_inventario})
        r = cur.fetchone()
        cur.close()
        return Inventario(*r) if r else None

    def update(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("""
            UPDATE inventario SET nombre=:nombre, tipo=:tipo, cantidad=:cantidad, precio_costo=:precio_costo
            WHERE id_inventario = :id
        """, {"nombre": self.nombre, "tipo": self.tipo, "cantidad": self.cantidad, "precio_costo": self.precio_costo, "id": self.id_inventario})
        db.commit()
        cur.close()
        return self

    def delete(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("DELETE FROM inventario WHERE id_inventario = :id", {"id": self.id_inventario})
        db.commit()
        cur.close()
        return True

@dataclass
class Habitacion:
    numero: int
    capacidad: int
    estado: str

    def save(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("INSERT INTO habitaciones (numero, capacidad, estado) VALUES (:numero, :capacidad, :estado)",
                    {"numero": self.numero, "capacidad": self.capacidad, "estado": self.estado})
        db.commit()
        cur.close()
        return self

    @staticmethod
    def get(db: ConexionOracle, numero: int) -> Optional['Habitacion']:
        cur = db.cursor()
        cur.execute("SELECT numero, capacidad, estado FROM habitaciones WHERE numero = :n", {"n": numero})
        r = cur.fetchone()
        cur.close()
        return Habitacion(*r) if r else None

    def update(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("UPDATE habitaciones SET capacidad=:capacidad, estado=:estado WHERE numero=:numero",
                    {"capacidad": self.capacidad, "estado": self.estado, "numero": self.numero})
        db.commit()
        cur.close()
        return self

@dataclass
class Usuario:
    id_usuario: Optional[int]
    nombre: str
    telefono: str
    ubicacion: str

    def save(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("INSERT INTO usuarios (id_usuario, nombre, telefono, ubicacion) VALUES (:id, :nombre, :telefono, :ubicacion)",
                    {"id": self.id_usuario, "nombre": self.nombre, "telefono": self.telefono, "ubicacion": self.ubicacion})
        db.commit()
        try:
            cur.execute("SELECT seq_usuarios.CURRVAL FROM dual")
            r = cur.fetchone()
            if r:
                self.id_usuario = r[0]
        except Exception:
            pass
        cur.close()
        return self

    @staticmethod
    def get(db: ConexionOracle, id_usuario: int) -> Optional['Usuario']:
        cur = db.cursor()
        cur.execute("SELECT id_usuario, nombre, telefono, ubicacion FROM usuarios WHERE id_usuario = :id", {"id": id_usuario})
        r = cur.fetchone()
        cur.close()
        return Usuario(*r) if r else None

@dataclass
class Recepcionista(Usuario):
    
    def check_disponibilidad(self, db: ConexionOracle) -> List[Habitacion]:
        cur = db.cursor()
        cur.execute("SELECT numero, capacidad, estado FROM habitaciones WHERE estado = 'disponible'")
        rows = cur.fetchall()
        cur.close()
        return [Habitacion(*r) for r in rows]

    def reservar_habitacion(self, db: ConexionOracle, numero_habitacion: int, id_cliente: int) -> bool:
        
        cur = db.cursor()
        cur.execute("UPDATE habitaciones SET estado = 'ocupada' WHERE numero = :num", {"num": numero_habitacion})
      
        cur.execute("UPDATE clientes SET id_habitacion = :num WHERE id_cliente = :cid", {"num": numero_habitacion, "cid": id_cliente})
        db.commit()
        cur.close()
        return True

@dataclass
class Cliente:
    id_cliente: Optional[int]
    nombre: str
    telefono: str
    nacionalidad: str
    habitacion_numero: Optional[int] = None

    def save(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("INSERT INTO clientes (id_cliente, nombre, telefono, nacionalidad, id_habitacion) VALUES (:id, :nombre, :telefono, :nacionalidad, :idh)",
                    {"id": self.id_cliente, "nombre": self.nombre, "telefono": self.telefono, "nacionalidad": self.nacionalidad, "idh": self.habitacion_numero})
        db.commit()
        try:
            cur.execute("SELECT seq_clientes.CURRVAL FROM dual")
            r = cur.fetchone()
            if r:
                self.id_cliente = r[0]
        except Exception:
            pass
        cur.close()
        return self

    @staticmethod
    def get(db: ConexionOracle, id_cliente: int) -> Optional['Cliente']:
        cur = db.cursor()
        cur.execute("SELECT id_cliente, nombre, telefono, nacionalidad, id_habitacion FROM clientes WHERE id_cliente = :id", {"id": id_cliente})
        r = cur.fetchone()
        cur.close()
        return Cliente(r[0], r[1], r[2], r[3], r[4]) if r else None

@dataclass
class Boleta:
    folio: Optional[int]
    id_cliente: int
    id_usuario: int
    fecha: Optional[datetime.date] = None

    def save(self, db: ConexionOracle):
        cur = db.cursor()
        cur.execute("INSERT INTO boletas (folio, id_cliente, id_usuario, fecha) VALUES (:folio, :cliente, :usuario, :fecha)",
                    {"folio": self.folio, "cliente": self.id_cliente, "usuario": self.id_usuario, "fecha": self.fecha or datetime.datetime.now()})
        db.commit()
        try:
            cur.execute("SELECT seq_boletas.CURRVAL FROM dual")
            r = cur.fetchone()
            if r:
                self.folio = r[0]
        except Exception:
            pass
        cur.close()
        return self

    @staticmethod
    def get(db: ConexionOracle, folio: int) -> Optional['Boleta']:
        cur = db.cursor()
        cur.execute("SELECT folio, id_cliente, id_usuario, fecha FROM boletas WHERE folio = :f", {"f": folio})
        r = cur.fetchone()
        cur.close()
        return Boleta(r[0], r[1], r[2], r[3]) if r else None
    
    