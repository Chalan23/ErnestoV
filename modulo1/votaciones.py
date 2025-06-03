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

# ----------------------------------------------------------------------------#

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