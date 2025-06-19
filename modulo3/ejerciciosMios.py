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
# # usar listas, diccionarios, funciones.
# # 1.-Buscar productos
# # 2.-Agregar productos
# # 3.-Mostrar inventario
# # 4.-Actualizar productos
# # 5.-Salir  


# inventario = [
#     {"nombre":"chocolate","stock":20},
#     {"nombre":"lentes","stock":15},
#     {"nombre":"pilas","stock":10}
# ]

# def buscarProductos(nombre):
#     for producto in inventario:
#         if producto["nombre"] == nombre:
#             return producto
#     return None

# def agregarProductos():
#     nombre = input("Ingrese el nombre del producto: ").lower()
#     cantidad = int(input("Ingrese la cantidad: "))
#     producto = buscarProductos(nombre)
#     if producto:
#         producto["stock"] += cantidad
#         print(f"Se agregaron {cantidad} unidades a {nombre}")
#     else:
#         inventario.append({"nombre": nombre, "stock": cantidad})
#         print(f"Producto {nombre} agregado con {cantidad} unidades.")

# def mostrarInventario():
#     print("Inventario actual:")
#     for i, producto in enumerate(inventario, 1):
#         print(f"{i}. {producto['nombre']} - {producto['stock']} unidades")
#     print()

# def actualizarProductos():
#     nombre = input("Ingrese nombre del producto a actualizar: ").lower()
#     producto = buscarProductos(nombre)
#     if producto:
#         nuevoStock = int(input(f"Ingrese el nuevo stock para {nombre}: "))
#         producto["stock"] = nuevoStock
#         print(f"Stock de {nombre} actualiza a {nuevoStock}")
#     else:
#         print("Producto no encontrado")
        
# def eliminarProducto():
#     nombre = input("Ingrese el nombre del producto que desea eliminar")
#     producto = buscarProductos(nombre)
#     if producto:
#         inventario.remove(producto)
#         print(f"El producto {nombre} se elimino del inventario.")
#     else:
#         print("Producto no encontrado")
# while True:
#     try:
#         print("""
#                 Menu de inventario.
#                 1.-Buscar productos
#                 2.-Agregar productos
#                 3.-Mostrar inventario
#                 4.-Actualizar productos
#                 5.-Eliminar productos
#                 6.-Salir
#               """)
#         opcion = int(input("Ingresa una opcion: "))
        
#         match opcion:
            
#             case 1:
#                 nombre = input("Ingrese el nombre del producto a buscar: ").lower()
#                 producto = buscarProductos(nombre)
#                 if producto:
#                     print(f"Producto encontrado: {producto['nombre']} - {producto['stock']} unidades")
#                 else:
#                     print("Producto no encontrado")
            
#             case 2:
#                 agregarProductos()
                
#             case 3:
#                 mostrarInventario()
            
#             case 4:
#                 actualizarProductos()
                
#             case 5:
#                 eliminarProducto()
            
#             case 6:
#                 print("Saliendo del programa!")
#                 break
            
#             case _:
#                 print("Opcion no valida.")
#     except Exception:
#         print("Error, ingresa un numero valido.")
        
# ---------------------------------------------------------------------------------

# # crear un programa de diccionarios dentro de un diccionario

# personas = {
#     1:{ "nombre": "diego rivera",
#         "numeros":[12345678],
#         "estado_civil":"casado",
#         "trabajando": True,
#         "edad": 64},
#     2:{ "nombre": "ernesto vilches",
#         "numeros":[23232323],
#         "estado_civil":"casado",
#         "trabajando": False,
#         "edad": 32},
#     3:{"nombre": "paula tramolao",
#         "numeros":[87654321],
#         "estado_civil":"soltero",
#         "trabajando": True,
#         "edad": 26}}

# def ingresar_personas(personas):
#     nombre = input("Ingrese su nombre: ")
#     numero = int(input("Ingrese su numero: "))
#     estado = int(input("Estado civil 1.-casado - 2.-soltero.: "))
#     if estado == 1:
#         estado_civil = "casado"
#     else:
#         estado_civil = "soltero"
#     edad = int(input("Que edad tiene: "))
#     nextkey = len(personas) + 1
#     personas[nextkey] = {
#         "nombre": nombre,
#         "numeros": [numero],
#         "estado_civil": estado_civil,
#         "trabajando": True,
#         "edad": edad}

# def consultar_personas(personas):
#     for key, val in personas.items():
#         print(key, val)

