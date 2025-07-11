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

autos = {
    'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
    'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
    'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
    'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L']
}

stock = {
    'ABC123': [14, 12500000],
    'DEF456': [0, 10400000],
    'GHI789': [4, 17900000],
    'JKL321': [6, 15500000],
    'ZZZ000': [2, 8900000]
}


def mostrar(diccionario):
    for clave, valor in diccionario.items():
        print(clave, valor)

def borrar(autos):
    mostrar(autos)
    patente = input("Que vas a borrar (escribe la patente): ")
    if patente in autos:
        del autos[patente]
        print("Patente borrada.")
    else:
        print("Patente no encontrada.")

def atcStock(stock):
    mostrar(stock)
    patente = input("Cuál quieres actualizar (patente): ")
    if patente in stock:
        nuevoStock = int(input("Nuevo stock: "))
        precio = stock[patente][1] 
        stock[patente] = [nuevoStock, precio]
        print("Stock actualizado")
    else:
        print("Patente no encontrada.")

def validarCode(codigo):
    mayus = False 
    minus = False
    num = False
    for letra in codigo:
        if letra.isupper():
            mayus = True
        if letra.islower():
            minus = True
        if letra.isdigit():
            num = True
    if mayus and minus and num and len(codigo) == 6:
        print("Correcto")
        return True
    else:
        print("Incorrecto")
        return False

def precioMayor(stock):
    autoMasCaro = 0
    patenteMasCara = ""
    for patente, datos in stock.items():
        precio = datos[1]
        if precio > autoMasCaro:
            autoMasCaro = precio
            patenteMasCara = patente
    if autoMasCaro > 0:
        print(f"El auto con el precio más alto es {patenteMasCara} con ${autoMasCaro}")
    else:
        print("No hay autos en stock.")

def actAuto(autos):
    mostrar(autos)
    patente = input("Ingresa la patente del vehículo a actualizar: ")
    if patente not in autos:
        print("Patente no encontrada.")
        return
    print("""
          1.- Actualizar patente
          2.- Actualizar marca
          3.- Actualizar año
          4.- Actualizar tipo de motor
          5.- Actualizar cilindrada
          """)
    opcion = int(input("¿Qué dato deseas actualizar?: "))
    
    match opcion:
        case 1:
            nueva_patente = input("Ingresa la nueva patente: ")
            autos[nueva_patente] = autos.pop(patente)
            print("Patente actualizada.")
        case 2:
            nueva_marca = input("Nueva marca: ")
            autos[patente][0] = nueva_marca
            print("Marca actualizada.")
        case 3:
            nuevo_anio = int(input("Nuevo año: "))
            autos[patente][1] = nuevo_anio
            print("Año actualizado.")
        case 4:
            nuevo_motor = input("Nuevo tipo de motor: ")
            autos[patente][2] = nuevo_motor
            print("Motor actualizado.")
        case 5:
            nueva_cilindrada = input("Nueva cilindrada: ")
            autos[patente][3] = nueva_cilindrada
            print("Cilindrada actualizada.")
        case _:
            print("Opción incorrecta.")

# Menú principal
while True:
    try:
        print("""
        °°° Menú °°°
    1.- Mostrar stock de cada uno 
    2.- Buscar precio más alto 
    3.- Actualizar stock 
    4.- Borrar un modelo (solo en autos)
    5.- Actualizar datos vehículo
    6.- Salir
    7.- Mostrar diccionario consolidado
        """)
        op = int(input("Selecciona una opción: "))
        match op:
            case 1:
                mostrar(stock)
            case 2:
                precioMayor(stock)
            case 3:
                atcStock(stock)
            case 4:
                borrar(autos)
            case 5:
                actAuto(autos)
            case 6:
                print("Saliendo...")
                break
            case 7:
                consolidado =(autos, stock)
                print("\n--- Diccionario Consolidado ---")
                mostrar(consolidado)
            case _:
                print("Error, elige una opción correcta")
    except Exception as e:
        print("Error:", e)
