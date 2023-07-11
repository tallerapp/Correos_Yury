import login
print("inicia sessión")
rut= input("ingresa tu rut");
passwd = input("ingresa tu contraseña")

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
    opcion = input("Ingrese su opción(1,2,3)")
    
if login.PerfilUsuario(rut) == "JFRRHH":
     print("""¿Que desea hacer?
          1.-Ver tabla resumen
          2.-Filtar trabajadores por sexo
          3.-Filtrar trabajadores por Cargo
          4.-Filtrar trabajadores por Area y departamento
          5.-Salir
          """)
        





