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
# usar listas, diccionarios, funciones.
# 1.-Buscar productos
# 2.-Agregar productos
# 3.-Mostrar inventario
# 4.-Actualizar productos
# 5.-Salir  


inventario = [
    {"nombre":"chocolate","stock":20},
    {"nombre":"lentes","stock":15},
    {"nombre":"pilas","stock":10}
]

def buscarProductos(nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None

def agregarProductos():
    nombre = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad: "))
    producto = buscarProductos(nombre)
    if producto:
        producto["stock"] += cantidad
        print(f"Se agregaron {cantidad} unidades a {nombre}")
    else:
        inventario.append({"nombre": nombre, "stock": cantidad})
        print(f"Producto {nombre} agregado con {cantidad} unidades.")

def mostrarInventario():
    print("Inventario actual:")
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. {producto['nombre']} - {producto['stock']} unidades")
    print()

def actualizarProductos():
    nombre = input("Ingrese nombre del producto a actualizar: ").lower()
    producto = buscarProductos(nombre)
    if producto:
        nuevoStock = int(input(f"Ingrese el nuevo stock para {nombre}: "))
        producto["stock"] = nuevoStock
        print(f"Stock de {nombre} actualiza a {nuevoStock}")
    else:
        print("Producto no encontrado")
        
def eliminarProducto():
    nombre = input("Ingrese el nombre del producto que desea eliminar")
    producto = buscarProductos(nombre)
    if producto:
        inventario.remove(producto)
        print(f"El producto {nombre} se elimino del inventario.")
    else:
        print("Producto no encontrado")
while True:
    try:
        print("""
                Menu de inventario.
                1.-Buscar productos
                2.-Agregar productos
                3.-Mostrar inventario
                4.-Actualizar productos
                5.-Eliminar productos
                6.-Salir
              """)
        opcion = int(input("Ingresa una opcion: "))
        
        match opcion:
            
            case 1:
                nombre = input("Ingrese el nombre del producto a buscar: ").lower()
                producto = buscarProductos(nombre)
                if producto:
                    print(f"Producto encontrado: {producto['nombre']} - {producto['stock']} unidades")
                else:
                    print("Producto no encontrado")
            
            case 2:
                agregarProductos()
                
            case 3:
                mostrarInventario()
            
            case 4:
                actualizarProductos()
                
            case 5:
                eliminarProducto()
            
            case 6:
                print("Saliendo del programa!")
                break
            
            case _:
                print("Opcion no valida.")
    except Exception:
        print("Error, ingresa un numero valido.")