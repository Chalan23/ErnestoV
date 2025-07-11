# # Este programa gestiona la venta y administración de entradas para un evento
# # mediante un sistema interactivo de menú. Permite a los usuarios realizar las 
# # siguientes operaciones:

# # Comprar entrada: Solicita el nombre del comprador, el tipoEntrada de entrada (General o VIP) 
# # y un codigo de confirmación que debe cumplir con criterios específicos 
# # (contener al menos una letra mayúscula, una minúscula, un número y tener una 
# # longitud de seis caracteres). Si el codigo es válido y el nombre no esta 
# # previamente registrado, registra la compra almacenando la información del comprador.

# # Consultar comprador: Permite buscar un comprador registrado mediante su nombre, 
# # mostrando el tipoEntrada de entrada y el codigo de confirmación asociados.

# # Cancelar compra: Permite eliminar la información de un comprador registrado, 
# # cancelando así su compra.

# # Salir: Finaliza la ejecución del programa.

# # El programa se ejecuta en un bucle continuo mostrando un menú principal que 
# # solicita al usuario seleccionar una opción para realizar las acciones descritas, 
# # manejando entradas inválidas y errores de forma controlada.

# cliente = {
#     1:{"nombre":"ernesto", 
#        "entrada":"V",
#        "codigo":"EErr23"},
#     2:{"nombre":"meme", 
#        "entrada":"G",
#        "codigo":"MMee23"}
# }

# def comprarEntrada(dicc):
#     nombre=input("Ingresa el nombre: ")
#     entrada=input("Ingresa la entrada general(G) o vip(V): ")
#     print("""
#           Recuerda el codigo debe tener 6 caracteres
#           2 mayuscula, 2 minuscula y 2 numero""")
#     codigo=input("Ingresa el codigo: ")
#     if codiValido(codigo):
#         clienteNuevo = max(dicc.keys()) + 1
#         dicc[clienteNuevo]={"nombre":nombre,
#                        "entrada":entrada,
#                        "codigo":codigo}
#     else:
#         print("El parametro del codigo no es correcto")

# def borrarCliente(dicc):
#     mostrarCliente(dicc)
#     borrar = int(input("Cual quieres borrar: "))
#     del dicc[borrar]
    
# def mostrarCliente(dicc):
#     for key, cliente in dicc.items():
#         print(key, cliente)

# def codiValido(codigo):
#     mayuscula = False
#     minuscula = False
#     numero = False
#     for palabra in codigo:
#         if palabra.isupper():
#             mayuscula = True
#         if palabra.islower():
#             minuscula = True
#         if palabra.isdigit():
#             numero = True
#     if mayuscula and minuscula and numero and len(codigo)==6:
#         print("Los parametros estan bien")
#         return True
#     else:
#         print("Los parametros estan mal")
#         return False

# while True:
#     try:
#         print("""
#                     ---Menu---
#                 1.-Comprar entrada
#                 2.-Consultar comprador 
#                 3.-Cancelar compra 
#                 4.-Salir
#                 """)
#         opc = int(input("Seleciona una opcion: "))
#         match opc:
#             case 1:
#                 comprarEntrada(cliente)
#             case 2:
#                 mostrarCliente(cliente)
#             case 3:
#                 borrarCliente(cliente)
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, seleciona una opcion valida.")
#     except Exception as e:
#         print("Error.", e)

# ------------------------------------------------------------------------------------

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
#         if patente in stock:
#             del stock[patente]
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


# -------------------------------------------------------------------------------------------

# carrito de compra 
# con el siguiente menu
# Validar codigo, mostrar producto, borrar producto, 
# actualizar producto, precio mayor, comprar producto

productos = {
    1:{"producto":"leche",
       "precio":1000,
       "codigo":"LLee10"},
    2:{"producto":"jugo",
       "precio":1200,
       "codigo":"JJuu12"},
    3:{"producto":"cereal",
       "precio":1500,
       "codigo":"CCee15"}
}

def valiCode(codigo):
    mayus = False
    minus = False
    num = False
    for palabra in codigo:
        if palabra.isupper():
            mayus = True
        if palabra.islower():
            minus = True
        if palabra.isdigit():
            num = True 
    if mayus and minus and num and len(codigo)==6:
        print("Codigo correcto")
        return True
    else:
        print("Codigo incorrecto")
        return False

def mostrarPro(dicc):
    for key, productos in dicc.items():
        print(key, productos)

def eliminarPro(dicc):
    mostrarPro(dicc)
    eliminar = int(input("Que producto deseas borrar: "))
    del dicc[eliminar]

def comprarPro(dicc):
    mostrarPro(dicc)
    idPro = int(input("Selecciona el numero del producto que deseas comprar: "))
    if idPro in dicc:
        print(f"Has comprado '{dicc[idPro]['producto']}' por ${dicc[idPro]['precio']}.")
    else:
        print("Producto no encontrado.")

def precioMayor(dicc):
    if dicc:
        mayor = 0
        nombre = ""
        for key in dicc:
            if dicc[key]["precio"] > mayor:
                mayor = dicc[key]["precio"]
                nombre = dicc[key]["producto"]
        print(f"Producto mas caro: '{nombre}' - ${mayor}")
    else:
        print("No hay productos.")

def actualizarPRo(dicc):
    mostrarPro(dicc)
    act = int(input("Seleciona un articulo: "))
    while True:
        print("""
              1.-producto
              2.-precio
              3.-codigo
              4.-salir
              """)
        dato=int(input("Que dato vas actualizar: "))
        match dato:
            case 1:
                nuevo=input("Ingresa el nuevo nombre: ")
                dicc[act]["producto"]=nuevo
            case 2:
                nuevo=int(input("Ingresa el nuevo precio: "))
                dicc[act]["precio"]=nuevo
            case 3:
                nuevo=input("Ingresa el nuevo codigo: ")
                if valiCode(nuevo):
                    dicc[act]["codigo"]=nuevo
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Error, elige una opcion valida")

while True:
    try:
        print("""
              °°°menu°°°
              1.-Comprar producto 
              2.-mostrar producto
              3.-eliminar producto 
              4.-precio mayor 
              5.-actualizar producto
              6.-salir
              """)
        opc = int(input("Seleciona una opcion: "))
        match opc:
            case 1:
                comprarPro(productos)
            case 2:
                mostrarPro(productos)
            case 3:
                eliminarPro(productos)
            case 4:
                precioMayor(productos)
            case 5:
                actualizarPRo(productos)
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Error, seleciona una opcion valida")
    except Exception as e:
        print("Error.", e)
        



