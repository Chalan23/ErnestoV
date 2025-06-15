# tarea
# hacer un sistema de login con diccionario
# debe verificar si el usuario existe y le pregunta la contraseña 
# solo tiene 3 oportunidades para acertar
# el diccionario debe de estar previamente escrito
# antes de iniciar el sistema

usuarios = {
    "ernesto": 2323,
    "ronaldo": 1111,
    "messi": 2222
}

while True:
    try:
        print("""
              1.-Consulta usuarios
              2.-Ingresar al sistema (iniciar sesion)
              3.-Salir
              """)
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:    
                print("Usuarios registrados:")
                for nombre in usuarios.keys():
                    print(f"- {nombre}")
            case 2:
                usuario = input("Ingrese su nombre de usuario: ")
                if usuario in usuarios:
                    intentos = 0
                    maxIntentos = 3
                    while intentos < maxIntentos:
                        clave = int(input("Ingrese su contraseña: "))
                        if clave == usuarios[usuario]:
                            print("Acceso correcto. Bienvenido!")
                            break
                        else:
                            intentos += 1
                            print(f"Contraseña incorrecta. Intentos restantes: {maxIntentos - intentos}")
                    if intentos == maxIntentos:
                        print("Acceso bloqueado. Demasiados intentos fallidos.")
                else:
                    print("Usuario no encontrado.")
            case 3:
                print("Saliendo del sistema.")
                break
            case _:
                print("Opcion no valida.")
    except Exception:
        print("Por favor, ingrese un numero valido.")
