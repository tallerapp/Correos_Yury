import conexion
from datetime import datetime
import re
import empleadoCargas
import empleadoEmergencia

def cerrar_conexion(database, cursor):
    if cursor:
        cursor.close()
    if database:
        database.close()
def validarCampo(campo, opciones_validas=None):
    while True:
        valor = input(f"{campo}: ").upper()

        # Si hay opciones válidas especificadas, verificar que el valor esté entre ellas
        if opciones_validas and valor not in opciones_validas:
            print(f"Opción inválida. Las opciones válidas son: {', '.join(opciones_validas)}")
            continue

        if valor.strip():
            return valor
        else:
            print(f"El campo {campo} no puede estar vacío. Por favor, ingresa un valor válido.")
            
def validar_rut(rut):
    patron_rut = r'^\d{7,8}-[\dkK]$'

    if re.match(patron_rut, rut):
        return True
    else:
        return False
    
def pedir_rut():
    while True:
        rut_ingresado = input("Ingresa el RUT: ")
        if validar_rut(rut_ingresado):
            return rut_ingresado
        else:
            print("El RUT es inválido. Asegúrate de que tenga el formato correcto: 'xxxxxxxx-x' o 'xxxxxxxx-X'.")

def registrarUsuario():
    database, cursor = conexion.conectar()
    if not database or not cursor:
        return

    rut = pedir_rut();
    password = validarCampo("Password: ")
    nombre_completo = validarCampo("Nombre completo: ")
    sexo = validarCampo("Sexo (M/F)", opciones_validas=["M", "F"])
    direccion = validarCampo("Dirección: ")
    telefono = validarCampo("Teléfono: ")
    cargo = validarCampo("Cargo: ")

    # Ingresar fecha de ingreso con validación del formato
    while True:
        fecha_ingreso_str = input("Fecha de ingreso (AAAA-MM-DD): ")
        try:
            fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Formato de fecha incorrecto. Intente nuevamente.")

    area = validarCampo("Área: ").upper()
    departamento = validarCampo("Departamento: ").upper()
    perfil = validarCampo("Perfil (empleado/RRHH/JFRRHH): ", opciones_validas=["EMPLEADO", "RRHH", "JFRRHH"]).upper()

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
    empleadoCargas.agregarCargas(rut);
    empleadoEmergencia.agregarContacto(rut);


   






    
   

    

    