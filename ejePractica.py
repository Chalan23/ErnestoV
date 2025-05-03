# ejercicios vistos en pseint pasados a python para practicar
# -------------------------------------------------------------------------------------------------
# # 1.- ingrese la edad y calcule cuantos dias a vivido
# edad = int(input("Cuantos años tienes? "))

# diasVida = edad * 365

# print ("Su edad en dias es ", diasVida)

# -------------------------------------------------------------------------------------------------

# # 2.- pedir un numero y evaluar si es negativo y positivo 
# num = int(input("Ingresa un numero "))

# if num > 0:
#     print ("El numero es positivo")

# elif num < 0:
#     print("El numero es negativo") 

# else:
#     print("El numero es 0")

# -------------------------------------------------------------------------------------------------

# # 3.- pedir un numero y evaluar si es par o impar 
# num = int(input("Ingrese un numero "))

# if num % 2 == 0:
#     print("Su numero es par")

# else: 
#    print("Su nuemro es impar")

# -------------------------------------------------------------------------------------------------

# # 4.- pedir ingresar 3 numeros y calcular el promedio

# nota1 = float(input("Ingrese su nota 1: "))
# nota2 = float(input("Ingrese su nota 2: "))
# nota3 = float(input("Ingrese su nota 3: "))

# promedio = (nota1 + nota2 + nota3) / 3

# print ("Su promedio es: ", promedio)

# -------------------------------------------------------------------------------------------------

# # 5.- pedir el nombre y repetirlo 5 veces.
# nombre = str(input("Cual es tu nombre? "))

# for i in range(5):
#     print("Hola", nombre, "que tengas un buen dia")

# -------------------------------------------------------------------------------------------------

# # 6.- tabla de multiplicar 
# num=int(input("Ingrese un numero para su tabla de multiplicar: "))

# for i in range(1,11): 
#     print(num, "X" , i, "=" , i*num)

# -------------------------------------------------------------------------------------------------

# # 7.- pedir al usuario que ingrese dos numeros y moestrar el resultado
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))

# total = num1 + num2

# print("El resultado de la suma es: ", total)

# -------------------------------------------------------------------------------------------------

# 8.- pida al usuario ingresar un numero 7 veces y moestra la suma de todos los numeros
# suma = 0
# for i in range(7):
#     num = int(input("Ingrese un numero: "))
#     suma = suma + num
# print("La suma total de los numeros es: ", suma)

# -------------------------------------------------------------------------------------------------

# # 9.- calculadora basica
# num1 = float(input("Ingresa el primer numero: "))
# num2 = float(input("Ingrersa el segundo numero: "))

# print("Operaciones que puedes realizar")
# print("1.-Suma (+)")
# print("2.-Resta (-)")
# print("3.-Multiplicacion(*)")
# print("4.-Divicion (/)")


# op = input("Elije una operacion: ")

# if op == "+":
#     res = num1 + num2

# elif op == "-":
#     res = num1 - num2

# elif op == "*":
#     res = num1 * num2

# elif op == "/":
#     res = num1 / num2

# else:
#     print("Error ingrese una operacion valida")

# print("El resultado de su operacion matematica es: ", res)

# -------------------------------------------------------------------------------------------------

# # 10.- pida al usuario ingresar su clave de ingreso.
# clave = int(input("Ingrese su clave: "))

# contraseña = 1234

# if  clave == contraseña:
#     print("Bienvenido al sistema")

# else:
#     print("Error, no puede ingresar.")

# -------------------------------------------------------------------------------------------------

# # 11.- Contraseña 3 intentos maximos 
# claveReal = 1234
# inten = 0
# intenMax = 3

# while inten < intenMax:
#     claveUsuario = int(input("Ingrese su contraseña: "))
#     if claveUsuario == claveReal:
#         print("Bienvenido al sistema!")
#         break
#     else: 
#         inten = inten + 1
#         print(f"Clave Invalida, le quedan {inten} de un total de {intenMax}")
 
# if inten == intenMax:
#     print("Sistema bloqueado")

# -------------------------------------------------------------------------------------------------

# # 12.- Nombre y edad de una persona
# nombre = "Ernesto"
# edad = 32

# print(f"Hola {nombre} tu edad es {edad}")

# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))

# print(f"Hola {nombre} tu edad es {edad} años, gracias por tu información")

# -------------------------------------------------------------------------------------------------

# # 13.- promedio calcular 3 notas
# nota1 = float(input("Ingrese la primera nota: "))
# nota2 = float(input("Ingrese la segunda nota: "))
# nota3 = float(input("Ingrese la tercera nota: "))

# promedio = (nota1+nota2+nota3)/3

# print(f"Su promedio es de {promedio} ")

# -------------------------------------------------------------------------------------------------

# # 14.- promedio 3 notas y verificar si paso o no de curso 

# nota1 = float(input("Ingresa tu primera nota: "))
# nota2 = float(input("Ingresa tu segunda nota: "))
# nota3 = float(input("Ingresa tu primera nota: "))

