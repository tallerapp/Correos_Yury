import conexion 
import rrhh
import pymysql
from prettytable import PrettyTable
connect = conexion.conectar();
database = connect[0]
cursor = connect[1]

def agregarContacto(rut):
    contacto = rrhh.validarCampo("¿Desea agregar un contacto de emergencia? (S/N): ").upper()
    if contacto == "S":
        while True:
            nombre_contacto = rrhh.validarCampo("Nombre del contacto de emergencia: ")
            relacion = rrhh.validarCampo("Relación con el empleado: (Familiar, tutor , amistad)", opciones_validas=["FAMILIAR", "TUTOR", "AMISTAD"]).upper()
            telefono_contacto = rrhh.validarCampo("Teléfono del contacto de emergencia: ")
            try:
                sql = '''
                    INSERT INTO contactos_emergencia (rut_empleado, nombre_contacto, relacion, telefono)
                    VALUES (%s, %s, %s, %s)
                '''
                values = (rut, nombre_contacto, relacion, telefono_contacto)
                cursor.execute(sql, values)
                database.commit()
                print("Registro de contacto de emergencia exitoso.")
            except conexion.mysql.connector.Error as err:
                print("Error al insertar datos en la tabla contactos_emergencia:", err)
            seguir_agregando = rrhh.validarCampo("¿Desea agregar otro contacto de emergencia? (S/N): ").upper()
            if seguir_agregando != "S":
                break
def eliminarContacto(rut):
    eliminar_carga = rrhh.validarCampo("¿Desea eliminar un contacto? (S/N): ").upper()
    if eliminar_carga == "S":
        sql = "SELECT contacto_id, nombre_contacto, relacion, telefono FROM contactos_emergencia WHERE rut_empleado = %s"
        val = rut
        cursor.execute(sql, (val ,))
        cargas = cursor.fetchall()
        mostrar_cargas(cargas)
    contacto= int(rrhh.validarCampo("Seleccione el id del contacto que desea eliminar"))
    seleccionarcarga(contacto,rut);
    
            
def mostrar_cargas(cargas_familiares):
    if cargas_familiares:
        tabla = PrettyTable()
        tabla.field_names = ["Carga ID", "Nombre Carga", "Parentesco", "Sexo"]

        for carga in cargas_familiares:
            tabla.add_row(carga)

        print(tabla)
    else:
        print("No se encontraron cargas familiares asociadas al empleado.")

def seleccionarcarga(contacto_id, rut):
    sql = "DELETE FROM contactos_emergencia WHERE contacto_id = %s AND rut_empleado = %s"
    val = (contacto_id, rut)
    cursor.execute(sql, val)
    database.commit()
    print("Carga familiar con carga_id", contacto_id, "eliminada correctamente.")