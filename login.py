import conexion 


connect = conexion.conectar();
database = connect[0]
cursor = connect[1]


def autentificar_usuarios(rut, passwd):
    sql = "SELECT * FROM empleados WHERE rut = %s AND password = %s"
    val = (rut, passwd)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        return True
    else:
        return False

def PerfilUsuario(rut):
    sql = "SELECT perfil FROM empleados WHERE rut = %s"
    val = (rut)
    cursor.execute(sql, (val ,))
    perfil = cursor.fetchone()
    perfilEmpleado = perfil[0]
    return perfilEmpleado;