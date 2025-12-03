import json
import oracledb

def conectar(user: str, password: str, dsn: str):
    try:
        conn = oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )

        return conn
    except oracledb.DatabaseError as e:
        error, = e.args
        return error
    
conn = conectar("System", "Ina.2025", "localhost:1521/xe")
cursor = conn.cursor()

datos = { 'nombre' : 'Ricardo' }
ruta = "c:/Users/19093075-0/Desktop/POO/poo_2025/hotel/Luis_vicencio/ACUMULATIVA 4/nombre.json"

with open(ruta , "r") as archivo:
    datos = json.load(datos, archivo)


for post in datos:
    consulta = "insert into posts (id, userId, title. body) values (:1, :2, :3, :4)"
    cursor.execute(consulta,(post['id'], post ['userId'], post['title'], post ['body']))

conn.commit()
conn.close()
