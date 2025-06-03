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
