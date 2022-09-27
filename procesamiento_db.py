import mysql.connector

def conexion_DB():
    my_conection=mysql.connector.connect(
        user="root",
        host="localhost",
        password="OlimaC880214+",
        database="universidad"
    )

    return my_conection

def register_alumn(nombre, apellido, carrera, edad):
    my_db=conexion_DB()
    mi_cursor=my_db.cursor()

    sql="""INSERT INTO estudiantes
            (nombre, apellido, carrera, edad)
            VALUES(%s, %s, %s, %s)"""

    valores=(nombre, apellido, carrera, edad)

    try:
        mi_cursor.execute(sql, valores)
    except:
        my_db.rollback() #revierte la transacción actual, contrario a un commit
        retorno=1
    else:
        my_db.commit()
        retorno=0
    finally:
        my_db.close()
        return retorno

# resultado=register_alumn("Camilo", "Jaramillo", "Programación", 28)
# print(resultado)

def list_alumns():
    my_db=conexion_DB()
    mi_cursor=my_db.cursor()

    sql="""SELECT nombre, apellido, carrera, edad
            FROM estudiantes"""

    try: 
        mi_cursor.execute(sql)
    except:
        my_db.rollback()
        retorno=1
    else:
        retorno=[]
        for alumn in mi_cursor:
            retorno.append(alumn)
    finally:
        my_db.close()
        return retorno

# resultado=list_alumns()
# print(resultado)

def get_alumn_by_id(id_alumn):
    my_db=conexion_DB()
    mi_cursor=my_db.cursor()

    sql="""SELECT nombre, apellido, carrera, edad
            FROM estudiantes
            WHERE estudiante_id = %s"""

    valores=(id_alumn,)

    try: 
        mi_cursor.execute(sql,valores)
    except:
        my_db.rollback()
        retorno=1
    else:
        retorno=()
        for alumn in mi_cursor:
            retorno=alumn
    finally:
        my_db.close()
        return retorno

# resultado=get_alumn_by_id(4)
# print(resultado)

def update_carreer_alumn(carrera, id_alumn):
    my_db=conexion_DB()
    mi_cursor=my_db.cursor()

    sql="""UPDATE estudiantes
            SET carrera=%s
            WHERE estudiante_id = %s
            """

    valores=(carrera, id_alumn)

    try: 
        mi_cursor.execute(sql,valores)
    except:
        my_db.rollback()
        retorno=1
    else:
        my_db.commit()
        retorno=0
    finally:
        my_db.close()
        return retorno

# resultado=update_carreer_alumn("Desarrollador Web", 4)
# print(resultado)

def delete_alumn_by_id(id_alumn):
    my_db=conexion_DB()
    mi_cursor=my_db.cursor()

    sql="""DELETE FROM estudiantes
            WHERE estudiante_id = %s
            """
    valores=(id_alumn,)

    try: 
        mi_cursor.execute(sql,valores)
    except:
        my_db.rollback()
        retorno=1
    else:
        my_db.commit()
        retorno=0
    finally:
        my_db.close()
        return retorno

# resultado=delete_alumn_by_id(3)
# print(resultado)



