class HabitacionModel():
    def __main__(self, numero: int, cantidad_personas: int, estado: str):
        self.numero = numero
        self.cantidad_personas= cantidad_personas
        self.estado = estado
    
    def guardar_item(self, numero, cantidad_personas, estado) -> bool:

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = 