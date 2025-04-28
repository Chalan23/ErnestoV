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


import random