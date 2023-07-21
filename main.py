import login
import rrhh
print("inicia sessión")
rut= rrhh.validarCampo("ingresa tu rut");
passwd = rrhh.validarCampo("ingresa tu contraseña");

login.autentificar_usuarios(rut,passwd);

if login.PerfilUsuario(rut) == "empleado":
    print("""¿Que desea hacer?
          1.-Agregar cargas familiares
          2.-Eliminar cargas familiares
          3.-Agregar contactos de emergencia
          4.-Eliminar contactos de emergencia
          5.-Modificar Datos Personales
          6.-Salir
          """)
    opcion = input("Ingrese su opción(1,2,3,4,5,6)")
    
if login.PerfilUsuario(rut) == "RRHH":
    print("""¿Que desea hacer?
          1.-Ver tabla resumen
          2.-Crear ficha del trabajador
          3.-salir
          """)
    opcion = int(input("Ingrese su opción(1,2,3)"))
    if opcion == 1:
        print("opcion 1")
    elif opcion == 2:
        rrhh.registrarUsuario();
    elif opcion == 3:
        print("opcion 3")
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
        





