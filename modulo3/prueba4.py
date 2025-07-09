# Este programa gestiona la venta y administración de entradas para un evento
# mediante un sistema interactivo de menú. Permite a los usuarios realizar las 
# siguientes operaciones:

# Comprar entrada: Solicita el nombre del comprador, el tipoEntrada de entrada (General o VIP) 
# y un codigo de confirmación que debe cumplir con criterios específicos 
# (contener al menos una letra mayúscula, una minúscula, un número y tener una 
# longitud de seis caracteres). Si el codigo es válido y el nombre no esta 
# previamente registrado, registra la compra almacenando la información del comprador.

# Consultar comprador: Permite buscar un comprador registrado mediante su nombre, 
# mostrando el tipoEntrada de entrada y el codigo de confirmación asociados.

# Cancelar compra: Permite eliminar la información de un comprador registrado, 
# cancelando así su compra.

# Salir: Finaliza la ejecución del programa.

# El programa se ejecuta en un bucle continuo mostrando un menú principal que 
# solicita al usuario seleccionar una opción para realizar las acciones descritas, 
# manejando entradas inválidas y errores de forma controlada.

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


