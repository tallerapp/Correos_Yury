import conexion
from datetime import datetime

def cerrar_conexion(database, cursor):
    if cursor:
        cursor.close()
    if database:
        database.close()

def registrarUsuario():
    database, cursor = conexion.conectar()
    if not database or not cursor:
        return

    rut = input("Rut: ")
    password = input("Password: ")
    nombre_completo = input("Nombre completo: ")
    sexo = input("Sexo (M/F): ").upper()
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    cargo = input("Cargo: ")

    # Ingresar fecha de ingreso con validación del formato
    while True:
        fecha_ingreso_str = input("Fecha de ingreso (AAAA-MM-DD): ")
        try:
            fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")

    area = input("Área: ")
    departamento = input("Departamento: ")
    perfil = input("Perfil (empleado/RRHH/JFRRHH): ").lower()

    # Inserción de datos en la tabla empleados
    try:
        sql = '''
            INSERT INTO empleados (rut, password, nombre_completo, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento, perfil)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (rut, password, nombre_completo, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento, perfil)
        cursor.execute(sql, values)
        database.commit()
        print("Registro de empleado exitoso.")
    except conexion.mysql.databaseector.Error as err:
        print("Error al insertar datos en la tabla empleados:", err)
        cerrar_conexion(database, cursor)
        return
    
     # Inserción de datos en la tabla contactos_emergencia
    try:
        nombre_contacto = input("Nombre del contacto de emergencia: ")
        relacion = input("Relación con el empleado: ")
        telefono_contacto = input("Teléfono del contacto de emergencia: ")

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

    cerrar_conexion(database, cursor)

    # Preguntar al usuario si tiene cargas familiares
    tiene_cargas = input("¿Tiene cargas familiares? (S/N): ").upper()
    if tiene_cargas == "S":
        while True:
            nombre_carga = input("Nombre de la carga familiar: ")
            parentesco = input("Parentesco con el empleado: ")
            sexo_carga = input("Sexo de la carga (M/F): ").upper()

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

            seguir_agregando = input("¿Desea agregar otra carga familiar? (S/N): ").upper()
            if seguir_agregando != "S":
                break

    cerrar_conexion(database, cursor)





    
   

    

    