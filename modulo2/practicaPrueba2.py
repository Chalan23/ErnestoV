# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# $ while sirve para iterar un bloque de codigo hasta que deje de cumplirse la funcion. 
# $ ejecuta el codigo siempre que sea True y si ya es False termina el bucle. 

# % for sirve para iterar sobre una coleccion de elementos.
# % es decir puede recorrer elemento a elemento ejecutando el mismo bloque de codigo. 

# match nos permite ordenar el codigo es ideales para menus 

# & break nos permite detener el bucle y salir de él aun que la expresion sea true.
# & continue nos permite terminar la iteracion aun que no haya llegado al final y seguir con la siguiente.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Ejemplo: while
# contador = int(input("Ingrese un numero: "))

# while contador != 0:
#     contador -= 1
#     print(f"Los numeros son: {contador}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Ejemplo: for, break y continue
# for numero in range(5):
#     if numero == 3:
#         break 
#     print(numero)
    
# for numero in range(5):
#     if numero == 3:
#         continue
#     print(numero)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Ejemplo: match  
# op = int(input("Seleciona una opcion: "))

# match op:
#     case 1: 
#         print("Ver perfil")
#     case 2:
#         print("Editar perfil")
#     case 3:
#         print("Cerrar sesion")
#     case _:
#         print("Opcion invalida")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # ejericio while 1
# # escribe un programa que pida al usuario ingresar numeros positivo.
# # el programa debe seguir pidiendo numeros hasta que el usuario ingrese un numero negativo.
# # al final muestra la suma de los numeros positivos ingresados.

# print("""
#       Ingrese un numero positivo para sumar 
#       para finalizar ingresa un numero negativo o cero
#       """) 
# suma = 0
# try:
#     num = int(input("Ingrese un numero: "))
#     while num > 0:
#         suma += num
#         num = int(input("Ingrese otro numero: "))
#     print(f"La suma total de los numeros es {suma}")
# except ValueError:
#     print("Por favor, ingrese un numero valido.")
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Objetivo: Crear un sistema de compras con menú.
# # Requisitos:
# # Mostrar un menú con las opciones:
# # Ingresar nombre de usuario
# # Agregar productos (elige entre 3 productos predefinidos con precios)
# # Mostrar boleta (precio neto, IVA, total)
# # Salir

# print("Bienvenido al carrito de compras!")
# nombre = input("Cual es su nombre: ")

# def productos():
#     print("""
#         1.-Leche $1.000 
#         2.-Cereal $2.000
#         3.-Jugo $1.500
#         4.-Salir 
#         """)
# def op():
#     total=0
#     while True:
#         productos()
#         try:
#             op = int(input("Ingresa el numero del producto que vas a comprar: "))
#         except ValueError:
#             print("Debe ingresar un numero!")
#         match op:
#             case 1:
#                 total+=1000
#                 print(f"""Usted lleva leche
#                       Su SubTotal es es {total}
#                       """)
#             case 2:
#                 total+=2000
#                 print(f"""Usted lleva Cereal
#                       Su SubTotal es es {total}
#                       """)
#             case 3:
#                 total+=1500
#                 print(f"""Usted lleva Jugo
#                       Su SubTotal es es {total}
#                       """)
#             case 4:
#                 print("Saliendo del sistema")
#                 break
            
#             case _:
#                 print("Ingresa una opcion valida")
                
#     print(f"""
#             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#             Gracias por su compra {nombre}
#             valor neto es de {total}
#             Total con IVA incluido {total*1.19}
#             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#             """)
# op()