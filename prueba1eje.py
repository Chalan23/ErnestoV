# # STREET FIGTHER #

# # Designe 2 peleadores solicitando sus nombres
# # cada peleador tiene 50 HP, debe mostrar la 
# # barra de energia. Las peleas son por turnos #print("[]"*20)
# # cada turno el peleador ataca entre 3 y 15
# # Existe posibilidad de ataque critico del 20% sera atk*2
# # gana el que le quita todo el HP al rival

# import random
# import time

# print("Ingrese nombre de los peleadores")
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
#             atk *= 2
#             print("Ataque Critico!")
#         hp2 -= atk
#         hp2 = max(0, hp2)
#         print(f"{p1} hizo {atk} de daño a {p2}")
#         print(f"vida de {p2}: {'<3' * hp2}")
        
#     else:
#         print(f"turno de {p2}")
#         atk = random.randint(3,15)
#         critico = random.randint(1,5)
#         if critico == 3:
#             atk *= 2
#             print("Ataque Critico!")
#         hp1 -= atk
#         hp1 = max(0, hp1)
#         print(f"{p2} hizo {atk} de daño a {p1}")
#         print(f"vida de {p1}: {'<3' * hp1}")
        
#     turno += 1
#     time.sleep(1)

# print("La pelea ha terminado")
# if hp1 > hp2:
#     print(f"Ha ganado {p1}")
# else:
#     print(f"Ha ganado {p2}")
 

# ---------------------------------------------------------------# 


# # VOTATOON
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quien votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate

# numVotantes = int(input("Cuantas personas votan? "))

# lala = 0
# lele = 0

# print("Ingrese 1 si votas por lala o 2 si votas por lele")

# for i in range(numVotantes):
#     voto = int(input(f"Votante {i+1}, ingrese su voto: "))

#     if voto == 1:
#         lala += 1
#     elif voto == 2:
#         lele += 1
#     else:
#         print("voto nulo")

# print("\nResultados:")
# print(f"Votos para lala: {lala}")
# print(f"Votos para lele: {lele}")

# if lala > lele:
#     print("Ganó lala")
# elif lele > lala:
#     print("Ganó lele")
# else:
#     print("Empate")

# ---------------------------------------------------------------# 

# Crear un cajero automatico
# Tener en cuenta cajas de billetes de 5000 , 10000 y 20000
# Cada caja tine 30 billetes. Verificar si el monto solicitado
# Esta disponible en el cajero.Verificar si el monto solicidado
# es posible por el multiplo de los billetes disponibles
# Al terminar cada transaccion, debe mostrar saldo Disponible
# Debe haber 3 usuarios cada uno son su saldo correspondiente
# Usar clave secreta para iniciar y segun la clave 
# asociar el saldo disponible

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

# descuento = 0
# print("La Florida 20%, La Pintana 30%, Puente Alto 25%, San Jaoquin 15%")
# comuna = input("En que comuna vives? ").lower()
# personas = int(input("Cuantas personas viven en tu casa? "))

# if comuna == "la florida":
#     descuento = 20
# elif comuna == "la pintana":
#     descuento = 30
# elif comuna ==  "puente alto":
#     descuento = 25
# else:
#     descuento = 15
   
# if personas == 1:
#     descuento += 2
# elif personas >= 2 and personas <= 4:
#     descuento += 3
# else:
#     descuento += 4

# totalDesc = 200000 * (descuento / 100)

# print(f"Su descuento total es {totalDesc}")
# print(f"El total a pagar es de {200000 - totalDesc}")



# ---------------------------------------------------------------# 

# Clasificar segun categoria y precio
# Cat 1 +200, cat 2 +400, cat 3 +600
# Decuento Precios : 1000 y menos;3%, entre 1001 y 5000 
# ;5% , 5001 y mas 6%
# Poner listado de 3 productos por categoria, las cat son 1 ,2 y 3
# Agregar los impuestos al ´precio , segun la cat y luego 
# aplicar descuento al total de la boleta segun el monto
'''
Ej:
Producto 1, cat 2, 1500 + 400
Producto 2 cat 1, 8000 + 200
EL total es 10100 * - 6%
EL total a pagar es: 9494
'''



# ---------------------------------------------------------------# 

