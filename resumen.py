import pymysql
from prettytable import PrettyTable
import conexion
connect = conexion.conectar();
database = connect[0]
cursor = connect[1]

def tabla():
        sql = "SELECT rut, nombre_completo, sexo, cargo FROM empleados"
        cursor.execute(sql)
        datos_empleados = cursor.fetchall()
        return mostrar_empleados(datos_empleados)
        
   
def mostrar_empleados(datos_empleados):
    tabla = PrettyTable()
    tabla.field_names = ["RUT", "Nombre", "Sexo", "Cargo"]

    for empleado in datos_empleados:
        tabla.add_row(empleado)

    print(tabla)