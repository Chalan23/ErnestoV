# autos = {
#     'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
#     'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
#     'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
#     'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L']
# }

# stock = {
#     'ABC123': [14, 12500000],
#     'DEF456': [0, 10400000],
#     'GHI789': [4, 17900000],
#     'JKL321': [6, 15500000],
#     'ZZZ000': [2, 8900000]
# }

# def mostrar(diccionario):
#     for clave, valor in diccionario.items():
#         print(clave, valor)

# def borrar(autos):
#     mostrar(autos)
#     patente = input("Que vas a borrar (escribe la patente): ")
#     if patente in autos:
#         del autos[patente]
#         print("Patente borrada.")
#     else:
#         print("Patente no encontrada.")

# def validarCode(codigo):
#     mayus = False 
#     minus = False
#     num = False
#     for letra in codigo:
#         if letra.isupper():
#             mayus = True
#         if letra.islower():
#             minus = True
#         if letra.isdigit():
#             num = True
#     if mayus and minus and num and len(codigo) == 6:
#         print("Correcto")
#         return True
#     else:
#         print("Incorrecto")
#         return False

# def atcStock(stock):
#     mostrar(stock)
#     patente = input("Cuul quieres actualizar (patente): ")
#     if patente in stock:
#         nuevoStock = int(input("Nuevo stock: "))
#         precio = stock[patente][1] 
#         stock[patente] = [nuevoStock, precio]
#         print("Stock actualizado")
#     else:
#         print("Patente no encontrada.")

# def precioMayor(stock):
#     autoMasCaro = 0
#     patenteMasCara = ""
#     for patente, datos in stock.items():
#         precio = datos[1]
#         if precio > autoMasCaro:
#             autoMasCaro = precio
#             patenteMasCara = patente
#     if autoMasCaro > 0:
#         print(f"El precio más alto es {patenteMasCara} con ${autoMasCaro}")
#     else:
#         print("No hay autos en stock.")

# def actAuto(autos):
#     mostrar(autos)
#     patente = input("Ingresa la patente del vehículo a actualizar: ")
#     if patente not in autos:
#         print("Patente no encontrada.")
#         return
#     print("""
#           1.- Actualizar patente
#           2.- Actualizar marca
#           3.- Actualizar año
#           4.- Actualizar tipo de motor
#           5.- Actualizar cilindrada
#           """)
#     opcion = int(input("¿Qué dato deseas actualizar?: "))
#     match opcion:
#         case 1:
#             nuevaPatente = input("Ingresa la nueva patente: ")
#             autos[nuevaPatente] = autos.pop(patente)
#             print("Patente actualizada.")
#         case 2:
#             nuevaMarca = input("Nueva marca: ")
#             autos[patente][0] = nuevaMarca
#             print("Marca actualizada.")
#         case 3:
#             nuevo_anio = int(input("Nuevo año: "))
#             autos[patente][1] = nuevo_anio
#             print("Año actualizado.")
#         case 4:
#             nuevo_motor = input("Nuevo tipo de motor: ")
#             autos[patente][2] = nuevo_motor
#             print("Motor actualizado.")
#         case 5:
#             nuevaCilindrada = input("Nueva cilindrada: ")
#             autos[patente][3] = nuevaCilindrada
#             print("Cilindrada actualizada.")
#         case _:
#             print("Opción incorrecta.")

# while True:
#     try:
#         print("""
#         °°° Menu °°°
#     1.- Mostrar stock de cada uno 
#     2.- Buscar precio más alto 
#     3.- Actualizar stock 
#     4.- Borrar un modelo (solo en autos)
#     5.- Actualizar datos vehículo
#     6.- Salir""")
#         op = int(input("Selecciona una opción: "))
#         match op:
#             case 1:
#                 mostrar(stock)
#             case 2:
#                 precioMayor(stock)
#             case 3:
#                 atcStock(stock)
#             case 4:
#                 borrar(autos)
#             case 5:
#                 actAuto(autos)
#             case 6:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, elige una opción correcta")
#     except Exception as e:
#         print("Error:", e)

# --------------------------------------------------------------
