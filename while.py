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

# # --------------------------------------------------------------------------------------------------

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

# # --------------------------------------------------------------------------------------------------

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

# # --------------------------------------------------------------------------------------------------

# # El usuario debe adivinar el numero
# import random

# numram=random.randint(1,50)

# print("Adivine el numero entre 1 y 50")
# intentos=5
# num=int(input())

# while numram!=num:
#     intentos-=1
#     if intentos==0:
#         break
#     if num>numram:
#         print("El numero a adivinar es menor")
#     else:
#         print("El numero a adivinar es mayor")
#     print(f"te quedan {intentos} intentos")
#     num=int(input())

# if intentos==0:
#     print("Perdiste")
# else:
#     print("SOS UN GENIO, ADIVINASTE EL NUMERO")
        
# # --------------------------------------------------------------------------------------------------

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
# p2 = input("Ingrese el nombre del peleados 2: ")

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

# # --------------------------------------------------------------------------------------------------

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

# # --------------------------------------------------------------------------------------------------

# #crear un cajero automatico 
# # tener en cuenta cajas de billetes 5.000 (150.000), 10000(300.000) y 20000(600.000) 30 billetes de cada uno  total dinero 1.050.000
# # cada caja tiene 30 billetes. 
# # verificar si el monto solicitado esta disponible en el cajero  
# # verificar si el monto solicitado es posible por el multiplo de los billetes disponibles
# # al terminar cada transaccion debe mostrar saldo disponible
# # debe haber tres usuarios cada uno con saldo correspondiente 
# #debe iniciar sesion y segun la clave asociar el saldo disponible 

# cajero = {20000: 30, 10000: 30, 5000: 30}
# saldo = 1050000
# usuarios = {
#     "usuario1": {"clave": 1111, "saldo": 200000},
#     "usuario2": {"clave": 2222, "saldo": 300000},
#     "usuario3": {"clave": 3333, "saldo": 250000}
# }

# def total_cajero():
#     return sum(billete * cantidad for billete, cantidad in cajero.items())

# def mostrar_saldo():
#     print("==ESTADO DEL CAJERO==")
#     print(f"Sado cajero: {total_cajero()}")
#     for billete, cantidad in cajero.items():
#         print(f"Billetes de {billete}: {cantidad}")
#     print("=======================")


# user = input("Ingrese su nombre de usuario: ")
# if user in usuarios:
#     clave = int(input("Ingrese su clave: "))
#     if usuarios[user]["clave"] == clave:
#         print(f"Bienvenido {user}, su saldo es: {usuarios[user]['saldo']}")
#         while True:
#             mostrar_saldo()
#             monto = int(input("Ingrese el monto a retirar (o 0 para salir): "))
#             if monto == 0:
#                 break
#             if monto > total_cajero():
#                 print("Monto solicitado no disponible en el cajero.")
#                 continue
#             if monto % 5000 != 0:
#                 print("El monto solicitado no es múltiplo de 5000.")
#                 continue
#             billetes_necesarios = {}
#             for billete in sorted(cajero.keys(), reverse=True):
#                 cantidad_billetes = min(monto // billete, cajero[billete])
#                 if cantidad_billetes > 0:
#                     billetes_necesarios[billete] = cantidad_billetes
#                     monto -= billete * cantidad_billetes
#                     cajero[billete] -= cantidad_billetes

#             if monto > 0:
#                 print("No hay suficientes billetes para completar la transacción.")
#                 for billete, cantidad in billetes_necesarios.items():
#                     cajero[billete] += cantidad
#             else:
#                 usuarios[user]["saldo"] -= sum(billete * cantidad for billete, cantidad in billetes_necesarios.items())
#                 print(f"Retiraste: {sum(billete * cantidad for billete, cantidad in billetes_necesarios.items())}")
#     else:
#         print("Clave incorrecta.")

# --------------------------------------------------------------------------------------------------

# # repaso
# intentos=3

# while intentos > 0:
#     intentos-=1 #(intentos = intentos -1) se puede poner de las dos formas
    
#     color = input("Ingrese el color ")

#     if color.lower()!="negro":
#         print("El color no es el requerido")
#     else:
#         print("Este es el color requerido")
#         break

# --------------------------------------------------------------------------------------------------

# # La Florida 20%, La Pintana 30%, Puente ALto 25%, San Joaquin 15%.
# # Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas =>4%
# # Preguntar al usuario en que comuna vive
# # Pregunta al usuario con cuantas personas vive 
# # El arancel actual es de 200.000 por semestre
# # Basado en las respuestas del usuario y en
# # La informacio dada, calcular se descuento.


# print("Selecciones la comuna donde usted vive")
# print('''
#     La Florida 
#     La Pintana 
#     Puente lto 
#     San Joaquin  
# ''')
# comuna = input("En que comuna vive: ")
# familia = int(input("cuantas personas viven es su casa incluyendolo a usted: "))

# if comuna == "la florida":
#     descuento = 20
# elif comuna == "la pintana":
#     descuento = 30
# elif comuna == "puente alto":
#     descuento = 25
# elif comuna == "san joaquin":
#     descuento = 15
# else:
#     print("Ingrese una opcion correcta ")

# if familia == 1:
#     descuento += 2
# elif familia >=2 and familia <= 4:
#     descuento += 3
# else:
#     descuento += 4

# descTotal = 200000 * (descuento / 100)
# print(f"El descuento total es de: {descTotal}")
# print(f"El arancel a pagar es de: {200000 - descTotal}")

# --------------------------------------------------------------------------------------------------

# clasficar segun categoria y precio
# cat 1 +200, cat 2 +400, cat 3 +600
# precios : 1000 y menos ; 3%, entre 1001 y 5000 ; 5%, 5001 y mas 6%
# poner listado de 3 productos por categoria, las cat son 1, 2 y 3
# agregar impuestos al precio, segun la cat y luego
# aplicar descuento al total de la boleta segun el monto

# Ej:
# producto 1, cat 2, 1500 + 400
# producto 2, cat 1, 8000 + 200
# El total es 10100 * -6%
# El total a pagar es 9494
total=0
print('''
    Seleccione una categoria
      1.-Zapatillas
      2.-Polera
      3.-Pelotas
''')
cat=int(input())
if cat==1:
    print('''
        1.-Zapatilla running 2000
        2.-Zapatilla futbolito 1500
        3.-Zapatilla padel 60
''')
    op=int(input())
    if op==1:
        total+=2000+400
    elif op==2:
        total+=1500+400
    elif op==3:
        total+=20+400
    else:
        print("Opcion incorrecta")
if cat==2:
    print('''
        1.-Polera running 3000
        2.-Camiseta futbolito 1500
        3.-Zapatilla padel 60
''')
    op=int(input())
    if op==1:
        total+=2000+200
    elif op==2:
        total+=1500+200
    elif op==3:
        total+=20+200
    else:
        print("Opcion incorrecta")
        
    if cat==3:
        print('''
        1.-Polera running 3000
        2.-Camiseta futbolito 1500
        3.-Zapatilla padel 60
''')
    op=int(input())
    if op==1:
        total+=2000+200
    elif op==2:
        total+=1500+200
    elif op==3:
        total+=20+200
    else:
        print("Opcion incorrecta")
        
if total<=1000:
    total=total*0.97
elif total<=1001 and total>=5000:
    total=total*0.95
elif total>=5000:
    total=total*0.94
    print(f"El total a pagar es {total}")
