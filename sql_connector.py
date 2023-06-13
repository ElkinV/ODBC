#Conectarse a una Base da datos MYSQL usando el modulo my-sql-connector
import mysql.connector
import json

# Establecer una conexión a la base de datos
cnx = mysql.connector.connect(
    user='root', 
    password='', 
    host='127.0.0.1', 
    database='calidad_agua')
cursor=cnx.cursor()


def do_select(columnas="*",tabla="proveedores"):
    # Ejecutar una consulta
    query = (f"SELECT {columnas} FROM {tabla}")
    cursor.execute(query)
    
    # Obtener los resultados
    results = cursor.fetchall()
    output=[]
    # Imprimir los resultados
    for row in results:
        print(row)
        
        
    cursor.close()
    cnx.close()
    
def do_insert(tabla,valor_campos,*nombre_campos):
        
    aux_campo=", ".join(list(nombre_campos))
    
    query = (f"INSERT INTO {tabla} ({aux_campo}) "
         "VALUES (%s, %s, %s, %s)")
    
    tuple(valor_campos)
    data = ("6", "dylan", "123", "tu-casa")
    
    cursor.execute(query, valor_campos)

    # Hacer commit de los cambios
    cnx.commit()
    
     # Cerrar la conexión
    cursor.close()
    cnx.close()
    

if __name__ == "__main__":
    lista_campos=("7","diego","321","UDC")
    #do_insert("proveedor",lista_campos,"codigo","nombre","telefono","direccion")
    
    do_select("*","piscinas")
    
     
    

       
