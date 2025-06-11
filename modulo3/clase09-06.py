# tarea realizar proyecto en grupo dos o 3 personas github

# -------------------------------------------------------------
# # listas

# # #       -5 -4 -3 -2 -1
# numeros = [2,5,12,8,77,7.9]
# # # indice 0, 1, 2, 3, 4

# # con indice negativo -1 llamo de atras hacia adelante
# print(round(numeros[-1]))

# for numero in numeros:
#     print("numeros X 2", numero*2)

# nombres = ["Felipe","Curly","Larry","Moe"]

# print(nombres)

# nombres.append("luthien") # append agrega un valor al final por ejemplo en los nombres

# print(nombres)

# -------------------------------------------------------------
# # menu ingresar nombres 
# # 1.- ingresa un nombre
# # 2.- ver nombres
# # 3.- salir

# nombres = []

# while True:
#     print("""
#           1.- Ingresar un nombre
#           2.- Consultar nombres
#           3.- Salir
#           """)
#     opcion = int(input("Ingrese una opcion: "))
#     match opcion:
#         case 1:
#             nombre = input("Ingresa un nombre: ")
#             nombres.append(nombre)
#         case 2:
#             print(nombres)
#         case 3:
#             print("Saliendo...")
#             break
#         case _:
#             print("Error ingresa una opcion valida.")
            
            
# -------------------------------------------------------------
# # ingresar nombres y apellidos 

# nombres = ["Ernesto","Alfredo", "Jonny","Hanz"]
# apellidos =["Vilches","Chalan", "Bravo", "Zimmer"]

# while True:
#     print("""
#           1.- mostrar nombre y apellido
#           2.- Consultar nombres
#           3.- Salir
#           """)
#     opcion = int(input("Ingrese una opcion: "))
#     match opcion:
#         case 1:
#             nombre = input("Ingresa su nombre: ")
#             nombres.append(nombre)
#             apellido = input("Ingresa su apellido: ")
#             apellidos.append(apellido)
#         case 2:
#             c=0
#             for i in nombres:
#                 print(nombres[c], apellidos[c])
#                 c+=1
#         case 3:
#             print("Saliendo...")
#             break
#         case _:
#             print("Error ingresa una opcion valida.")
            
# -------------------------------------------------------------    
   
# nombres = ["Ernesto","Alfredo", "Jonny","Hanz"]
# apellidos =["Vilches","Chalan", "Bravo", "Zimmer"]

# while True:
#     print("""
#           1.- Ingresar nombre y apellido
#           2.- Consultar nombres
#           3.- Buscar
#           4.- Salir
#           """)
#     opcion = int(input("Ingrese una opcion: "))
#     match opcion:
#         case 1:
#             nombre = input("Ingresa su nombre: ")
#             nombres.append(nombre)
#             apellido = input("Ingresa su apellido: ")
#             apellidos.append(apellido)
#         case 2:
#             c=0
#             for i in nombres:
#                 print(nombres[c], apellidos[c])
#                 c+=1
#         case 3:
#             buscar=input("Indique que nombre buscara: ")
#             if buscar in nombres:
#                 print(f"El nombre {buscar} esta en la lista")
#             else:
#                 print(f"El nombre {buscar} NO esta en la lista")
                
#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("Error ingresa una opcion valida.")
            
# -------------------------------------------------------------            
# # # seleccionar una opcion 
# # # 1.-agregar productos (Nombre producto y precio)
# # # 2.-comprar (Sub menu mostrando productos y precios)
# # # 3.-crear boleta
# # # 4.-salir

# productos = ["disco SSD", "memoria Ram"]
# precios = [70000, 30000]
# carrito = []

# while True:
#     print('''
#         1.- Agregar Productos
#         2.- Comprar
#         3.- Crear Boleta
#         4.- Salir
#     ''')
#     op = int(input("Ingrese una opción: "))

#     match op:
#         case 1:
#             nom = input("Ingrese el producto: ")
#             precio = int(input("Ingrese precio: "))
#             productos.append(nom)
#             precios.append(precio)
#         case 2:
#             print("Productos disponibles:")
#             for i in range(len(productos)):
#                 print(f"{i+1}.- {productos[i]} - ${precios[i]}")
#             seleccion = int(input("Seleccione el número del producto a comprar: "))
#             if 1 <= seleccion <= len(productos):
#                 carrito.append(seleccion - 1)
#                 print("Producto agregado al carrito.")
#             else:
#                 print("Selección fuera de rango.")
#         case 3:
#             if len(carrito) == 0:
#                 print("El carrito está vacío.")
#             else:
#                 print("BOLETA:")
#                 total = 0
#                 for idx in carrito:
#                     print(f"{productos[idx]} - ${precios[idx]}")
#                     total += precios[idx]
#                 print(f"Total a pagar: ${total}")
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opción inválida")

# -----------------------------------------------------------------------
# ejercicio con el profe
# seleccionar una opcion 
# 1.-agregar productos (Nombre producto y precio)
# 2.-comprar (Sub menu mostrando productos y precios)
# 3.-crear boleta
# 4.-salir

productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
precios=[70000, 30000, 15000]
carrito=[]

while True:
    print('''
        1.- Ingresar productos a la tienda
        2.- Comprar
        3.- Crear Boleta
        4.- Salir
          ''')
    op=int(input("Ingese una opcion: "))
    match op:
        case 1:
            nom=input("Ingrese un Producto: ")
            productos.append(nom)
            ape=int(input("Ingrese un Precio: "))
            precios.append(ape)
        case 2:
                for i in range(3):
                    print(i+1, ".-", productos[i], "$", precios[i] )
                pro=int(input("Selecione que quiere comprar: "))
                carrito.append(pro-1)
                print(carrito)
        case 3:
            total=0
            print("---------------0----------------")
            print("Bienvenido a PC House ")
            for i in carrito:
                  print( productos[i], "----- $", precios[i] )
                  total=total+precios[i]
            print("Es total de articulos es", len(carrito))
            print("Su total neto es ", total)
            print("Su total mas iva es ", total*1.19)
            print("---------------0----------------")

        case 4:
            print("Saliendo")
            break
        case _:
            print("opcion invalida")