# # calcular el puntaje de credito 
# # debe calcular que tanto credito tiene una persona 
# # en cierta entidad financiera, debe considerar
# # cantidad de ingresos, nivel educacional y nacionalidad
# # cantidad de ingresos
# # 500.000 a 1.000.000 : 300.000
# # 1.000.000 a 1.500.000 : 650.000
# # 1.500.001 o mas : 1.000.000
# # nivel educacional
# # basico: 1x, medio: x1.3, superior: x1.5


# credito = 0
# nacionalidad = int(input("Ingrese nacionalidad (1 chileno, 2 extranjero): "))
# sueldo = int(input("Ingrese sueldo mensual: "))
# educacion = int(input("Ingrese educación (1 básico, 2 medio, 3 superior): "))

# if nacionalidad == 1:
#     credito = sueldo * 1.5
# elif nacionalidad == 2:
#     credito = sueldo * 1.3
# else:
#     credito = sueldo * 1.1


# if sueldo >= 500000 and sueldo <= 1000000:
#     credito += 300000
# elif sueldo > 1000000 and sueldo <= 1500000:
#     credito += 650000
# elif sueldo > 1500000:
#     credito += 1000000

# if educacion == 1:
#     credito *= 1
# elif educacion == 2:
#     credito *= 1.3
# elif educacion == 3:
#     credito *= 1.5
# else:
#     credito = 0

# print(f"El puntaje de crédito es {credito}")


# ---------------------------------------------------------------#


# # pida al usuario 2 digitos verificando que el segundo sea mayor 
# # genere un numero aleatorio entre esos digitos
# # e imprime la cantidad de veces el simbolo (alt+220)

# import random
# from random import randint

# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))



# while num1 > num2:
#     print("El numero 2 no puede ser menor que el numero 1")
#     num2=int(input("numero 2: "))
    
# num=random.randint(num1, num2)
# print("▄"*num)

# # for i in range(num):
# #     print("▄") 

# ---------------------------------------------------------------#

# # crear un programa que pida la cantidad de ramos 
# # luego pida el promedio por cada materia 
# # basado en su promedio final, aplique puntaje de beneficios
# # 4.5 y 5 : 300, 5.1 y 6 : 500, 6.1  y 7.: 800
# # agregar puntaje segun carrera 
# # tecnico: +60, ingeneria: +40, diplomado: +20
        
# mat=int(input("Ingrese la cant de materias: "))
# suma=0
# for i in range(mat):
#    notaramo=float(input(f"Ingrese la nota del ramo{i+1}: "))
#    suma+=notaramo
# prom=suma/mat
# print("Su nota final es ", round(prom,1))
# if prom>=4.5 and prom<=5.0:
#    puntaje=300
#    print( f"Su puntaje de beneficios es de {puntaje}")
# elif prom>=5.2 and prom<=6.0:
#     puntaje=500
#     print( f"Su puntaje de beneficios es de {puntaje}")
# elif prom>=6.1 and prom<=7.0:
#     puntaje=800
#     print( f"Su puntaje de beneficios es de {puntaje}")
# else:
#    print(" Es tan porro que no tiene beneficios")

# car=int(input('''
#             Ingrese su tipo de grado
#               1.- Tecnico
#               2.- Ingenieria
#               3.- Diplomado
#               '''))
# if car==1:
#    puntaje+=60
# elif car==2:
#    puntaje+=40
# elif car==3:
#    puntaje+=20
# else:
#    print("no es nuemro valido")

# print( " El puntaje de beneficios es ", puntaje)
    

# ---------------------------------------------------------------#

# # Escribe un programa que le pida al usuario un número entero y verifique si es positivo, negativo o cero. Usa if, elif y else.

# print("Verificador de numeros!")
# num = int(input("Ingresa un numero: "))

# if num >= 1:
#     print("El numero es positivo!")
# elif num == 0:
#     print("El numero es 0")
# else: 
#     print("El numero es negativo!")

# ---------------------------------------------------------------#

# crea un programa que simule un juego de adivinanzas. El programa debe generar un numero aleatorio entre 
# 1 y 10 usando random.randint. Luego, debe pedirle al usuario que adivine el número. El usuario tiene 3
# intentos. Si adivina correctamente, el programa debe felicitarlo. Si no lo adivina en 3 intentos, debe mostrar
# el número correcto. Usa import random y un bucle while.

# import random

# numSecreto = random.randint(1,10)
# intentos = 0
# maxIntentos = 3

# print("Juego de adivinar el numero")

