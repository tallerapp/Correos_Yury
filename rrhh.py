def registrarUsuario():
    rut = input("Ingrese Rut del empleado")
    nombre = input("Ingrese Nombre completo del empleado")
    sexo = input("ingrese el sexo del empleado 'M' o 'f' ")
    direccion = input("ingrese la direccion del empleado")
    telefono = input("ingrese el telefono del empleado")
    cargo = input("ingrese el cargo del empleado")
    fechaingreso = input("ingrese la fecha de ingreso")
    area = input("ingrese el area al cual pertenece")
    departamento = input("ingrese el departamento al cual pertenece")
    contactoEmergencia = input("ingrese el nombre del contacto de emergencia")
    relacion= input("¿Que relacion tiene con el empleado?")
    ceTelefono = input("Ingresa el contacto de emergencia")
    cargas = input("¿El empleado tiene cargas familiares?")
    if cargas == "si":
        input("el empleado tiene cargas familiares")
    elif cargas == "no":
        input("el empleado no tiene cargas familiares")