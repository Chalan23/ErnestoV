# #Inicio de estudio con ciclo for 
# ---------------------------------------------------------------# 

# for i in range(5): #todos los indices comienzan en 0
#     print("repeticion", i+1) 

# ---------------------------------------------------------------# 
# pide un numero al usuario y muestra cantidad de repeticiones
# num=int(input("Ingrese un numero: "))

# for i in range(num): 
#     print("repeticion", i+1) 

# ---------------------------------------------------------------# 

# # pide un numero al usuario y muestra la tabla de multiplicar hasta el 10

# num=int(input("Ingrese un numero para su tabla de multiplicar: "))

# for i in range(10): 
#     print(num, "X" , i+1, "=", num*(i+1))

# ---------------------------------------------------------------# 

# # pide un numero al usuario y muestra la tabla de multiplicar hasta el 10 (Profe)

# num=int(input("Ingrese un numero para su tabla de multiplicar: "))

# for i in range(1,11): 
#     print(num, "X" , i, "=" , i*num)

# #tablas de multiplica completa del 1 al 10 automaticas
# for j in range(10):
#     for i in range(10): 
#         print(j+1, "X" , i+1, "=" , (i+1)*(j+1))

# ---------------------------------------------------------------# 

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

# ---------------------------------------------------------------# 

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

# ---------------------------------------------------------------# 

# # Pida al usuario un numero y sume todos los digitos del 1 hasta ese digito

# num=int(input("Ingrese un numero: "))
# suma=0
# for i in range(num):
#     suma+=i+1
# print("La suma de los numeros es", suma)

# ---------------------------------------------------------------# 

# # par e impar

# num=int(input("Ingrese un numero: "))
# if num % 2==0:
#     print("El numero es par")

# else:
#     print("El numero es impar")

# ---------------------------------------------------------------# 

# #pida al usuario una cantidad de numeros y verifique si es par o impar

# cant=int(input("ingrese la cantidad de numeros"))
# for i in range(cant):
#     cant=0
#     num=int(input("Ingrese un numero: "))
#     if num % 2==0:
#         print("El numero es par")

#     else:
#         print("El numero es impar")

# ---------------------------------------------------------------# 

# #designe dos votantes, pida cantidad de votantes y muestre los resultados
# #verifique quien gano y considere un empate.

# print("Cuantas personas votan?")
# numVotantes =int(input())

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

#definir dos candidatos y pedir la cantidad de votos, mostrar resultados y verificar
#quien gano o si hubo empate. (profe)

# c1="Aqua"
# c2="koku"
# cv1=0
# cv2=0

# cantV=int(input("Cuantas peronas votan? "))

# for i in range(cantV):
#     print(f"por quiem votaras? 1.-{c1} 2.-{c2}")
#     voto=int(input ())
#     if voto==1:
#         cv1=cv1+1
#         # cv1+=1 (tambien se puede escribir asi la suma)
    
#     else:
#         cv2=cv2+1
# print(f"la cantidad de votos para {c1} es {cv1}")
# print(f"la cantidad de votos para {c2} es {cv2}")
# if cv1>cv2:
#     print(f"El ganador es {c1}")
# elif cv2>cv1:
#     print(f"El ganador es {c2}")
# else:  
#     print("Hubo un empate")


# # ver cuantas vocales tiene una palabra
# pa="musolini"
# vocales="aeiou"
# cont=0
# for i in pa:
#     if i in vocales:
#         cont+=1
# print("La cantidad de vocales es", cont)

# for i in pa:
#     print(i)

# ---------------------------------------------------------------# 

# frase= input("ingrese una frase: ")
# c=0
# v=0
# cons=0
# for i in frase:
#     # print(i)
#     if i.lower() in "aeiou":
#         v+=1
#     else:
#         cons=cons+1
#     c=c+1
# print("La cantidad de letras es", c)
# print("La cantidad de vocales es", v)
# print("La cantidad de consonantes es", cons)


# ---------------------------------------------------------------# 


# cant=int(input("Ingrese un numero: "))

# for i in range (cant):
#     num=int(input("Ingrese un numero: "))
#     if  num % 2==0:
#         print("El numero es par")

#     else:
#         print("El numero es impar")

# ---------------------------------------------------------------# 

# pedir un numero y mostrar todos los pares e impares desde 1 hasta el numero ingresado

# num=int(input("Ingrese un numero: "))

# for i in range(1, num+1):
#     if i % 2==0:
#         print(f"el numero {i} es par")
#     else:
#         print(f"es numero {i} impar")

# ---------------------------------------------------------------# 

# # super mercado 
# # ingrese la cantidad de productos 
# # preguntar al usuario cuantos preductos llevara y mostrar el total a pagar total + IVA

# cant=int(input("Ingrese la cantidad de productos: "))
# total=0
# for i in range(cant):
#     print('''
#         Que producto desea comprar?
#         1.- diazepan
#         2.- metametazona
#         3.- oblea china   
#           ''')
    
#     op=int(input("Ingrese su opcion: "))
#     if op==1:
#         print("usted lleva diazepan")
#         total=total+9000
#     elif op==2:
#         print("usted lleva metametazona")
#         total=total+18500
    
#     elif op==3: 
#         print("usted lleva oblea china")
#         total=total+1000

#     else: 
#         print("opcion no valida")
        
#     print("!-------------------------------------!")   
#     print(f"EL total neto es , {total}")
#     print(f"EL total mas IVA es , {total*1.19}")