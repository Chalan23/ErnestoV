# # suma del total de los numeros de una lista
# lista = [1,2,3,4,5,6,7,8,9,10]
# suma = sum(lista)
# print(suma)

# ------------------------------------------------------------------------------------
# # Encontrar el numero mayor
# numeros = [10,2,5,16,23,20]
# mayor = max(numeros)
# print(mayor)

# ------------------------------------------------------------------------------------
# # Contar cuantas veces aparece un numero mayor de una lista
# lista = [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,4,4,4,4,3,3,3,3]
# numero = 2
# cantidad = lista.count(numero)
# print(cantidad)

# ------------------------------------------------------------------------------------
# # Eliminar duplicados de una lista
# lista = [1,2,3,3,4,5,5]
# sinDuplicados = list(set(lista))
# print(sinDuplicados)

# ------------------------------------------------------------------------------------
# # invertir una lista 
# lista = [1,2,3,4,5]
# invertir = []
# for i in range(len(lista)-1, -1, -1,):
#     invertir.append(lista[i])
# print(invertir)

# ------------------------------------------------------------------------------------
# # multiplicar todos los elementos de una lista.
# lista = [1,2,3,4,5]
# producto = 1
# for num in lista:
#     producto *= num
# print(producto)

# ------------------------------------------------------------------------------------
# # Encontrar elementos comunes en diferentes listas
# a = [1,2,3,4,5]
# b = [5,6,7,8,9]

# comunes = list(set(a) & set(b))
# print(comunes)

# ------------------------------------------------------------------------------------
# # Separar una lista en numeros pares e impares
# lista = [1,2,3,4,5,6,7,8,9,10]
# pares = []
# impares = []
# for num in lista:
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)
# print(f"Pares {pares}")
# print(f"ImPares {impares}")

# ------------------------------------------------------------------------------------
# # ordenar una lista
# lista = [5,1,4,2,8]
# for i in range(len(lista)):
#     for j in range(len(lista)-1):
#         if lista[j] > lista[j+1]:
#             lista[j], lista[j+1] = lista[j+1], lista[j]
# print(lista)

# ------------------------------------------------------------------------------------