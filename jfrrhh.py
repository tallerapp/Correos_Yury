import conexion
import rrhh
from datetime import datetime
import pymysql
from prettytable import PrettyTable
connect = conexion.conectar();
database = connect[0]
cursor = connect[1]


def filtrar_trabajadores_por_sexo():
    
        sql = "SELECT rut, nombre_completo, cargo FROM empleados WHERE sexo = %s"
        val = rrhh.validarCampo("Seleccione para filtrar (M/F)", opciones_validas=["M", "F"]).upper()
        cursor.execute(sql, (val ,))
        trabajadores = cursor.fetchall()

        mostrar_trabajadores(trabajadores)
        
def filtrar_trabajadores_por_cargo():
    
        sql = "SELECT rut, nombre_completo, cargo FROM empleados WHERE cargo = %s"
        val = rrhh.validarCampo("Ingrese el cargo para filtrar").upper()
        cursor.execute(sql, (val ,))
        trabajadores = cursor.fetchall()

        mostrar_trabajadores(trabajadores)
def filtrar_trabajadores_por_area_y_departamento():
    
        sql = "SELECT rut, nombre_completo, cargo FROM empleados WHERE area = %s AND departamento = %s"
        area = rrhh.validarCampo("Ingrese el area").upper()
        departamento = rrhh.validarCampo("Ingrese el departamento").upper()
        val = (area, departamento)
        cursor.execute(sql, val)
        trabajadores = cursor.fetchall()

        mostrar_trabajadores(trabajadores)
        
def mostrar_trabajadores(trabajadores):
    if trabajadores:
        tabla = PrettyTable()
        tabla.field_names = ["RUT", "Nombre Completo", "Cargo"]

        for trabajador in trabajadores:
            tabla.add_row(trabajador)

        print(tabla)
    else:
        print("No se encontraron trabajadores con el sexo especificado.")