# while intentos < maxIntentos:
#     num = int(input("Ingresa un numero (1,10): "))
    
#     if num == numSecreto:
#         print("Felicidades adivinaste el numero!!!")
#         break
#     else:
#         print("Intentalo de nuevo!")
#         intentos += 1

# if num != numSecreto:        
#     print(f"Perdiste!!!! El numero secreto era {numSecreto}")

# ---------------------------------------------------------------#

# # Un cine ofrece distintos tipos de entrada según la edad:
# # Si la persona tiene menos de 5 años, no puede ingresar.
# # Si tiene entre 5 y 12 años, paga entrada infantil: $2.000
# # Si tiene entre 13 y 64 años, paga entrada general: $4.000
# # Si tiene 65 años o más, paga entrada senior: $2.500
# # Escribe un programa que:
# # Pida al usuario su edad.
# # Imprima si puede entrar o no.
# # Si puede, muestre cuánto debe pagar.

# print("Bienvenido al cine")
# print("----------------------------------------------------------")
# print("Si eres menor de 5 años no puede ingresar")
# print("Si tienes entre 5 y 12 años. Valor entrada infantil $2.000")
# print("Si tiene entre 13 y 65 años. Valor entrada general $4.000 ")
# print("Si tiene 65 años o más. Valor entrada senior: $2.500")
# print("----------------------------------------------------------")

# edad = int(input("Que edad tienes?: "))
# if edad <= 5:
#     print("Lo sentimos no puedes ingresar")
# elif edad >= 6 and edad <= 12:
#     print("El valor de su entrada es de $2.000")
# elif edad >= 13 and edad <= 65:
#     print("El valor de su entrada es de $4.000")
# else:
#     print("El valor de su entrada es de $2.500")

# ---------------------------------------------------------------#

# # 🐉 BATALLA DE DRAGONES 🐉
# # Pide el nombre de dos dragones.❤️
# # Cada dragón tiene 80 puntos de vida (HP).
# # En cada turno, el dragón ataca al otro con una llamarada de entre 10 y 18 de daño (random.randint()).
# # Existe un 30% de probabilidad de llamarada crítica que hace el triple de daño.
# # El juego alterna turnos hasta que un dragón quede con 0 o menos HP.
# # Muestra en cada turno:
# # Quién atacó a quién
# # Si el ataque fue crítico
# # Cuánto daño se hizo
# # La barra de vida de ambos ("🔥" * (hp // 4)).

# import random
# import time

# hp1 = 80
# hp2 = 80
# turno = random.randint(1, 2)

# print("Bienvenido a la batalla de dragones!")
# print("---------------------------------------------")
# dragon1 = input("Como se llama Tu dragon? 🐉 ")
# dragon2 = input("Como se llama el dragon rival? 🐉 ")

# while hp1 > 0 and hp2 > 0:
#     if turno % 2 == 0:
#         print(f"turno de {dragon1}🐉")
#         atk = random.randint(10, 18)
#         critico = random.randint(1, 5) 
#         if critico == 3:
#             atk *= 3
#             print("🔥Ataque Critico🔥")
#         hp2 -= atk
#         hp2 = max (0, hp2)
#         print(f"El daño de {dragon1} fue de {atk} a {dragon2}")
#         print(f"vida de {dragon2}: {'🔥' * (hp2 // 4)}")
        
#     else:
#         print(f"turno de {dragon2}🐉")
#         atk = random.randint(10, 18)
#         critico = random.randint(1, 5) 
#         if critico == 3:
#             atk *= 3
#             print("🔥Ataque Critico🔥")
#         hp1 -= atk
#         hp1 = max (0, hp1)
#         print(f"El daño de {dragon2} fue de {atk} a {dragon1}")
#         print(f"vida de {dragon1}: {'🔥' * (hp1 // 4)}")
#         time.sleep(1)
        
# print("La pelea ha terminado")
# print("---------------------------------------------")
# if hp1 > hp2:
#     print(f"Ha ganado {dragon1}🐉")
# else:
#     print(f"Ha ganado {dragon2}🐉")

# ---------------------------------------------------------------#


# # 🥇 Ejercicio 1 (Nivel Básico)
# # Enunciado:
# # Crea un programa que solicite al usuario su edad y diga si puede votar o no. En Chile, se puede votar desde los 18 años.
# # Instrucciones:
# # Solicita la edad del usuario con input().
# # Convierte el dato a entero.
# # Usa una estructura if para determinar si puede o no votar.
# # Muestra un mensaje adecuado.

