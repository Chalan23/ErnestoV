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
# notas debe incluir while o for, tambien debe incluir match y try except exception 
# y no debe incluir listas o tuplas ni def, debe ser un codigo simple 


usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

while True:
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    try:
        op = int(input("Opción: "))
    except Exception:
        print("Error: debe ingresar un número.")
        continue

    match op:
        case 1:
            if usuario1 is None and usuario2 is None and usuario3 is None:
                print("Debe registrar un usuario primero.")
                continue
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if (usuario == usuario1 and contrasena == contrasena1) or (usuario == usuario2 and contrasena == contrasena2) or (usuario == usuario3 and contrasena == contrasena3):
                print("Sesión iniciada")
                while True:
                    print("1. Realizar llamada")
                    print("2. Enviar correo electrónico")
                    print("3. Cerrar sesión")
                    try:
                        op2 = int(input("Opción: "))
                    except Exception:
                        print("Error: debe ingresar un número.")
                        continue
                    match op2:
                        case 1:
                            num = input("Ingrese número celular: ")
                            if len(num) == 9 and num[0] == "9" and num.isdigit():
                                print("Llamando a", num)
                            else:
                                print("Número inválido. Debe comenzar con 9 y tener 9 dígitos.")
                        case 2:
                            while True:
                                correo = input("Ingrese correo: ")
                                tiene_arroba = False
                                for c in correo:
                                    if c == "@":
                                        tiene_arroba = True
                                if tiene_arroba:
                                    mensaje = input("Mensaje: ")
                                    print("Correo enviado.")
                                    break
                                else:
                                    print("Correo inválido, debe tener '@'.")
                        case 3:
                            print("Sesión cerrada.")
                            break
                        case _:
                            print("Opción inválida.")
            else:
                print("Usuario o contraseña incorrectos.")
        case 2:
            if usuario1 is None:
                usuario1 = input("Nuevo usuario: ")
                contrasena1 = input("Contraseña: ")
                print("Usuario registrado.")
            elif usuario2 is None:
                usuario2 = input("Nuevo usuario: ")
                contrasena2 = input("Contraseña: ")
                print("Usuario registrado.")
            elif usuario3 is None:
                usuario3 = input("Nuevo usuario: ")
                contrasena3 = input("Contraseña: ")
                print("Usuario registrado.")
            else:
                print("Ya hay 3 usuarios.")
        case 3:
            print("Chao gracias.")
            break
        case _:
            print("Opción inválida.")