# def actualizar_personas(personas):
#     for key, val in personas.items():
#         print(key, val)
#     pide = int(input("Ingresa el ID de la persona que quieres actualizar: "))
#     if pide in personas:
#         nombre = input("Nuevo nombre (o dejar vacio para mantener: )")
#         numero = input("nuevo numero (o dejar vacio para mantener: )")
#         estado = input("1.-Casado - 2.-Soltero (o dejar vacio para mantener: )")
#         edad = int(input("Ingresa tu edad (o dejar vacio para mantener: )"))
#         trabajando = input("Estas trabajando s/n").lower()
#         if nombre:
#             personas[pide]["nombre"] = nombre
#         if numero:
#             personas[pide]["numero"] = [int(numero)]
#         if estado == "1":
#             personas[pide]["estado_civil"] = "Casado"
#         elif estado == "2":
#             personas[pide]["estado_civil"] = "Soltero"
#         if edad: 
#             personas[pide]["edad"] = (edad)
#         if trabajando == "s":
#             personas[pide]["trabajando"] = True
#         elif trabajando == "n":
#             personas[pide]["trabajando"] = False
#     else:
#         print("ID no encontrado")
        
# def borrar_personas(personas):
#     for key, val in personas.items():
#         print(key,val)
#     dell = int(input("Selecciona cual desea borrar: "))
#     if dell in personas:
#         del personas[dell]
#         print("persona borrada")
#     else:
#         print("ID no encontrado")

# while True:
#     try:
#         print("""
#               1.-Ingresar personas
#               2.-Consultar personas
#               3.-Actualizar personas
#               4.-Borrar personas
#               5.-Salir 
#               """)
#         op = int(input("Ingrese una opcion: "))
#         match op:
#             case 1:
#                 ingresar_personas(personas)
#             case 2:
#                 consultar_personas(personas)
#             case 3:
#                 actualizar_personas(personas)
#             case 4:
#                 borrar_personas(personas)
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, opcion no valida")
#     except Exception as e:
#         print("Error")

# ----------------------------------------------------------------------------------------

# hacer un carrito de compras con 3 productos y sus precios 
# el menu debe tener:
# 1.-Agregar producto al carrito
# 2.-Ver carrito
# 3.-Actualizar cantidad de un producto
# 4.-Eliminar producto del carrito
# 5.-Salir 
# debe tener funciones, match case, while true, try, listas y diccionarios

productos = [
    {"nombre": "manzana", "precio": 500},
    {"nombre": "pan", "precio": 1000},
    {"nombre": "leche", "precio": 1200}
]

carrito = []

def mostrar_productos():
    print("Productos disponibles:")
    for i, prod in enumerate(productos, 1):
        print(f"{i}. {prod["nombre"]} - ${prod["precio"]}")
    print()

def agregar_al_carrito():
    mostrar_productos()
    try:
        opcion = int(input("Seleccione el producto a agregar (numero): "))
        if 1 <= opcion <= len(productos):
            cantidad = int(input("Ingrese la cantidad: "))
            nombre = productos[opcion-1]["nombre"]
            precio = productos[opcion-1]["precio"]
            for item in carrito:
                if item["nombre"] == nombre:
                    item["cantidad"] += cantidad
                    print(f"Se agregaron {cantidad} {nombre}(s) al carrito.")
                    return
            carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print(f"{nombre} agregado al carrito.")
        else:
            print("Opcion invalida.")
    except Exception:
        print("Entrada invalida.")

def ver_carrito():
    if not carrito:
        print("El carrito esta vacio.")
        return
    total = 0
    print("Carrito de compras:")
    for i, item in enumerate(carrito, 1):
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{i}. {item['nombre']} - ${item['precio']} x {item['cantidad']} = ${subtotal}")
    print(f"Total a pagar: ${total}")

def actualizar_cantidad():
    if not carrito:
        print("El carrito esta vacio.")
        return
    ver_carrito()
    try:
        opcion = int(input("Seleccione el producto a actualizar (u): "))
        if 1 <= opcion <= len(carrito):
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            if nueva_cantidad > 0:
                carrito[opcion-1]["cantidad"] = nueva_cantidad
                print("Cantidad actualizada.")
            else:
                print("Cantidad invalida.")
        else:
            print("o invalida.")
    except Exception:
        print("Entrada invalida.")

def eliminar_producto():
    if not carrito:
        print("El carrito esta vacio.")
        return
    ver_carrito()
    try:
        opcion = int(input("Seleccione el producto a eliminar (u): "))
        if 1 <= opcion <= len(carrito):
            eliminado = carrito.pop(opcion-1)
            print(f"{eliminado['nombre']} eliminado del carrito.")
        else:
            print("o invalida.")
    except Exception:
        print("Entrada invalida.")

while True:
    try:
        print("""
        Menu Carrito de Compras
        1.-Agregar producto al carrito
        2.-Ver carrito
        3.-Actualizar cantidad de un producto
        4.-Eliminar producto del carrito
        5.-Salir
        """)
        op = int(input("Seleccione una opción: "))
        match op:
            case 1:
                agregar_al_carrito()
            case 2:
                ver_carrito()
            case 3:
                actualizar_cantidad()
            case 4:
                eliminar_producto()
            case 5:
                print("¡Gracias por usar el carrito de compras!")
                break
            case _:
                print("o no válida.")
    except Exception:
        print("Error, ingrese un u válido.")