# promedio = (nota1+nota2+nota3)/3

# print(f"Su promedio es: {promedio}")

# if promedio >= 4:
#     print("Pasa de curso")

# else:
#     print("No pasa de curso")

# -------------------------------------------------------------------------------------------------

# # N°1 ejercicios para la prueba (Cine)
# # pida al usuario selecionar categoria de sala del cine 
# # selecione una categoria de pelicula 
# # seleccionar pelicula 
# # preguntar si quiere llevar promocion de cabritas 
# # preguntar cuantas entradas desea llevar 

# print("Bienvenido al cine")
# print("Selecciona una categoria de sala de cine")
# print("1.-Sala Normal")
# print("2.-Sala 3D")
# print("3.-Sala Pro")

# sala = int(input("En que sala te gustaria disfrutar tu pelicula: "))

# print("Seleciona el numero la categoria de la pelicula que quieres ver")
# print("1.Terror")
# print("2.-Accion")
# print("3.-Comedia")

# catPelicula = int(input("Que genero de peliculas desea ver hoy: "))
# pelicula = ""

# if catPelicula == 1:
#     print("Peliculas de terror")
#     print("1.-It el payaso")
#     print("2.-La monja")
#     print("3.-El diablo en la tierra")
#     peli = int(input("Selecione una pelicula: "))
#     if peli == 1:
#         pelicula = "It el payaso"
#     elif peli == 2:
#         pelicula = "La monja"
#     elif peli == 3:
#         pelicula = "El diablo en la tierra"
#     else:
#         print("Opcion Invalida")
 
# elif catPelicula == 2:
#     print("Peliculas de accion")
#     print("1.-Rapidos y furiosos 23")
#     print("2.-El ultimo soldado")
#     print("3.-La pareja explosiva")
#     peli = int(input("Selecione una pelicula: "))
#     if peli == 1:
#         pelicula = "Rapidos y furiosos 23"
#     elif peli == 2:
#         pelicula = "El ultimo soldado"
#     elif peli == 3:
#         pelicula = "La pareja explosiva"
#     else:
#         print("Opcion Invalida") 
        
# elif catPelicula == 3:
#     print("Peliculas de comedia")
#     print("1.-Los corredores de la risa")
#     print("2.-El payaso fome")
#     print("3.-El mimo parlanchin")
#     peli = int(input("Selecione una pelicula: "))
#     if peli == 1:
#         pelicula = "Los corredores de la risa"
#     elif peli == 2:
#         pelicula = "El payaso fome"
#     elif peli == 3:
#         pelicula = "El mimo parlanchin"
#     else:
#         print("Opcion Invalida")    

# else:
#         print("Opcion invalida")

# promo = input("Deseas llevar cabritas Si/No: ").lower()

# entradas = int(input("Cuantas entradas deseas llevar (cantidad de entradas en numero): "))

# print("#---------------------------------------#")

# print(f"Pelicula seleccionada: {pelicula}")
# print(f"Llevas tu promo: {promo}")
# print(f"Total entradas: {entradas}")

# -------------------------------------------------------------------------------------------------

# # N°2 ejercicios para la prueba (Concierto)
# # el usuario cuenta con descuentos por comprar su entrada con tarjetas 
# # banco bci 30%, banco de chile 20%, banco falabella 25%
# # cancha $100.000, galeria $150.000, vip 250.000 (Recargo por entrada $20.000) 
# # preguntar cuantas entradas desea comprar
# # y seleccionar con que banco va a pagar


# print("Bienvenido al sistema de compra de entradas")
# print("!-----------------------------------------!")
# entradas = int(input("Cuantas entradas deseas comprar: "))

# print("PROMOCION DESCUENTO PAGO CON TARJETA")
# print("1.-BCI 30% - 2.-Banco de Chile 20% - 3.-Banco Falabella 25%")
# banco = int(input("Elije el banco con el que pagas: "))

# print("Elige tu sector de preferencia")
# print("1.-Cancha $100.000")
# print("2.-Galeria $150.000")
# print("3.-Vip $250.000")
# print("Recuerda el recargo por servicio es de $20.000")

# sector = int(input("En que sector quieres estar (1, 2 o 3): "))

# if sector == 1:
#     precioSector = 100000 
# elif sector== 2:
#     precioSector = 150000 
# elif sector == 3:
#     precioSector = 250000
# else:
#     print("Opcion invalida")
#     exit()
    
# precioEntradas = precioSector +20000
# precioTotal = entradas * precioEntradas


# if banco == 1:
#     desc = precioTotal * 0.3
# elif banco == 2:
#     desc = precioTotal * 0.2
# elif banco == 3:
#     desc = precioTotal * 0.25
# else:
#     print("opcion invalida")
#     exit()
    
# precioFinal = precioTotal - desc    

# print("!-----------------------------------------!")
# print(f"Usted lleva {entradas} entradas")
# print(f"El descuento total es de ${desc}")
# print(f"El total a pagar es de ${precioFinal}")
# print("!-----------------------------------------!")


