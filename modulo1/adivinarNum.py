
# # crea un programa que simule un juego de adivinanzas. El programa debe generar un numero aleatorio entre 
# # 1 y 10 usando random.randint. Luego, debe pedirle al usuario que adivine el número. El usuario tiene 3
# # intentos. Si adivina correctamente, el programa debe felicitarlo. Si no lo adivina en 3 intentos, debe mostrar
# # el número correcto. Usa import random y un bucle while.

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