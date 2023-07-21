import rrhh
import conexion 
connect = conexion.conectar();
database = connect[0]
cursor = connect[1]


def opcionnes(rut):
    print(""" 
            ¿Que datos deseas cambiar? 
            1.-Nombre
            2.-sexo
            3.-direccion
            4.-telefonno
          
          """)
    opcionnes = int(rrhh.validarCampo("Ingresa la opcion que deseas(1,2,3,4)", opciones_validas=["1","2","3","4"]));
    if opcionnes == 1:
        nombre = rrhh.validarCampo("Ingresa tu nuevo nombre");
        cambiarNombre(nombre,rut)
    elif opcionnes == 2:
        sexo = rrhh.validarCampo("Ingresa tu Sexo (M/F)", opciones_validas=["M", "F"]).upper()
        cambiarSexo(sexo,rut)
    elif opcionnes == 3:
        direccion = rrhh.validarCampo("Ingresa tu nueva direccion")
        cambiarDireccion(direccion,rut)
    elif opcionnes == 4:
        telefono = rrhh.validarCampo("Ingresa tu nuevo telefono")
        cambiarTelefono(telefono,rut)
    else: 
        print("opcion incorrecta")
    
def cambiarNombre(nuevo_nombre,rut):
        sql = "UPDATE empleados SET nombre_completo = %s WHERE rut = %s"
        val = (nuevo_nombre, rut)
        cursor.execute(sql, val)
        database.commit()

        print("Nombre del usuario con RUT", rut, "cambiado a:", nuevo_nombre)
def cambiarSexo(nuevo_sexo,rut):
        sql = "UPDATE empleados SET sexo = %s WHERE rut = %s"
        val = (nuevo_sexo, rut)
        cursor.execute(sql, val)
        database.commit()

        print("Sexo del usuario con RUT", rut, "cambiado a:", nuevo_sexo)
def cambiarDireccion(direccion,rut):
        sql = "UPDATE empleados SET direccion = %s WHERE rut = %s"
        val = (direccion, rut)
        cursor.execute(sql, val)
        database.commit()

        print("direccion del usuario con RUT", rut, "cambiado a:", direccion)
def cambiarTelefono(telefono,rut):
        sql = "UPDATE empleados SET telefono = %s WHERE rut = %s"
        val = (telefono, rut)
        cursor.execute(sql, val)
        database.commit()

        print("telefono del usuario con RUT", rut, "cambiado a:", telefono)
    

   