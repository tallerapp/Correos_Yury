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
    opcionnes = int(rrhh.validarCampo("Ingresa la opcion que deseas(1,2,3,4)"));
    if opcionnes == 1:
        nombre = rrhh.validarCampo("ingresa tu nuevo nombre");
        cambiarNombre(nombre,rut)
    
def cambiarNombre(nuevo_nombre,rut):
        sql = "UPDATE empleados SET nombre_completo = %s WHERE rut = %s"
        val = (nuevo_nombre, rut)
        cursor.execute(sql, val)
        database.commit()

        print("Nombre del usuario con RUT", rut, "cambiado a:", nuevo_nombre)

   