from fastapi import FastAPI
import sql_connector
app = FastAPI()
app.title="CalidadAguaAPI"

@app.get("/piscinas/", tags=["Piscinas"])#Obtener todas las piscinas
def get_piscinas():
    cnx=sql_connector.connect(user='root',  password='', host='127.0.0.1', database='calidad_agua')
    cnx.cursor.execute("SELECT * from piscinas")
    result=sql_connector.cursor.fetchall()
    piscinas=[]
    
    for row in result:
        piscinas.append({'id_piscina': row[0], 'fecha_monitoreo': row[1], 'Ubicacion': row[2], "Codigo":row[3]})
    
    sql_connector.cursor.close()
    #sql_connector.cnx.close()
    return piscinas

@app.get("/piscinas/{id}",tags=["Piscinas"])#Obtener piscinas por id
def get_piscinas_by_id(id:int):
     sql_connector.cnx
     sql_connector.cursor.execute("SELECT * FROM piscinas ")
     result=sql_connector.cursor.fetchall()
     piscinas=[]
     
     for row in result:
        piscinas.append({'id_piscina': row[0], 'fecha_monitoreo': row[1], 'Ubicacion': row[2], "Codigo":row[3]})
        
     p=[i for i in piscinas if i['id_piscina']==id]
    
     sql_connector.cursor.close()
     return p

if __name__ == "__main__":
    print(get_piscinas())