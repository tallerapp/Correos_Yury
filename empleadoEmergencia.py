import conexion 
import rrhh
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
            seguir_agregando = rrhh.validarCampo("¿Desea agregar otra carga familiar? (S/N): ").upper()
            if seguir_agregando != "S":
                break