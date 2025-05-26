# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# $ while sirve para iterar un bloque de codigo hasta que deje de cumplirse la funcion. 
# $ ejecuta el codigo siempre que sea True y si ya es False termina el bucle. 

# % for sirve para iterar sobre una coleccion de elementos.
# % es decir puede recorrer elemento a elemento ejecutando el mismo bloque de codigo. 

# match nos permite ordenar el codigo es ideales para menus 

# & break nos permite detener el bucle y salir de él aun que la expresion sea true.
# & continue nos permite terminar la iteracion aun que no haya llegado al final y seguir cantidadConejos la siguiente.
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

# # Objetivo: Crear un sistema de compras cantidadConejos menú EJERCICIO 2
# # Requisitos:
# # Mostrar un menú cantidadConejos las opciones:
# # Ingresar nombre de usuario
# # Agregar productos (elige entre 3 productos predefinidos cantidadConejos precios)
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
#             Total cantidadConejos IVA incluido {total*1.19}
#             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#             """)
# op()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # EJERCICIO 3
# # calcular tus gastos 
# # el usuario debe calcular sus gastos uno por uno hasta escribir 0
# # luego el programa muestra gastos totales 

# total = 0

# while True:
#     try:
#         gastos=int(input("Ingresa tus gastos (0 para salir): "))
#         if gastos == 0:
#             break
#         total += gastos
#     except ValueError:
#         print("Ingresa un numero valido") 
# print(f"El monto total gastado es {total}")
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# EJERCICIO 4
#perros de casa 
# pida al usuario la cantidad de perros 
# muestre cual es la cuota minima de conejos 
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minina 
# cumplio la cuota, sino se queda sin filete 
# mostrar resumen de perro que cumplieron y los que no

# conejos = 0
# cuotaConejos = int(input("Cuanto es la cuota de conejos: "))
# perros = int(input("Ingrese la cantidad de perros: "))

# for i in range(perros):
#     nombrePerro = input(f"Ingresa el nombre del perro {i+1}: ")
#     ConejosCazados = int(input(f"Cuantos conejos trajo el perro {nombrePerro}: "))
#     if ConejosCazados >= cuotaConejos:
#         print(f"{nombrePerro} Cumplio la cuota de conejos tiene un filete de premio!")
#         conejos += ConejosCazados
#     else: 
#         print(f"{nombrePerro} No cumplio la cuota pero le dare pollito por el esfuerzo")
# print(f"El total de conejos fue de {conejos}")

# import random
# import time
# cuota = 3
# cumple = 0

# while True:
#     try:
#         perros = int(input("Ingrese la cantidad de perros: "))
#         break
#     except ValueError:
#         print("Esto solo acepta numeros enteros")

# for i in range(perros):
#     time.sleep(1)
#     print("Esperando a los perros...")
#     cantidadConejos = random.randint(0, 5)
#     print(f"El perro {i+1} trajo {cantidadConejos} conejos")
#     if cantidadConejos >= cuota:
#         print(f"El perro gana filete")
#         cumple += 1
#     else:
#         print(f"El perro no gana filete")
# print(f"La cantidad de perros que cumplieron la cuota es de: {cumple}")
# print(f"La cantidad de perros que no cumplieron la cuota es de: {perros - cumple}")
# print(f"El total de conejos es de {cumple * cuota}")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# En una granja se está llevando el conteo de comidas entregadas a cerdos.
# Usa un while que se repita hasta que el usuario escriba "fin".
# En cada iteración, pregunta por la cantidad de comida entregada.
# Usa try-except para validar que el usuario ingrese un número entero.
# Suma todas las comidas válidas.
# Al final, muestra el total entregado.

# comida = 0
# while True:
#     try:
#         comidaEntregada = input("Ingrese la cantidad de comida entregada (o 'fin' para terminar): ")
#         if comidaEntregada.lower() == "fin":
#             break
#         comidaEntregada = int(comidaEntregada)
#         comida += comidaEntregada
#     except ValueError:
#         print("Por favor, ingrese un número entero válido.")
# print(f"El total de comida entregada es: {comida} kg")


# # Se está realizando un concurso de lanzamiento de huesos para perros.
# # Hay 4 participantes.
# # Por cada uno, pide la distancia lanzada.
# # Usa try-except para validar que sea un número flotante.
# # Guarda la mayor distancia y el nombre del ganador.
# # Al final, muestra quién ganó y con qué distancia.

