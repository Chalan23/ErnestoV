# crear un programa que pida la cantidad de ramos 
# # luego pida el promedio por cada materia 
# # basado en su promedio final, aplique puntaje de beneficios
# # 4.5 y 5 : 300, 5.1 y 6 : 500, 6.1  y 7.: 800
# # agregar puntaje segun carrera 
# # tecnico: +60, ingeneria: +40, diplomado: +20
        
# mat=int(input("Ingrese la cant de materias: "))
# suma=0
# for i in range(mat):
#    notaramo=float(input(f"Ingrese la nota del ramo{i+1}: "))
#    suma+=notaramo
# prom=suma/mat
# print("Su nota final es ", round(prom,1))
# if prom>=4.5 and prom<=5.0:
#    puntaje=300
#    print( f"Su puntaje de beneficios es de {puntaje}")
# elif prom>=5.2 and prom<=6.0:
#     puntaje=500
#     print( f"Su puntaje de beneficios es de {puntaje}")
# elif prom>=6.1 and prom<=7.0:
#     puntaje=800
#     print( f"Su puntaje de beneficios es de {puntaje}")
# else:
#    print(" Es tan porro que no tiene beneficios")

# car=int(input('''
#             Ingrese su tipo de grado
#               1.- Tecnico
#               2.- Ingenieria
#               3.- Diplomado
#               '''))
# if car==1:
#    puntaje+=60
# elif car==2:
#    puntaje+=40
# elif car==3:
#    puntaje+=20
# else:
#    print("no es nuemro valido")

# print( " El puntaje de beneficios es ", puntaje)
    