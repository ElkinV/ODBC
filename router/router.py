from fastapi import APIRouter, Body, HTTPException
import db.database as database

router = APIRouter()



@router.get("/", tags=["General"])
async def root():
    return {"message": "Hello World"}


@router.get("/api/v1/piscinas/", tags=["Piscinas"])
async def get_piscinas():
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM piscinas")
    result = cursor.fetchall()
    cursor.close()

    piscinas = [
        {
            'id_piscina': row[0],
            'fecha_monitoreo': row[1],
            'Ubicacion': row[2],
            "Descripcion": row[3],
            "Codigo": row[4]
        }
        for row in result
    ]

    return piscinas


@router.get("/api/v1/piscinas/codigo={codigo}", tags=["Piscinas"])
async def get_piscinas_by_client(codigo: int):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM piscinas")
    result = cursor.fetchall()
    cursor.close()

    piscinas = [
        {
            'id_piscina': row[0],
            'fecha_monitoreo': row[1],
            'Ubicacion': row[2],
            "Descripcion": row[3],
            "Codigo": row[4]
        }
        for row in result
    ]

    p = [i for i in piscinas if i['Codigo'] == codigo]

    if not p:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return p


@router.get("/api/v1/piscinas/id={id}", tags=["Piscinas"])
async def get_piscinas_by_id(id: int):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM piscinas")
    result = cursor.fetchall()
    cursor.close()

    piscinas = [
        {
            'id_piscina': row[0],
            'fecha_monitoreo': row[1],
            'Ubicacion': row[2],
            "Descripcion": row[3],
            "Codigo": row[4]
        }
        for row in result
    ]

    p = [i for i in piscinas if i['id_piscina'] == id]

    if not p:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return p


@router.post('/api/v1/piscinas/', tags=['Piscinas'])
async def create_piscinas(
    fecha_monitoreo: str = Body(),
    Descripcion: str = Body(),
    Ubicacion: str = Body(),
    Codigo: int = Body()
):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute(
        "INSERT INTO piscinas (`FECHA_MONITOREO`, `UBICACION`, `Descripcion`, `codigo`) VALUES (%s,%s,%s,%s)",
        (fecha_monitoreo, Descripcion, Ubicacion, Codigo)
    )
    cnx.commit()
    cursor.close()
    return await get_piscinas()


@router.put('/api/v1/piscinas/{id}', tags=['Piscinas'])
async def update_piscinas(
    id: int,
    id_piscina: int = Body(),
    fecha_monitoreo: str = Body(),
    Ubicacion: str = Body(),
    Codigo: int = Body()
):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute(
        "UPDATE piscinas SET ID_PISCINAS=%s, FECHA_MONITOREO=%s, UBICACION=%s, codigo=%s WHERE ID_PISCINAS=%s",
        (id_piscina, fecha_monitoreo, Ubicacion, Codigo, id)
    )
    cnx.commit()
    cursor.close()
    return await get_piscinas()


@router.delete('/api/v1/piscinas/{id}', tags=['Piscinas'])
async def delete_piscinas(id: int):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM HISTORIAL_DE_PARAMETROS WHERE ID_PISCINAS=%s", (id,))
    cursor.execute("DELETE FROM piscinas WHERE ID_PISCINAS=%s", (id,))
    cnx.commit()
    cursor.close()
    return await get_piscinas()


@router.get("/api/v1/parametros/", tags=["Parametros"])
async def get_parameters():
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * from historial_de_parametros")
    result = cursor.fetchall()
    cursor.close()

    parametros = [
        {
            'id_historial': row[0],
            'nombre_parametro': row[1],
            'sensor_origen': row[2],
            "valor": row[3],
            "fecha": row[4],
            "ID_PISCINAS": row[5]
        }
        for row in result
    ]

    return parametros


@router.get("/api/v1/parametros/{id}", tags=["Parametros"])
async def get_parameters_by_piscina(id: int):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM historial_de_parametros")
    result = cursor.fetchall()
    cursor.close()

    parametros = [
        {
            'id_historial': row[0],
            'nombre_parametro': row[1],
            'sensor_origen': row[2],
            "valor": row[3],
            "fecha": row[4],
            "ID_PISCINAS": row[5]
        }
        for row in result
    ]

    p = [i for i in parametros if i['ID_PISCINAS'] == id]

    if not p:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return p
    
@router.post('/api/v1/parametros/', tags=['Parametros'])
async def create_parametros(
    nombre_parametro: str = Body(),
    sensor_origen: str = Body(),
    valor: int = Body(),
    fecha: str = Body(),
    ID_PISCINAS: int = Body()
):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute(
        "INSERT INTO HISTORIAL_DE_PARAMETROS (NOMBRE_PARAMETRO, SENSOR, VALOR_PARAMETRO, FECHA_PARAMETRO, ID_PISCINAS) "
        "VALUES (%s,%s,%s,%s,%s)",
        (nombre_parametro, sensor_origen, valor, fecha, ID_PISCINAS)
    )
    cnx.commit()
    cursor.close()
    return await get_parameters()


@router.patch('/api/v1/parametros/{id}', tags=['Parametros'])
async def update_parametros(id: int, valor: str = Body()):
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute(
        "UPDATE historial_de_parametros SET VALOR_PARAMETRO=%s  WHERE id_historial=%s",
        (valor,id)
    )
    cnx.commit()
    cursor.close()
    return await get_parameters()


@router.get("/api/v1/clientes/", tags=["Clientes"])
async def get_clientes():
    cnx = database.cnx
    cursor = cnx.cursor()
    cursor.execute("SELECT * from cliente")
    result = cursor.fetchall()
    cursor.close()

    clientes = [
        {
            'nombre': row[0],
            'codigo': row[1],
            'apellido': row[2],
            "email": row[3],
            "contraseña": row[4]
        }
        for row in result
    ]

    return clientes




