import conexion 
import rrhh
import pymysql
from prettytable import PrettyTable
connect = conexion.conectar();
database = connect[0]
cursor = connect[1]


def agregarCargas(rut):
    tiene_cargas = rrhh.validarCampo("¿Desea agregar una carga familiar? (S/N): ").upper()
    if tiene_cargas == "S":
        while True:
            nombre_carga = rrhh.validarCampo("Nombre de la carga familiar: ")
            parentesco = rrhh.validarCampo("Parentesco con el empleado: ")
            sexo_carga = rrhh.validarCampo("Sexo (M/F)", opciones_validas=["M", "F"])

            try:
                sql = '''
                    INSERT INTO cargas_familiares (rut_empleado, nombre_carga, parentesco, sexo)
                    VALUES (%s, %s, %s, %s)
                '''
                values = (rut, nombre_carga, parentesco, sexo_carga)
                cursor.execute(sql, values)
                database.commit()
                print("Registro de carga familiar exitoso.")
            except conexion.mysql.databaseector.Error as err:
                print("Error al insertar datos en la tabla cargas_familiares:", err)

            seguir_agregando = rrhh.validarCampo("¿Desea agregar otra carga familiar? (S/N): ").upper()
            if seguir_agregando != "S":
                break
def eliminarCargas(rut):
    eliminar_carga = rrhh.validarCampo("¿Desea eliminar una carga familiar? (S/N): ").upper()
    if eliminar_carga == "S":
        sql = "SELECT carga_id, nombre_carga, parentesco, sexo FROM cargas_familiares WHERE rut_empleado = %s"
        val = rut
        cursor.execute(sql, (val ,))
        cargas = cursor.fetchall()
        mostrar_cargas(cargas)
    carga= int(input("seleccionne que el id de la carga que quiere eliminar :"));
    seleccionarcarga(carga,rut);
        
def mostrar_cargas(cargas_familiares):
    if cargas_familiares:
        tabla = PrettyTable()
        tabla.field_names = ["Carga ID", "Nombre Carga", "Parentesco", "Sexo"]

        for carga in cargas_familiares:
            tabla.add_row(carga)

        print(tabla)
    else:
        print("No se encontraron cargas familiares asociadas al empleado.")

def seleccionarcarga(carga_id, rut):
    sql = "DELETE FROM cargas_familiares WHERE carga_id = %s AND rut_empleado = %s"
    val = (carga_id, rut)
    cursor.execute(sql, val)
    database.commit()
    print("Carga familiar con carga_id", carga_id, "eliminada correctamente.")