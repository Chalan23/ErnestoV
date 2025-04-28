# Explicacion y uso del while

# # intentos infinitos
# clave = 123
# intentos = 0
# password = int(input("Introduce la clave: "))
# while clave != password:
#     print("Clave incorrecta, vuelve a intentarlo")
#     intentos = intentos + 1
#     password = int(input("Introduce la clave: "))

# if intentos <=3:
#     print("Has superado el maximo de intentos")

#     print("Clave correcta! Binevenido")


# #clave 3 intentos maximos 
 
# clave = 123
# intentos = 0
# max_intentos = 3

# while intentos < max_intentos:
#     password = int(input("Introduce la clave: "))
#     if password == clave:
#         print("¡Clave correcta! Bienvenido")
#         break
#     else:
#         print("Clave incorrecta, vuelve a intentarlo")
#         intentos += 1

# if intentos == max_intentos:
#     print("Has superado el máximo de intentos")




# #pida al usuario el limite inferior y superior de rango
# # despues genere un numero al azardentro de un rango
# # el segundo numero no debe ser menor que el primero 
# # pero debe darle la oportunidad al usuario de ingresar otro 

# import random

# print("Ingrese un numero")
# n1=int(input("Ingrese el primer numero: "))
# n2=int(input("Ingrese el segundo numero: "))

# numRan=random.randint(n1,n2)
# print(numRan)

# while n1 <= n2:
#     print("El numero debe ser mayor al anterior")
#     n2=int(input("ingrese otro numero mayor al anterior"))
    
# numRan=random.randint(n1,n2)

# print(numRan)



# # El usuario debe adivinar el numero
# import random

# numAleatorio=random.randint(1,50)

# print("Adivina el numero del 1 al 50")
# intentos = 5
# num=int(input())


# while numAleatorio != num:
#     intentos -= 1
#     if numAleatorio > num:
#         break
#     if intentos == 0:
#         print("El numero es menor ")
#     else:
#         print("El numero es mayor")
#     print(f"te quedan {intentos} intentos")
#     num=int(input())

# if intentos == 0:
#     print("perdiste")
# else: 
#     print("Sos un genio adivinaste el numero")
        


# # STREET FIGTHER
# # Designe 2 peleadores solicitando sus nombres
# # cada peleador tiene 50 hp
# # tiene que mostrar la barra de ejergia, las peleas son por turnos
# # cada peleador ataca entre 3 y 15
# # existe posibilidad de ataque critico del 20% sera ataque doble atk*2
# # gana el que quita todo el hp al otro

# import random
# import time

# print("Ingrese el nombre de los peleadores")
# p1 = input("ingrese el nombre del peleados 1: ")
# p2 = input("Ingrese el nombre del peleados 2:")

# hp1 = 50
# hp2 = 50
# turno = random.randint(1,2)

# while hp1 > 0 and hp2 > 0:
#     if turno % 2==0:
#         print(f"turno de {p1}")
#         atk = random.randint(3,15)
#         critical = random.randint(1,5)
#         if critical == 3: 
#             atk*2
#             print("Ataque critico")
#         hp2 -= atk 
#         time.sleep(1)
#         print(f"Vida de {p2}")
#         print("/"*hp2)

#     else:
#         print(f"turno de {p2}")
#         atk = random.randint(3,15)
#         critical = random.randint(1,5)
#         if critical == 3: 
#             atk*2
#             print("Ataque critico")
#         hp1 -= atk 
#         time.sleep(1)
#         print(f"Vida de {p1}")
#         print("/"*hp1)

#     turno += 1
# if hp1 > hp2:
#     print(f"Ganador {p1}")
# else:
#     print(f"Ganador {p2}")


# # Explicacion del while
# while True:
#     print ('''
#         1.-
#         2.-
#         3.-Salir 
#            ''')
#     op= int(input("Ingrese una opcion:"))
#     if op == 1:
#         print("Opcion 1")
#     elif op == 2:
#         print("Opcion 2")
#     elif op == 3:
#         print("Opcion salir")
#         break
#     else:
#         print("Opcion incorrecta")


#crear un cajero automatico 
# tener en cuenta cajas de billetes 5000, 10000 y 20000 30 billetes de cada uno 
# cada caja tiene 30 billetes. verificar si el monto solicitado 
# esta disponible en el cajero  
# verificar si el monto solicitado es posible por el multiplo de los billetes disponibles
# al terminar cada transaccion debe mostrar saldo disponible
# debe haber tres usuarios cada uno con saldo correspondiente 
#debe iniciar sesion y segun la clave asociar el saldo disponible 