import login
import rrhh
import resumen
import empleadoCargas
import empleadoEmergencia
import empleadoDatos
print("Inicia sesión")

while True:
    rut = rrhh.validarCampo("Ingresa tu RUT: ")
    passwd = rrhh.validarCampo("Ingresa tu contraseña: ")

    if login.autentificar_usuarios(rut, passwd):
        print("Te logeaste correctamente")
        break
    else:
        print("RUT o contraseña incorrectos. Inténtalo nuevamente.\n")

if login.PerfilUsuario(rut) == "EMPLEADO":
    print("""¿Que desea hacer?
          1.-Agregar cargas familiares
          2.-Eliminar cargas familiares
          3.-Agregar contactos de emergencia
          4.-Eliminar contactos de emergencia
          5.-Modificar Datos Personales
          6.-Salir
          """)
    opcion = int(input("Ingrese su opción(1,2,3,4,5,6)"))
    if opcion == 1:
        empleadoCargas.agregarCargas(rut)
    elif opcion == 2:
        empleadoCargas.eliminarCargas(rut);
    elif opcion == 3:
        empleadoEmergencia.agregarContacto(rut);
    elif opcion == 4:
        empleadoEmergencia.eliminarContacto(rut);
    elif opcion == 5:
        empleadoDatos.opcionnes(rut)
    elif opcion == 6:
        print("session terminada")
    else:
        print("Opcion no disponible")
    
if login.PerfilUsuario(rut) == "RRHH":
    print("""¿Que desea hacer?
          1.-Ver tabla resumen
          2.-Crear ficha del trabajador
          3.-salir
          """)
    opcion = int(input("Ingrese su opción(1,2,3)"))
    if opcion == 1:
        resumen.tabla();
    elif opcion == 2:
        rrhh.registrarUsuario();
    elif opcion == 3:
        print("session terminada")
    else:
        print("Opcion no disponible")
        
    
    
if login.PerfilUsuario(rut) == "JFRRHH":
     print("""¿Que desea hacer?
          1.-Ver tabla resumen
          2.-Filtar trabajadores por sexo
          3.-Filtrar trabajadores por Cargo
          4.-Filtrar trabajadores por Area y departamento
          5.-Salir
          """)
        