# participantes = 4
# metros = 0
# ganador = ""

# for i in range(participantes):
#     nombre = input(f"Ingrese el nombre del participante {i+1}: ")
#     try:
#         distancia = float(input(f"Ingrese la distancia lanzada por {nombre} (en metros): "))
#         if distancia > metros:
#             metros = distancia
#             ganador = nombre
#     except ValueError:
#         print("Por favor, ingrese un número válido para la distancia.")
# print(f"El ganador es {ganador} con una distancia de {metros} metros.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# lavar ropa 
# la lavadora lava maximo 12kg de ropa 
# por cada carga de ropa se usa 200 grs de detergente 
# si es ropa de color solo detergente 
# si es ropa blanca debe agregar 50 ml de cloro
# evaluar si las condiciones se cumplen para lavar ropa

# print("Lavadora Automática")
# print("""
#       Para usar la lavadora debe considerar:
#       Ropa color: detergente 200grs
#       Ropa blanca: detergente 200grs y cloro 50ml
# """)

# while True:
#     try:
#         ropa = float(input("¿Cuánta ropa desea lavar? (kg): "))
#     except ValueError:
#         print("Debe ingresar un número válido para la cantidad de ropa.")
#         continue
#     if ropa > 12 or ropa <= 0:
#         print("No puede lavar esa cantidad de ropa. El máximo es 12kg y debe ser mayor a 0.")
#         continue
#     tipoRopa = input("¿La ropa es blanca o de color? (blanca/color): ").lower()
#     if tipoRopa not in ["blanca", "color"]:
#         print("Debe indicar si la ropa es 'blanca' o 'color'.")
#         continue
#     detergente = input("¿Tiene al menos 200gr de detergente? (si/no): ").lower()
#     if detergente != "si":
#         print("No puede lavar la ropa sin suficiente detergente.")
#         continue
#     if tipoRopa == "blanca":
#         cloro = input("¿Tiene al menos 50ml de cloro? (si/no): ").lower()
#         if cloro != "si":
#             print("No puede lavar ropa blanca sin cloro suficiente.")
#             continue
#         else:
#             print("Puede lavar ropa blanca. ¡Lavado iniciado!")
#     else:
#         print("Puede lavar ropa de color. ¡Lavado iniciado!")
#     break 

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # poner la mesa 

# import time
# jugo = 1000
# comida = 700

# familia = int(input("Cuantos familiares son: "))

# for i in range(familia):
#     print("poner platos")
#     time.sleep(1)
#     print("poner vasos")
#     time.sleep(1)
#     print("poner cubiertos")
#     time.sleep(1)
#     if jugo > 200:
#         print("Llenar el vaso")
#         jugo -= 200
#         print(f"Queda {jugo} de jugo")
#         time.sleep(2)
#     else:
#         print("No queda jugo")
        
#     if comida > 500:
#         print("Llenar el plato")
#         comida -= 500
#         print(f"Queda {comida} de comida")
#         time.sleep(2)
#     else:
#         print("No queda comida")
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# total = 0

# while True:
#     opcion = int(input('''
#                        Seleccione una comida
#                        1.-Pikachu Roll $4500
#                        2.-Otaku Roll $5000
#                        3.-Pulpo Venenoso Roll $5200
#                        4.-Aguila Electrica Roll $4800
#                        5.-Pagar y salir
#                        '''))
#     match opcion:
#         case 1:
#             total += 4500
#         case 2: 
#             total += 5000
#         case 3:
#             total += 5200
#         case 4:
#             total += 4800
#         case 5:
#             print("Tiene codigo de descuento? (1.-Si / 2.-No) ")
#             descuento=int(input())
#             if descuento == 1:
#                 while True:
#                     cod = input("Ingresa tu codigo de descuento: ")
#                     if cod == "soyotaku":
#                         desc10 = total*0.1
#                         total = total - desc10
#                         print(f"El descuento es de {desc10}")
#                         break
#                     else:
#                         print("Codigo caducado o no valido")
#                         nu = input("Desea intentar nuevamente? 1.-Si / 2.-No")
#                         if nu!= "1":
#                             break
#             print(f"El total es ${total}")
#             break
#         case _:
#             print("Opcion invalida")
#     print(f"El total a pagar es de {total}")
    
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

