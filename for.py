# #Inicio de estudio con ciclo for 

# for i in range(5): #todos los indices comienzan en 0
#     print("repeticion", i+1) 

# pide un numero al usuario y muestra cantidad de repeticiones
# num=int(input("Ingrese un numero: "))

# for i in range(num): 
#     print("repeticion", i+1) 


# # pide un numero al usuario y muestra la tabla de multiplicar hasta el 10

# num=int(input("Ingrese un numero para su tabla de multiplicar: "))

# for i in range(10): 
#     print(num, "X" , i+1, "=", num*(i+1))


# # pide un numero al usuario y muestra la tabla de multiplicar hasta el 10 (Profe)

# num=int(input("Ingrese un numero para su tabla de multiplicar: "))

# for i in range(1,11): 
#     print(num, "X" , i, "=" , i*num)

# #tablas de multiplica completa del 1 al 10 automaticas
# for j in range(10):
#     for i in range(10): 
#         print(j+1, "X" , i+1, "=" , (i+1)*(j+1))



# #promedio de notas
# cant=int(input("ingrese la cantidad de notas"))
# suma=0
# for i in range(cant):
#     print("ingrese nota", i+1)
#     nota=float
#     (input())
#     suma += nota
#     # suma=suma+nota
# prom=suma/cant
# print("su promedio es", prom)


# # REVISAR
# # Cantidad de alumnos y sus promedios 

# cantA=int(input("ingrese la cantidad de alumnos"))

# for j in range(cantA):
#     print("ingrese nota del alumno ", j+1)
#     cantN=int(input())
#     suma=0
#     for i in range(cantN):
#         print("ingrese nota", i+1, "del alumno ", j+1,  "(Use valores decimales)")
#         nota=float(input())
#         suma += nota
#         # suma=suma+nota
#     prom=suma/cantN
#     print("su promedio es", prom)
#     if prom >4:
#         print("El alumno aprobo")
#     else:
#         print("El alumno reprobo")



# # Pida al usuario un numero y sume todos los digitos del 1 hasta ese digito

# num=int(input("Ingrese un numero: "))
# suma=0
# for i in range(num):
#     suma+=i+1
# print("La suma de los numeros es", suma)



# # par e impar

# num=int(input("Ingrese un numero: "))
# if num % 2==0:
#     print("El numero es par")

# else:
#     print("El numero es impar")



# #pida al usuario una cantidad de numeros y verifique si es par o impar

# cant=int(input("ingrese la cantidad de numeros"))
# for i in range(cant):
#     cant=0
#     num=int(input("Ingrese un numero: "))
#     if num % 2==0:
#         print("El numero es par")

#     else:
#         print("El numero es impar")


#designe dos votantes, pida cantidad de votantes y muestre los resultados
#verifique quien gano y considere un empate.

print("Cuantas personas votan?")
numVotantes =int(input())

lala = 0
lele = 0

print("Ingrese 1 si votas por lala o 2 si votas por lele")

for i in range(numVotantes):
    voto = int(input(f"Votante {i+1}, ingrese su voto: "))

    if voto == 1:
        lala += 1
    elif voto == 2:
        lele += 1
    else:
        print("voto nulo")

print("\nResultados:")
print(f"Votos para lala: {lala}")
print(f"Votos para lele: {lele}")

if lala > lele:
    print("Ganó lala")
elif lele > lala:
    print("Ganó lele")
else:
    print("Empate")


