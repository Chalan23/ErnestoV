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