# print("Votaciones Presidenciales 2025")

# edad = int(input("Ingresa tu edad para validar si puede votar: "))

# if edad >= 18:
#     print("Felicidades tienes derecho a voto.")
# else:
#     print("Lo sentimos no tienes la edad suficiente para votar.")

# ---------------------------------------------------------------#

# # 🥈 Ejercicio 2 (Nivel Medio - Distinto a Street Fighter)
# # Enunciado: CARRERA DE CARACOLES 🐌🏁
# # Dos caracoles están compitiendo en una carrera. Cada uno avanza por turnos una cantidad aleatoria de pasos entre 1 y 6.
# # Gana el primer caracol que llegue o supere los 30 pasos.
# # Instrucciones:
# # Pide al usuario los nombres de los dos caracoles.
# # Cada caracol parte desde 0 pasos.
# # En cada turno, uno de los caracoles avanza una cantidad aleatoria entre 1 y 6.
# # Muestra visualmente el avance con "." por cada paso. Ej: print("." * pasos).
# # Alternan los turnos hasta que uno llegue a 30 o más pasos.
# # Al final, muestra quién ganó y con cuántos pasos.

# import random
# import time

# turno = random.randint(1, 2)
# caracol1 = input("Nombre del primer caracol: ")
# caracol2 = input("Nombre del segundo caracol: ")

# pasos1 = 0
# pasos2 = 0

# while pasos1 < 30 and pasos2 < 30: 
#     if turno % 2 == 0:
#         print(f"Turno de {caracol1}")
#         pasos = random.randint(1, 6)
#         pasos1 += pasos
#         pasos1 = min(30, pasos1)  
#         print(f"{caracol1} avanzó {pasos1} pasos")
#         print(f"Pasos de {caracol1}: {'.' * pasos}")

#     else:
#         print(f"Turno de {caracol2}")
#         pasos = random.randint(1, 6)
#         pasos2 += pasos
#         pasos2 = min(30, pasos2)  
#         print(f"{caracol2} avanzó {pasos2} pasos")
#         print(f"Pasos de {caracol2}: {'.' * pasos}")

#     turno += 1
#     time.sleep(1)

# if pasos1 >= 30:
#     print(f"Gano {caracol1}")
# else:
#     print(f"Gano {caracol2}")

# ---------------------------------------------------------------#

# # 🐉 BATALLA DE DRAGONES 🐉
# # Pide el nombre de dos dragones.❤️
# # Cada dragón tiene 80 puntos de vida (HP).
# # En cada turno, el dragón ataca al otro con una llamarada de entre 10 y 18 de daño (random.randint()).
# # Existe un 30% de probabilidad de llamarada crítica que hace el triple de daño.
# # El juego alterna turnos hasta que un dragón quede con 0 o menos HP.
# # Muestra en cada turno:
# # Quién atacó a quién
# # Si el ataque fue crítico
# # Cuánto daño se hizo
# # La barra de vida de ambos ("🔥" * (hp // 4)).        

import random 
import time 

turno = random.randint(1,2)

hp1 = 80
hp2 = 80
print("Bienvenido a la pelea de dragones")
dragon1 = input("Nombre de tu dragon: ")
dragon2 = input("Nombre del dragon rival: ")

while hp1 > 0 and hp2 > 0:
    if turno % 2 == 0:
        print(f"Comneza {dragon1}")
        atk = random.randint(10,18)
        critico = random.randint(1,5)
        if critico == 3:
            atk *3
            print("Critico! Llamaradaaaa!!")
        hp2 -= atk
        hp2 = max(0, hp2)
        print(f"{dragon1} hizo {atk} a {dragon2}")
        print(f"La vida de {dragon2}: {'❤️'*hp2}")
    else:
        print(f"Comneza {dragon2}")
        atk = random.randint(10,18)
        critico = random.randint(1,5)
        if critico == 3:
            atk *3
            print("Critico! Llamaradaaaa!!")
        hp1 -= atk
        hp1 = max(0, hp1)
        print(f"{dragon2} hizo {atk} a {dragon1}")
        print(f"La vida de {dragon1}: {'❤️'*hp1}")
    
    turno += 1
    time.sleep(1)
    
    if hp1 > hp2:
        print(f"Gano {dragon1}")
    else:
        print(f"Gano {dragon2}")
        
        


