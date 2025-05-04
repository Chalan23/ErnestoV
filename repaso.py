# repaso general

#Uso de while. for. if, elif y else.
# ---------------------------------------------------------------#  
# Uso de if, elif y else
# ---------------------------------------------------------------#  

# ej: import random 
# num1=random.randint(1,6)
# num2=random.randint(1,6)
# print(num1,num2)

# ---------------------------------------------------------------#  

# # mayor de 3 numeros
# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))
# num3 = int(input("Ingresa el tercer numero: "))

# if num1 > num2 and num1 0 num3:
#     print(f"El numero mayor es {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"El numero mayor es {num2}")
# else:
#     print(f"El numero mayor es {num3}")
  
# ---------------------------------------------------------------#  
    
# # clasificion por edad

# edad = int(input("Ingrese su edad: "))

# if edad <= 12:
#     print("Es un niño")
# elif edad >= 13 and edad <= 17:
#     print("Es un adolecente")
# else:
#     print("Es adulto")

# ---------------------------------------------------------------#  

# # par e impar

# num = int(input("Ingrese un numero: "))

# if num % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar") 

# ---------------------------------------------------------------#  

# # promedio de tres notas

# nota1 = float(input("Ingrese su primera nota "))
# nota2 = float(input("Ingrese su segunda nota "))
# nota3 = float(input("Ingrese su tercera nota "))

# promedio = round((nota1 + nota2 + nota3) / 3, 1)

# print(f"Su promedio de notas es: {promedio}")

# ---------------------------------------------------------------# 

# # promedio de notas y evaluar si pasa o no de curso

# nota1 = float(input("Ingresa tu primnera nota: "))
# nota2 = float(input("Ingresa tu segunda nota: "))
# nota3 = float(input("Ingresa tu tercera nota: "))

# promedio = round((nota1 + nota2 + nota3) / 3, 1)

# print(f"Su promedio es {promedio}")

# if promedio >= 4:
#     print("Pasa de curso")
# else:
#     print("Repite de curso")

# ---------------------------------------------------------------# 

# # menu con 3 opciones

# print("1.-Pan")
# print("2.-Jugo")
# print("3.-Cereal")
# print("4.-Salir")

# menu = int(input("Que seas llevar: "))

# if menu == 1: 
#     print("Llevas pan")
# elif menu == 2: 
#     print("Llevas Jugo")
# elif menu == 3: 
#     print("Llevas Cereal")
# elif menu == 4: 
#     print("Salir")
# else:
#     print("Opcion invalida")
  
# ---------------------------------------------------------------#
# Uso del while
# ---------------------------------------------------------------#  

# # adivina el numero secreto intentos ilimitados 

# import random

# numSecreto = random.randint(1, 10)
# num = int(input("Adivina el numero: "))

# while num != numSecreto: 
#     print("Numero incorrecto")
    
#     num = int(input("Intenta otra vez: "))

# print("Adivinaste")

# ---------------------------------------------------------------# 

# # # numero secreto maximo 3 intentos

# import random

# numSecreto = random.randint(1,10)
# intentiosMaximos = 3
# intentos = 0

# while intentos < intentiosMaximos:
#     num = int(input("Adivina el numero del 1 al 10: "))
#     intentos += 1
    
#     if num == numSecreto:
#         print("Adivinaste!")
#         break
#     else: 
#         print("Numero incorrecto!")
        
# if num != numSecreto:
#     print(f"Perdiste el numero secreto era {numSecreto}")

# ---------------------------------------------------------------# 

# # que un numero se repita 10 veces

# contador = 1
 
# while contador <= 10:
#     print(contador)
#     contador += 1

# ---------------------------------------------------------------# 

# # clave con 3 intentos maximos.

# password = 1234
# intentosMax = 3
# intentos = 0

# while intentos < intentosMax:
#     clave = int(input("Ingresa tu contraseña "))
#     if clave == password:
#         print("Clave correcta, Bienvenido al sistema")
#         break
#     else: 
#         print("Clave incorrecta")
#         intentos += 1

# if intentos == intentosMax:
#     print("Intentos maximos superados")
   
# ---------------------------------------------------------------# 

# # suma total de numeros hasta que usuario ingrese 0

# suma = 0
# num = int(input("Ingresa un numero o (0 para terminar): "))

# while num != 0:
#     suma += num
#     num = int(input("Ingresa un numero o (0 para terminar): "))

# print(f"La suma total es: {suma}")

# ---------------------------------------------------------------# 

# un menu que se repita hasta que el usuario quiera salir

# opcion = ""

# while opcion != "4":
#     print("\n--- MENÚ ---")
#     print("1. Saludar")
#     print("2. Sumar dos números")
#     print("3. Mostrar una frase")
#     print("4. Salir")
    
#     opcion = input("Elige una opción: ")

#     if opcion == "1":
#         print("¡Hola!")
#     elif opcion == "2":
#         a = int(input("Ingresa el primer número: "))
#         b = int(input("Ingresa el segundo número: "))
#         print(f"La suma es: {a + b}")
#     elif opcion == "3":
#         print("Python es genial 😎")
#     elif opcion == "4":
#         print("Saliendo del programa...")
#     else:
#         print("Opción no válida. Intenta de nuevo.")

# ---------------------------------------------------------------# 
# for
# ---------------------------------------------------------------# 

# tablas de multiplicar
num = int(input("Ingrese un numero a multiplicar: "))

for i in range(1,11):
    print(num, "X" , i, "=" , i*num)
