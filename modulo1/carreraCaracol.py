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
