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


# # ejercicio profe
# import random
# while True:
#     try:
#         cant=int(input("Ingrese la cantidad de perros: "))
#         break
#     except Exception:
#         print("Esto solo acepta numeros enteros")
# cuota=3
# cumple=0

# for i in range(cant):
#     con=random.randint(0,5)
#     print(f"El perro {i+1} trajo {con} conejos")
#     if con >= cuota:
#         print(f"El perro gana filete")
#         cumple += 1
#     else:
#         print(f"El perro no gana filete")

# print(f"La cantidad de perros que cumplieron la cuota es de: {cumple}")
# print(f"La cantidad de perros que no cumplieron la cuota es de: {cant-cumple}")


# quiere pasar el ramo?
# pregunta la cantidad de rojos en el curso
# los talleres que hay en el semestre son 4
# por cada taller asistido obtienen 0.3 decimas 
# si el alumno tiene mas de 1 punto 
# tiene la bendicion del profe
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acumuladas.
# muestra si aprueba o reprueba.



# try:
#     cantidadRojos=int(input("Ingrese la cantidad de rojos: "))
#     total=0
#     for i in range(cantidadRojos):
#         print(f"Ingrese el rojo de {i+1} (Ingresa numeros decimales)")
#         nota=float(input("Ingrese la nota: "))
#         total += nota

#     print("asistio a los 4 talleres")
#     canTalleres=int(input("Cuantos talleres asistio? "))
#     decimas=canTalleres*0.3
#     if canTalleres == 4:
#         print("Bendecido por el profe")
#     else:
#         print("No asistio a todos los talleres")
    
#     notaFinal=total+decimas/cantidadRojos
#     print(f"Su nota final es de {notaFinal}")

#     if notaFinal >= 4:
#         print("Usted aprobo el ramo")
#     else:
#         print("Usted reprobo el ramo")
# except Exception:
#     print("Esto solo acepta numeros")


# #ejercicio profe 

# rojos = int(input("Ingrese la cantidad de rojos: "))
# talleres = 4
# tDecimas = 0

# for r in range(rojos):
#     for t in range(talleres):
#         asist=input(f"Asistio al taller {t+1}? Si / No: " )
#         if asist.lower() == "Si":
#             tDecimas += 0.3
#     if tDecimas >= 1:
#         print("Bendecido por el profe")
#     else:
#         print("No bendecido por el profe")
#     nf=float(input("Ingrese la nota final: "))
#     nf += tDecimas
#     print(f"Su nota final es de {nf}")
#     if nf >= 4:
#         print("Aprobado")
#     else:
#         print("Reprobado")


# lavado de autos 
# crear un menu para lavar autos
# 1.- Cursar pago del lavado
# 2.- Ver ventas diarias
# 3.- Salir
# El lavado tiene tres niveles
# 1.- full $15.000, 2- standard 10.000, 3- basico $7.000
# al mostrar ventas diarias, debe mostrar la
# cantidad de autos lavados y montos total recaudado
# tambien debe mostrar el monto mas alto pagado
# notas: usar try 

ventas_totales = 0
autos_lavados = 0
monto_mas_alto = 0

while True:
    print("Bienvenido al lavado de autos")
    print('''
    1.- Cursar pago del lavado
    2.- Ver ventas diarias
    3.- Salir''')
    
    try:
        op = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue
    
    if op == 1:
        print("Elija el tipo de lavado:")
        print('''
        1.- Full     $15.000
        2.- Standard $10.000
        3.- Básico   $7.000''')
        
        try:
            opLavado = int(input("¿Qué tipo de lavado desea?: "))
        except ValueError:
            print("Error: Ingrese un número válido para el tipo de lavado.")
            continue

        if opLavado == 1:
            print("Lavado Full seleccionado")
            total = 15000
        elif opLavado == 2:
            print("Lavado Standard seleccionado")
            total = 10000
        elif opLavado == 3:
            print("Lavado Básico seleccionado")
            total = 7000
        else:
            print("Opción de lavado no válida.")
            continue  

        autos_lavados += 1
        ventas_totales += total
        if total > monto_mas_alto:
            monto_mas_alto = total
        
        print(f"Pago realizado: ${total}")

    elif op == 2:
        print("\n--- Ventas Diarias ---")
        print(f"Autos lavados: {autos_lavados}")
        print(f"Total recaudado: ${ventas_totales}")
        print(f"Monto más alto pagado: ${monto_mas_alto}")
        
    elif op == 3:
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

