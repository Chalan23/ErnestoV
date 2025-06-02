# # Ejercicios 1

# empleados = 0
# mas10años = 0
# menos10años = 0
# antiguedad = 0

# while True:
#     try:
#         empleados = int(input("Ingresa la cantidad de empleados registrados: "))
#         break
#     except Exception:
#         print("Error, debes ingresar un numero entero.")

# for i in range(empleados):
#     nombre = input(f"Ingresa el nombre del empleado N°{i+1} : ")
#     while True:
#         try:
#             antiguedad = int(input("Ingrese los años de antiguedad de que lleva en la empresa: "))
#             break
#         except Exception:
#             print("Error, debes ingresar un numero entero.")
#     if antiguedad > 10:
#         print("Mas de 10 años de antiguedad.")
#         mas10años += 1
#     else:
#         print("10 o menos años de antiguedad.")
#         menos10años += 1

# print(f"Se registraron {mas10años} empleados con más de 10 años de antiguedad.")
# print(f"Se registraron {menos10años} empleados con 10 o menos años de antiguedad.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicios 2

entradas = 23

while True:
    try:
        opcion = int(input("""
                                    ***** Cine Estrella *****
                        Bienvenido al sistema de venta de entradas del Cine Estrella
                        1.- Ver cuantas entradas quedan.
                        2.- Comprar una cantidad de entradas.
                        3.- Salir del sistema.   
                        Selecciona una opcion (1, 2 o 3) """))
    except Exception:
        print("Error, debe ingresar numeros enteros")

    match opcion:
        case 1:
            print(f"Las entradas disponibles son: {entradas}")
        case 2:
            try:
                cantidad = int(input("Cuantas entradas quieres comprar?: "))
                if cantidad <= 0:
                    print("Debes por lo menos comprar una entrada")
                elif cantidad > entradas:
                    print("Lo siento no hay suficientes entradas")
                else:
                    entradas -= cantidad
                    print(f"Compra exitosa!!! Quedan {entradas} entradas")
            except Exception:
                print("Debe ingresar un numero entero")
        case 3:
            print("Gracias por visitar Cine Estrella! vuelve pronto")
            break
        case _:
            print("Error, seleccione una opcion valida")





