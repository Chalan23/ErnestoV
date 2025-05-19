# otros ejercicios de for 

#perros de casa 
# pida al usuario la cantidad de perros 
# muestre cual es la cuota minima de conejos 
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minina 
# cumolio la cuota, sino se queda sin filete 
# mostrar resumen de perro que cumplieron y los que no

# conejos = 0
# cuotaConejos = int(input("Ingrese la cuota minima de conejos: "))

# perros=int(input("Ingrese un numero de perrros: "))

# for i in range(perros):
#     nombrePerro = input(f"Cual es el nombre del perro {i+1}: ")
#     conejosCazados=int(input("Cuantos conejos caso el perro: "))
#     if conejosCazados >= cuotaConejos:
#         print(f"El perro {nombrePerro} cumplio la cuota")
#         conejos += conejosCazados
#     else:
#         print(f"El perro {nombrePerro} no cumplio la cuota")
#         print(f"El perro {nombrePerro} no tiene filete")

# print(f"El total de conejos es de {conejos}")

import random
while True:
    try:
        cant=int(input("Ingrese la cantidad de perros: "))
        break
    except Exception:
        print("Esto solo acepta numeros enteros")
cuota=3
cumple=0

for i in range(cant):
    con=random.randint(0,5)
    print(f"El perro {i+1} trajo {con} conejos")
    if con >= cuota:
        print(f"El perro gana filete")
        cumple += 1
    else:
        print(f"El perro no gana filete")

print(f"La cantidad de perros que cumplieron la cuota es de: {cumple}")
print(f"La cantidad de perros que no cumplieron la cuota es de: {cant-cumple}")