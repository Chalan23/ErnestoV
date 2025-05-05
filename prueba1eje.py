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










































