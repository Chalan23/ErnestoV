# corredores = ["slatan","bombasi","lando"]
# tiempos = [10.9,11.1,12.5]

# while True:
#     try:
#         print("""
#             1.-Registrar corredor y tiempo
#             2.-Ver lista de corredores
#             3.-Ver estadisticas (Tiempo menor, tiempo mayor, ordenador por mas rapidos)
#             4.-Salir
#             """)
#         opcion = int(input("Selecione una opcion: "))
#         match opcion:
#             case 1:
#                 corre=input("Ingrese el nombre del corredores: ")
#                 corredores.append(corre)
#                 tie=float(input("Registre su mejor tiempo: "))
#                 tiempos.append(tie)
#             case 2:
#                 for i in range(len(corredores)):
#                     print(f"Corredor: {corredores[i]} , Tiempo: {tiempos[i]}")
#             case 3:
#                 print("El tiempo mas bajo es", min(tiempos))   
#                 print("El tiempo mas alto es", max(tiempos))   
#                 print("Ordenados por mas rapido a mas lento")   
#                 print("El tiempo mas alto es", max(tiempos))
#                 tiempos.sort()
#                 print(tiempos)
            # case _:
            #     print("Opcion invalida")
#     except Exception as e:
#         print("Error, selecione una opcion valida")

# ---------------------------------------------------------------------------------------

# productos = {
#     "lapiz":100,
#     "goma":100,
#     "estuche":500,
#     "plumon":1000
# }
# # agregar productos
# # print(productos)
# # productos["corrector"]=2000
# # print(productos)

# while True:
#     try:
#         print("""
#               1.-Agregar articulos
#               2.-ver listado
#               3.-borrar articulos
#               4.-actualizar precio
#               5.-salir
#               """)
#         opcion=int(input("Selecione una opcion: "))
#         match opcion:
#             case 1:
#                 art=input("Ingrese el nombre del articulo: ")
#                 precio=int(input("Ingrese el precio del articulo: "))
#                 productos[art]=precio
#             case 2:
#                 for nom, precio in productos.items():
#                     print(nom, "$", precio)
#             case 3:
#                 borrar=input("Cual es el articulo que desea borrar: ")
#                 del productos[borrar]
#                 print(f"El articulo {borrar} fue borrado")
#             case 4:
#                 for nom, precio in productos.items():
#                     print(nom, "$", precio)
#                 art=input("Cual es el articulo que desea actualizar: ")
#                 if art in productos:
#                     precio=int(input("Ingrese el nuevo precio: "))
#                     productos[art]=precio
#                 else:
#                     print("El articulo no existe")
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception as error:
#         print("Error, hiciste algo mal", error)

# ---------------------------------------------------------------------------------------

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
        opcion = int(input("Ingresa una opcion: "))
        match opcion: 
            case 1:
                print("Usuarios regitrados:")
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
                        print("Usuario no encontrado")
            case 3:
                print("Saliendo del sistema")
                break
            case _:
                print ("opcion no valida")
    except Exception:
        print("Por favor, ingresa un numero valido")


