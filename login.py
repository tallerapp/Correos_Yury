import conexion 


connect = conexion.conectar();
database = connect[0]
cursor = connect[1]


def autentificar_usuarios(rut,passwd):
    sql = "SELECT * FROM empleados WHERE rut = %s AND password = %s"
    val = (rut, passwd)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        print("¡Inicio de sesión exitoso!")
    else:
        print("Usuario no encontrado o contraseña incorrecta.")
