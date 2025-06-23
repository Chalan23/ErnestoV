# """crear gestion de vehiculos 
# crear programa para un parking de autos
# se debe ingresar marca, año, patente y tipo

# marca: tipo string, se debe tipear la marca 
# año: tipo int, solo de 4 digitos enteros
# patente: debe tener 4 letras minusculas y dos numeros
# tipo: s= sedan, c= camioneta, m= moto

# se debe validar cada aspecto y tener un mantenedor para 
# todos los vehiculos motorizados

# 1.-Ingresa un vehiculo
# 2.-Mostrar un Vehiculo
# 3.-Actualizar Vehiculo
# 4.-Borrar Vehiculo
# 5.-Mostrar estadisticas: Ultimo vehiculo ingresado y total del estacionamiento
# 6.-Salir

# Usar dunciones con argumentos para poder validar
# y para poder llamar las acciones dentro del menú
# """

# vehiculos = {
#     1: {"marca": "jeep",
#         "año":"2025",
#         "patente":"evch23",
#         "tipo":"camioneta"},
#     2: {"marca": "suzuki",
#         "año":"2020",
#         "patente":"eevv11",
#         "tipo":"moto"},
#     3: {"marca": "chevrolet",
#         "año":"2023",
#         "patente":"cchh22",
#         "tipo":"suv"}
# }

# def mostrar_vehiculo(dict):
#     for key, auto in dict.items():
#         print(key, auto)
        

# def validar_pass(clave):
#     mayuscula = False
#     minuscula = False
#     numeros = False
#     for palabra in clave:
#         if palabra.isupper():
#             mayuscula = True
#         if palabra.islower():
#             minuscula = True
#         if palabra.isdigit():
#             numeros = True
#     if mayuscula and minuscula and numeros and len(clave)==6:
#         print("Esta bien escrito.")
#         return True
#     else:
#         print("Esta mal escrito")
#         return False   
# def ingresar_vehiculo(dict):
#     marca = input("Ingrese la marca del vehiculo: ")
#     año = input("Ingrese el año del vehiculo: ")
#     patente = input("Ingrese la patente del vehiculo: ")
#     print("Seleccione el tipo de vehículo:")
#     print("  s - Sedan")
#     print("  c - Camioneta")
#     print("  m - Moto")
#     tipo = input("Ingrese el tipo (s/c/m): ").lower()
#     while tipo not in ['s', 'c', 'm']:
#         print("Tipo inválido. Debe ser 's', 'c' o 'm'.")
#         tipo = input("Ingrese el tipo (s/c/m): ").lower()
    
#     if validar_pass(patente):
#         nuevo_id = max(dict.keys(), default=0) + 1
#         dict[nuevo_id] = {
#             "marca": marca,
#             "año": año,
#             "patente": patente,
#             "tipo": tipo
#         }
#     else:
#         print("Error, no cumple con el parametro")
        
# def actualizar_vehiculo(dict):
#     mostrar_vehiculo(dict)
#     actualizar = int(input("Que vehiculos deseas actualizar: "))
#     while True:
#         print("""
#               1.-Marca 
#               2.-Año
#               3.-Patente
#               4.-Tipo
#               5.-Salir
#               """)
#         dato = int(input("Que dato quieres actualizar: "))
#         match dato:
#             case 1:
#                 act = input("Actualiza la marca: ")
#                 dict[actualizar]["marca"] = act
#             case 2:
#                 act = input("Actualiza el año: ")
#                 dict[actualizar]["año"] = act
#             case 3:
#                 act = input("Actualiza la patente: ")
#                 if validar_pass(act):
#                     dict[actualizar]["patente"] = act
#                 else:
#                     print("El parametro no es correcto")
#             case 4:
#                 act = input("Actualiza el tipo: ")
#                 dict[actualizar]["tipo"] = act
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")

# def borrar_vehiculo(dect):
#     mostrar_vehiculo(dect)
#     borrar = int(input("Selecciona el vehiculo a borrar: "))
#     del dict[borrar]

# def mostrar_estadistica(dict):
#     if not dict:
#         print("No hay vehículos en el estacionamiento.")
#         return
#     total = len(dict)
#     ultimo_id = max(dict.keys())
#     ultimo_vehiculo = dict[ultimo_id]
#     print(f"Total de vehículos en el estacionamiento: {total}")
#     print(f"Último vehículo ingresado (ID {ultimo_id}): {ultimo_vehiculo}")
    

# while True:
#     try:
#         print("""---Menu sistema de estacionamiento---   
#                     1.-Ingresa un vehiculo
#                     2.-Mostrar un Vehiculo
#                     3.-Actualizar Vehiculo
#                     4.-Borrar Vehiculo
#                     5.-Mostrar estadisticas: Ultimo vehiculo ingresado y total del estacionamiento
#                     6.-Salir""")
#         opcion = int(input("Selecciona una opcion: "))
#         match opcion:
#             case 1: 
#                 ingresar_vehiculo(vehiculos)
#             case 2: 
#                 mostrar_vehiculo(vehiculos)
#             case 3: 
#                 actualizar_vehiculo(vehiculos)
#             case 4: 
#                 borrar_vehiculo(vehiculos)
#             case 5: 
#                 print(vehiculos)
#             case 6:
#                 print("Saliendo...")
#                 break 
#             case _: 
#                 print("Error, seleciona una opcion valida")
#     except Exception as e:
#         print("Error")


# -----------------------------------------------------------------

