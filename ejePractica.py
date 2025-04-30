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

