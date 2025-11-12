from hotel.Heidi_Labe.config.db_config import ConexionOracle
class InventarioModel:

  def __init__(self,nombre:str,tipo:str,cantidad:int,precio_costo: float,conexion:ConexionOracle):
      self.nombre = nombre
      self.tipo = tipo
      self.cantidad = cantidad
      self.precio_costo = precio_costo
      self.db = conexion

def guardar_item(self, nombre, tipo, cantidad, precio_costo) -> bool:

  cursor = self.db.obtener_cursor()

  try:
     
     consulta_validacion = "select * from inventario where nombre = :1"
     cursor.execute(consulta_validacion, (nombre,))


  if len(cursor.fetchall()) > 0:
     print(f"[ERROR]: ya existe un item con el nombre {nombre}")

  return False
else:





















