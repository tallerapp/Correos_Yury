import mysql.connector

def conectar():
    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="correosyury",
            port= 3306
        )
        cursor = database.cursor(buffered=True);
        return [database, cursor]
    except mysql.connector.Error as err:
        print("Error al conectar a la base de datos:", err)
        return None, None
