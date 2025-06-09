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
#           1.- mostrar o ingresar nombre y apellido
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
#             for i in nombres:
#                 c=0
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
# seleccionar una opcion 
# 1.-agregar productos (Nombre producto y precio)
# 2.-comprar (Sub menu mostrando productos y precios)
# 3.-crear boleta
# 4.-salir

productos = ["disco", "memoria ram"]
precios = [10000, 30000]
carrito = []

while True:
    print("""
    1.- Agregar producto y precio
    2.- Comprar producto
    3.- Crear boleta
    4.- Salir
    """)
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
            producto = input("Ingrese el nombre del producto: ")
            productos.append(producto)
            precio = float(input("Ingrese el precio del producto: "))
            precios.append(precio)
        case 2:
          