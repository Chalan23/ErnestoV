# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1. Pago de Tarjeta de Crédito:
# a. El usuario comienza con una deuda de $100.000
# b. El usuario puede ingresar un monto para realizar un pago en la
# tarjeta de crédito.
# c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d. Se debe verificar que el monto a pagar no exceda el saldo actual de
# la tarjeta.
# e. Al pagar el sistema debe descontar de la deuda total
# f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
# saldo de la tarjeta.
# 2. Simulación de Compras:
# a. El usuario puede simular realizar un número ilimitado de compras.
# b. Para cada compra, se solicita al usuario ingresar el monto de la
# compra. El programa suma los montos de cada compra.
# c. Se verifica que el monto de la compra sea mayor o igual a cero.
# d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
# iteración del bucle for.
# 3. Salir:
# a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.
# A considerar:
# 1. Manejo de Errores:
# a. Se utilizan bloques try y except para manejar posibles errores al
# ingresar datos, validar valores no numéricos y errores inesperados.
# . Se debe programar mensajes de error específicos para guiar al
# usuario sobre posibles problemas.

# deuda = 100000

# while True:
#     print("\nMenú principal:")
#     print("1. Pago de Tarjeta de Crédito")
#     print("2. Compras con tarjeta de crédito")
#     print("3. Salir")
#     try:
#         opcion = int(input("Seleccione una opción: "))
#         match opcion:
#             case 1:
#                 print(f"Su deuda actual es: ${deuda}")
#                 try:
#                     montoPago = int(input("Ingrese el monto a pagar: "))
#                     if montoPago <= 0:
#                         print("Error: el monto debe ser mayor a 0.")
#                     elif montoPago > deuda:
#                         print(f"Error: el monto no puede ser mayor a la deuda ${deuda}.")
#                     else:
#                         deuda -= montoPago
#                         print(f"Pago realizado. Su deuda actual es: ${deuda}")
#                 except Exception:
#                     print("Error: debe ingresar un número válido.")
#             case 2:
#                 print("Simulador de compras. Ingrese 0 para volver al menú principal.")
#                 while True:
#                     try:
#                         montoCompra = int(input("Ingrese el monto de la compra: "))
#                         if montoCompra == 0:
#                             break
#                         elif montoCompra < 0:
#                             print("Error: el monto debe ser mayor o igual a 0.")
#                         else:
#                             deuda += montoCompra
#                             print(f"Compra realizada por ${montoCompra}. Su deuda actual es: ${deuda}")
#                     except Exception:
#                         print("Error: debe ingresar un número válido.")
#             case 3:
#                 print("Saliendo del programa...")
#                 break
#             case _:
#                 print("Opción no válida, por favor intente de nuevo.")
#     except Exception:
#         print("Error: debe ingresar un número válido.")
# ---------------------------------------------------------------------------------------

# Debe crear un menú de inicio de sesión, en el cual se debe mostrar los siguientes campos:
# 1) iniciar sesión
# 2) registrar usuario
# 3) salir
# Para lo cual usted deberá haber creado 3 variables de usuario y 3 variables de contraseña,
# ambas con valor inicial vacío, ejemplo:
# • usuario1= None
# • usuario2=None
# • usuario3=None
# • contrasena1= None
# • contrasena2=None
# • contrasena3= None
# Si se selecciona la opción 1 y no existen registros de usuarios, el sistema deberá indicar que
# es necesario registrar un usuario antes, y volverá al menú principal, en el caso de que
# ingrese el usuario y contraseña correctamente, entonces el sistema mostrará el siguiente
# menú:
# 1) Realizar llamada
# 2) Enviar correo electrónico
# 3) Cerrar sesión
# Donde la opción 1 debe solicitar un número de celular, éste deberá comenzar con 9 y su
# tamaño es de 9 dígitos (ejemplo: 985447561).
# La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de
# “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
# También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”
# Finalmente cerrar sesión, volverá al menú principal.
# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre
# esto, entonces el sistema emite un error y vuelve a solicitar la opción.
# Recuerde utilizar try Exception en caso de ser necesario.
# Instrucciones para el envío de la actividad
# El representante del grupo deberá comprimir los programas y enviar al docente a través de
# Mensajes de AVA, utilizando el siguiente formato para el nombre del archivo:


usuario1= None
usuario2=None
usuario3=None
contrasena1= None
contrasena2=None
contrasena3= None

while True:
    try:
        op = int(input("""
Seleccione una opción:
1.- Iniciar sesión
2.- Registrar usuario
3.- Salir
> """))
    except Exception:
        print("Error: debe ingresar un número válido.")
        

    match op:
        case 1:

            if all(u is None for u in [usuario1, usuario2, usuario3]):
                print("No hay usuarios registrados, por favor registre un usuario primero.")
                

            print("Iniciar sesión")
            usuario = input("Ingrese nombre de usuario: ")
            contrasena = input("Ingrese contraseña: ")


            if (usuario == usuario1 and contrasena == contrasena1) or \
               (usuario == usuario2 and contrasena == contrasena2) or \
               (usuario == usuario3 and contrasena == contrasena3):
                print("¡Sesión iniciada correctamente!")

                while True:
                    try:
                        op2 = int(input("""
Menú de usuario:
1) Realizar llamada
2) Enviar correo electrónico
3) Cerrar sesión
> """))
                    except Exception:
                        print("Error: debe ingresar un número válido.")
                        

                    if op2 == 1:
                        numero = input("Ingrese número de celular (9 dígitos, comienza con 9): ")
                        if len(numero) == 9 and numero.isdigit() and numero[0] == "9":
                            print(f"Llamando al número {numero}...")
                        else:
                            print("Error: el número debe comenzar con 9 y tener 9 dígitos.")
                    elif op2 == 2:
                        while True:
                            correo = input("Ingrese correo electrónico: ")
                            tiene_arroba = False
                            for c in correo:
                                if c == "@":
                                    tiene_arroba = True
                                    break
                            if tiene_arroba:
                                break
                            else:
                                print("Error: el correo debe contener '@'.")
                        mensaje = input("Ingrese el mensaje a enviar: ")
                        print(f"Correo enviado a {correo} con el mensaje: {mensaje}")
                    elif op2 == 3:
                        print("Cerrando sesión...")
                        break
                    else:
                        print("Opción inválida, intente de nuevo.")
            else:
                print("Usuario o contraseña incorrectos.")

        case 2:
            print("Registrar usuario")
            if usuario1 is None:
                usuario1 = input("Ingrese nombre de usuario1: ")
                contrasena1 = input("Ingrese contraseña de usuario1: ")
                print("Usuario 1 registrado correctamente.")
            elif usuario2 is None:
                usuario2 = input("Ingrese nombre de usuario2: ")
                contrasena2 = input("Ingrese contraseña de usuario2: ")
                print("Usuario 2 registrado correctamente.")
            elif usuario3 is None:
                usuario3 = input("Ingrese nombre de usuario3: ")
                contrasena3 = input("Ingrese contraseña de usuario3: ")
                print("Usuario 3 registrado correctamente.")
            else:
                print("No hay espacio para más usuarios.")

        case 3:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida, intente de nuevo.")