menu = """
Menu principal
1.- Pago tarjeta de credito
2.- Simulacion de compras
3.-Salir
"""
total = 0
deuda = 100000

while True:
    print(menu)
    try:
        opcion =int(input("Selecione una opcion: "))
        
        match opcion:
            case 1:
                print("---Pago de tarjeta de credito---")
                try:
                    montoPago = int(input("Ingrese el monto a pagar: "))
                    if montoPago <= 0:
                        print("Error el monto debe ser mayor a 0")
                    elif montoPago > deuda:
                        print("Error el monto no puede ser mayor a la deuda")
                    else:
                        deuda -= montoPago
                        print(f"Pago realizado, su deuda es de {deuda}")
                except ValueError:
                    print("Error, debe ingresar un número")
            case 2:
                print("---Simulacion de compras---")
                compra = [] 
                
                while True:
                    try:
                        monto = int(input("Ingres el monto de la compra o 0 para salir: "))
                        
                        if monto < 0:
                            print("Error el monto no puede ser negativo")
                        elif monto == 0:
                            break
                        else:
                            total += monto
                    except ValueError:
                        print("Error, debe ingresar un número")
            case 3:
                print("Saliendo del programa")
                break
            case _:
                print("Error, opcion no valida")
    except ValueError:
        print("Error, debe ingresar un número")
        
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # crear menus con categirias 

# cantArt=0
# total=0

# while True:
#     while True:
#         try:
#             print("""
#                 Seleccione una opcion
#                 1.-Teclados
#                 2.-Monitores 
#                 3.-Audifonos
#                 4.-Pagar
#                 5.-Salir
#                 """)
#             op = int(input())
#             break
#         except Exception:
#             print("Ingrese solo numeros enteros")
#     match op:
#         case 1:
#             while True:
#                 print("""
#                       Selecionar una opcion
#                       1.-Teclado de manco $20.000
#                       2.-Teclado gamer $40.000
#                       3.-Teclado Normal y aburrido $8.000
#                       4.-Volver al menu principal
#                       """)
#                 op=int(input())
#                 match op:
#                     case 1:
#                         total+=20000
#                         cantArt+=1
#                     case 2:
#                         total+=40000
#                         cantArt+=1
#                     case 3:
#                         total+=8000
#                     case 4:
#                         break
#                     case _:
#                         print("Opcion invalida")
#                 print(f"Articulo Agregado al carro, lleva {cantArt} en total")
#                 print(f"El total parcial es ${total}")
#         case 2:
#             while True:
#                 print("""
#                       Seleccione una opcion
#                     1.-Monitor Xth67cv $200.000
#                     2.-Monito3 Exa67jk92 $140.000
#                     3.-Monitor VGA $28.000
#                     4.-Volver al menu principal
#                       """)
#                 op=int(input())
#                 match op:
#                     case 1:
#                         total+=200000
#                         cantArt+=1
#                     case 2:
#                         total+=140000
#                         cantArt+=1
#                     case 3:
#                         total+=28000
#                     case 4:
#                         break
#                     case _:
#                         print("Opcion invalida")
#                 print(f"Articulo Agregado al carro, lleva {cantArt} en total")
#                 print(f"El total parcial es ${total}")
#         case 3:
#             while True:
#                 print("""
#                       Seleccione una opcion
#                     1.-Audifonos JBL 720 $60.000
#                     2.-Audifonos gamer $140.000
#                     3.-Audifonos normal y aburrido $10.000
#                     4.-Volver al menu principal
#                       """)
#                 op=int(input())
#                 match op:
#                     case 1:
#                         total+=200000
#                         cantArt+=1
#                     case 2:
#                         total+=140000
#                         cantArt+=1
#                     case 3:
#                         total+=28000
#                     case 4:
#                         break
#                     case _:
#                         print("Opcion invalida")
#                 print(f"Articulo Agregado al carro, lleva {cantArt} en total")
#                 print(f"El total parcial es ${total}")
#         case 4:
#             print("-----------------------------------")
#             print(f"El total de articulos es {cantArt}")
#             print(f"El total neto es {total}")
#             print(f"El total + IVA es {total*1.19} ")
#             print("-----------------------------------")
#         case 5:
#             print("Saliendo...")
#             break
#         case _:
#             print("Opcion Invalida")
        
            
                        
    