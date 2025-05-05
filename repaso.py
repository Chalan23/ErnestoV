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
#         print("Python es genial")
#     elif opcion == "4":
#         print("Saliendo del programa...")
#     else:
#         print("Opción no válida. Intenta de nuevo.")

# ---------------------------------------------------------------# 
# for
# ---------------------------------------------------------------# 

# # tablas de multiplicar
# num = int(input("Ingrese un numero a multiplicar: "))

# for i in range(1,11):
#     print(num, "X" , i, "=" , i*num)

# ---------------------------------------------------------------# 

# # STREET FIGTHER #

# # Designe 2 peleadores solicitando sus nombres
# # cada peleador tiene 50 HP, debe mostrar la 
# # barra de energia. Las peleas son por turnos #print("[]"*20)
# # cada turno el peleador ataca entre 3 y 15
# # Existe posibilidad de ataque critico del 20% sera atk*2
# # gana el que le quita todo el HP al rival

# import random
# import time

# print("Quienes son los peleadores")
# p1 = input("Ingresa el nombre del primer peleador: ")
# p2 = input("Ingresa el nombre del segundo peleador: ")
# hp1 = 50
# hp2 = 50

# turno = random.randint(1,2)

# while hp1 > 0 and hp2 > 0:
#     if turno % 2 == 0:
#         print(f"turno de {p1}")
#         atk = random.randint(3,15)
#         critico = random.randint(1,5)
#         if critico == 3:
#             atk *=2
#             print("Ataque Critico!")
#         hp2 -= atk
#         hp2 = max(0, hp2)
#         print(f"El ataque de {p1} fue de {atk}")
#         print(f"Vida de {p2}: {'<3' * hp2}")
#     else:
#         print(f"turno de {p2}")
#         atk = random.randint(3,15)
#         critico = random.randint(1,5)
#         if critico == 3:
#             atk *=2
#             print("Ataque critico!")
#         hp1 -= atk
#         hp1 = max(0, hp1)
#         print(f"El ataque de {p2} fue de {atk}")
#         print(f"La vida de {p1}: {'<3' * hp2}")
        
#     turno += 1
#     time.sleep(1)
# if hp1 > hp2:
#     print(f"Ganador {p1}")
# else:
#     print(f"Ganador {p2}")

# ---------------------------------------------------------------# 

# # VOTATOON
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quien votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate
print("Elecciones presidenciales")
numVotantes = int(input("Cuantas personas votan? "))

guruGuru = 0
tutuTutu = 0

print("Por quien vas a votar?")
print("1.-guruGuru")
print("2.-tutuTutu")

for i in range(numVotantes):
    voto = int(input(f"El votante {i+1} por quien vota? "))
    if voto == 1:
        guruGuru += 1
    elif voto == 2:
        tutuTutu += 1
    else: 
        print("Voto nulo")

print("Conteo de votos")    
print(f"total votos para guruGuru es de: {guruGuru}")
print(f"total votos para tutoTutu es de: {tutuTutu}")

if guruGuru > tutuTutu:
    print(f"Gano tutuTutu")
elif tutuTutu > guruGuru:
    print(f"Gano guruGuru")
else: 
    print("Empate")
        
# ---------------------------------------------------------------# 

# Calcular el araccel a pagar segun grupo familiar y comuna en la que reside
# A continuacion , los descuentos por cumuna:
# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y en 
# la informacion dada, calcular su descuento
'''
ej :
Ingrese su comuna : La Florida
Ingrese su grupo familiar( numero entero usted incluido ) : 4
EL total del descuento es 23%
EL total a pagar es $154.000
'''

descuento = 0
print("La Florida 20%, La Pintana 30%, Puente Alto 25%, San Jaoquin 15%")
comuna = input("En que comuna vives? ").lower()
personas = int(input("Cuantas personas viven en tu casa? "))

if comuna == "la florida":
    descuento = 20
elif comuna == "la pintana":
    descuento = 30
elif comuna ==  "puente alto":
    descuento = 25
else:
    descuento = 15
   
if personas == 1:
    descuento += 2
elif personas >= 2 and personas <= 4:
    descuento += 3
else:
    descuento += 4

totalDesc = 200000 * (descuento / 100)

print(f"Su descuento total es {totalDesc}")
print(f"El total a pagar es de {200000 - totalDesc}")

# ---------------------------------------------------------------# 


# ---------------------------------------------------------------# 