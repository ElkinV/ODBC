from fastapi import APIRouter, Body
from fastapi import HTTPException
import db.database as database


router= APIRouter()


@router.get("/")
def root():
    return {"message": "Hello World"}

@router.get("/api/v1/piscinas/", tags=["Piscinas"])#Obtener todas las piscinas
async def get_piscinas():
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("SELECT * from piscinas")
    result=cursor.fetchall()
    piscinas=[]
    
    for row in result:
        piscinas.append({'id_piscina': row[0], 'fecha_monitoreo': row[1], 'Ubicacion': row[2],"Descripcion":row[3], "Codigo":row[4]})
    
    cursor.close()
    return piscinas
 
@router.get("/api/v1/piscinas/codigo={codigo}",tags=["Piscinas"])#Obtener piscinas por codigo_cliente
async def get_piscinas_by_client(codigo:int):
     cnx= database.cnx
     cursor= cnx.cursor()
     cursor.execute("SELECT * FROM piscinas ")
     result=cursor.fetchall()
     piscinas=[]
     
     for row in result:
        piscinas.append({'id_piscina': row[0], 'fecha_monitoreo': row[1], 'Ubicacion': row[2], "Descripcion":row[3],"Codigo":row[4]})
        
     p=[i for i in piscinas if i['Codigo']==codigo]
     cursor.close()
     
     if not p:
        raise HTTPException(status_code=404, detail="Item not found")
     else:
        return p

@router.get("/api/v1/piscinas/id={id}",tags=["Piscinas"])#Obtener piscinas por id
async def get_piscinas_by_id(id:int):
     cnx= database.cnx
     cursor= cnx.cursor()
     cursor.execute("SELECT * FROM piscinas ")
     result=cursor.fetchall()
     piscinas=[]
     
     for row in result:
        piscinas.append({'id_piscina': row[0], 'fecha_monitoreo': row[1], 'Ubicacion': row[2], "Codigo":row[3]})
        
     p=[i for i in piscinas if i['id_piscina']==id ]
     cursor.close()
    
     if not p:
        raise HTTPException(status_code=404, detail="Item not found")
     else:
        return p
    
    
@router.post('/api/v1/piscinas/', tags=['Piscinas'])#Crear piscinas
async def create_piscinas(id_piscina:int= Body(), fecha_monitoreo:str= Body(), Ubicacion:str=Body(), Codigo:int=Body()):
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("INSERT INTO piscinas(`ID_PISCINAS`, `FECHA_MONITOREO`, `UBICACION`, `codigo`) VALUES (%s,%s,%s,%s)",(id_piscina, fecha_monitoreo, Ubicacion, Codigo))
    cnx.commit()
    cursor.close()
    return await get_piscinas()

@router.put('/api/v1/piscinas/{id}', tags=['Piscinas'])#Actualizar piscinas
async def update_piscinas(id:int, id_piscina:int= Body(), fecha_monitoreo:str= Body(), Ubicacion:str=Body(), Codigo:int=Body()):
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("UPDATE piscinas SET ID_PISCINAS=%s, FECHA_MONITOREO=%s, UBICACION=%s, codigo=%s WHERE ID_PISCINAS=%s",(id_piscina, fecha_monitoreo, Ubicacion, Codigo, id))
    cnx.commit()
    cursor.close()
    return await get_piscinas()

@router.delete('/api/v1/piscinas/{id}', tags=['Piscinas'])#Eliminar piscinas
async def delete_piscinas(id:int):
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("DELETE FROM HISTORIAL_DE_PARAMETROS WHERE ID_PISCINAS=%s",(id,))
    cursor.execute("DELETE FROM piscinas WHERE ID_PISCINAS=%s",(id,))
    cnx.commit()
    cursor.close()
    return await get_piscinas()

@router.get("/api/v1/parametros/", tags=["Parametros"])#Obtener todos los parametros de monitoreo
async def get_parameters():
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("SELECT * from historial_de_parametros")
    result=cursor.fetchall()
    parametros=[]
    
    for row in result:
        parametros.append({'id_historial': row[0], 'nombre_parametro': row[1], 'sensor origen': row[2], "valor":row[3], "fecha":row[4],"ID_PISCINAS":row[5]})
    
    cursor.close()
    return parametros


@router.get("/api/v1/parametros/{id}", tags=["Parametros"])#Obtener parametros por id
async def get_parameters_by_id(id:int):
        cnx= database.cnx
        cursor= cnx.cursor()
        cursor.execute("SELECT * FROM historial_de_parametros ")
        result=cursor.fetchall()
        parametros=[]
        
        for row in result:
            parametros.append({'id_historial': row[0], 'nombre_parametro': row[1], 'sensor origen': row[2], "valor":row[3], "fecha":row[4],"ID_PISCINAS":row[5]})
            
        p=[i for i in parametros if i['ID_PISCINAS']==id ]
        cursor.close()
        
        if not p:
            raise HTTPException(status_code=404, detail="Item not found")
        else:
            return p

@router.get("/api/v1/clientes/", tags=["Clientes"])
def get_clientes():
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("SELECT * from cliente")
    result=cursor.fetchall()
    clientes=[]
    
    for row in result:
        clientes.append({'id_cliente': row[0], 'nombre_cliente': row[1], 'correo': row[2], "telefono":row[3], "direccion":row[4]})
    
    cursor.close()
    return clientes

#post parametros
@router.post('/api/v1/parametros/', tags=['Parametros'])#Crear parametros
async def create_parametros(nombre_parametro:str= Body(), sensor_origen:str=Body(), valor:int=Body(), fecha:str=Body(), ID_PISCINAS:int=Body()):
    cnx= database.cnx
    cursor= cnx.cursor()
    cursor.execute("INSERT INTO HISTORIAL_DE_PARAMETROS (NOMBRE_PARAMETRO, SENSOR, VALOR_PARAMETRO, FECHA_PARAMETRO, ID_PISCINAS) VALUES (%s,%s,%s,%s,%s)",(nombre_parametro, sensor_origen, valor, fecha, ID_PISCINAS))
    cnx.commit()
    cursor.close()
    return await get_parameters()