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

# lista de matrimonio 
#   1.- Registrar una persona
#   2.- Mostrar personas
#   3.- Actualizar personas
#   4.- Borrar personas
#   5.- Salir

# personas = {
#     1: {"nombre": "ernesto", "edad": 32, "invitado": True},
#     2: {"nombre": "camila", "edad": 29, "invitado": True}
# }

# def mostrar_personas(personas):
#     for key, nombre in personas.items():
#         print(key, nombre)
# def valida_pass(clave):
#     mayuscula = False
#     minuscula = False
#     numero = False
#     for palabra in clave:
#         if palabra.isupper():
#             mayuscula = True
#         elif palabra.islower():
#             minuscula = True
#         elif palabra.isdigit():
#             numero = True
#     return mayuscula and minuscula and numero
# def ingresar_persona(personas):
#     nombre = input("Ingrese su nombre: ")
#     edad = int(input("Ingrese su edad: "))
#     invitado = input("¿Es invitado? (s/n): ").lower()
#     if invitado == 's':
#         invitado = True
#     else:
#         invitado = False
#     nextkey = len(personas) + 1
#     personas[nextkey] = {
#         "nombre": nombre,
#         "edad": edad,
#         "invitado": invitado
#     }
# def actualizar_persona(personas):
#     mostrar_personas(personas)
#     pide = int(input("Ingrese el ID de la persona que desea actualizar: "))
#     if pide in personas:
#         nombre = input("Nuevo nombre (o dejar vacio para mantener): ")
#         edad = input("Nueva edad (o dejar vacio para mantener): ")
#         invitado = input("¿Es invitado? (s/n) (o dejar vacio para mantener): ").lower()
#         if nombre:
#             personas[pide]["nombre"] = nombre
#         if edad:
#             personas[pide]["edad"] = int(edad)
#         if invitado == 's':
#             personas[pide]["invitado"] = True
#         elif invitado == 'n':
#             personas[pide]["invitado"] = False
#     else:
#         print("ID no encontrado")
# def borrar_persona(personas):
#     mostrar_personas(personas)
#     dell = int(input("Selecciona el ID de la persona que desea borrar: "))
#     if dell in personas:
#         del personas[dell]
#         print("Persona borrada")
#     else:
#         print("ID no encontrado")

# while True:
#     try:
#         print("""
#                 1.- Registrar una persona
#                 2.- Mostrar personas
#                 3.- Actualizar personas
#                 4.- Borrar personas
#                 5.- Salir
#               """)
#         opcion = int(input("Seleciona una opcion: "))
#         match opcion:
#             case 1:
#                 ingresar_persona(personas)
#             case 2:
#                 mostrar_personas(personas)
#             case 3:
#                 actualizar_persona(personas)
#             case 4:
#                 borrar_persona(personas)
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, seleciona una opcion valida.")
#     except Exception as e:
#         print("Error")


# -------------------------------------------------------------------------------------------

# carrito de compras (Bueno)
# registrar un articulo 
# muestra articulos
# actualizar producto 
# borrar producto
# salir

articulos = {
    1:{"nombre":"leche",
       "precio": 1000,
       "codigo":"LLee10"},
    2:{"nombre":"cereal",
       "precio": 1500,
       "codigo":"CCee15"},
    3:{"nombre":"jugo",
       "precio": 1200,
       "codigo":"JJuu12"}
}

def mostrar_productos(dicc):
    for key, articulos  in dicc.items():
        print(key, articulos)
        
def validar_code(codigo):
    mayuscula=False
    minuscula=False
    numero=False
    for palabra in codigo:
        if palabra.isupper():
            mayuscula=True
        if palabra.islower():
            minuscula=True
        if palabra.isdigit():
            numero=True
    if mayuscula and minuscula and numero and len(codigo)==6:
        print("El codigo esta bien ingresado")
        return True
    else:
        print("El codigo esta mal escrito, debe tener al menos una mayuscula, minuscula y numero")
        return False
    
def ingresar_articulo(dicc):
    nombre=input("Ingrese el nombre: ")
    precio=input("Ingrese el precio: ")
    codigo=input("Ingrese el codigo: ")
    if validar_code(codigo):
        largo=list(dicc.keys())[-1]
        dicc[largo+1]={"nombre":nombre,
                       "precio":precio,
                       "codigo":codigo}
    else:
        print("El parametro del codigo no es correcto")












def actualizar_producto(dicc):
    mostrar_productos(dicc)
    actualizar=int(input("Seleccionar un articulo: "))
    while True:
        print("""
              1.-Nombre
              2.-Precio
              3.-Codigo
              4.-Salir
              """)
        dato=int(input("Que dato va actualizar: "))
        match dato:
            case 1:
                n=input("Ingrese nuevo nombre: ")
                dicc[actualizar]["nombre"]=n
            case 2:
                n=input("Ingrese nuevo precio: ")
                dicc[actualizar]["precio"]=n
            case 3:
                n=input("Ingrese nuevo codigo: )")
                if validar_code(n):
                    dicc[actualizar]["codigo"]=n
                else:
                    print("El parametro del codigo no es correcto")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")


















 



















def borrar_articulos(dicc):
    mostrar_productos(dicc)
    borrar=int(input("Seleccionar el articulo a borrar: "))
    del dicc[borrar]

while True:
    try:
        print("""
              ---Menu de compras---
              1.-Ingresar un articulo
              2.-Muestra articulos 
              3.-Actualiza productos
              4.-Borrar productos
              5.-Salir.
              """)
        opcion = int(input("Ingresa una opcion: "))
        match opcion:
            case 1:
                ingresar_articulo(articulos)
            case 2:
                mostrar_productos(articulos)
            case 3:
                actualizar_producto(articulos)
            case 4:
                borrar_articulos(articulos)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Error ingresa una opcion valida")
    except Exception as e:
        print("Error")



# -------------------------------------------------------
# carrito de compras 
# registrar un articulo 
# muestra articulos
# actualizar producto 
# borrar producto
# salir

# articulos = {
#     1: {"nombre": "azucar",
#         "precio": 500,
#         "codigo": "AAzz50"},
#     2: {"nombre": "sal",
#         "precio": 800,
#         "codigo": "SSAA80"}
# }

# def mostrar_articulos(dicc):
#     for key, articulos in dicc.items():
#         print(key, articulos)

# def borrar_articulos(dicc):
#     mostrar_articulos(dicc)
#     borrar = int(input("Que ID quieres borrar"))
#     del dicc[borrar]

# def validar_code(codigo):
#     mayuscula = False
#     minuscula = False
#     numero = False
#     for palabra in codigo:
#         if palabra.isupper():
#             mayuscula = True
#         if palabra.islower():
#             minuscula = True
#         if palabra.isdigit():
#             numero = True
#     if mayuscula and minuscula and numero and len(codigo) == 6:
#         print("El codigo cumple con los parametros")
#         return True
#     else:
#         print("No cumple con los parametros solicitados")
#         return False

# def ingresar_articulo():
#     nombre=input("Ingresar nombre: ")
#     precio=input("Ingresar precio: ")
#     codigo=input("Ingresar codigo: ")
#     if validar_code(codigo):
#         largo=list(dicc.keys())[-1]
#         dicc[largo+1]={"nombre":nombre,
#                        "precio":precio,
#                        "codigo":codigo}
#     else:
#         print("El parametro no es correcto")

# def actualizar_articulo(dicc):
#     mostrar_articulos(dicc)
#     act = int(input("Que actualizara: "))
#     while True:
#         print("""
#               1.-nombre
#               2.-precio
#               3.-codigo
#               4.-salir
#               """)
#         dato=int(input("Que dato va actualizar: "))
#         match dato:
#             case 1:
#                 n=input("Nuevo nombre: ")
#                 dicc[act]["nombre"]=n
#             case 2:
#                 n=input("Nuevo precio: ")
#                 dicc[act]["precio"]=n
#             case 3:
#                 n=input("Nuevo codigo: ")
#                 if validar_code(n):
#                     dicc[act]["precio"]=n
                
#                 else:
#                     print("Codigo no correcto")
                    
# while True:
#     try:
#         print("""
#               ---Carrito de compras---
#               1.-Ingresar articulos
#               2.-Mostrar articulos
#               3.-Actualizar articulos 
#               4.-Borrar articulos 
#               5.-Salir
#               """)
#         opcion = int(input("Ingrese una opcion: "))
#         match opcion:
#             case 1:
#                 ingresar_articulo(articulos)
#             case 2:
#                 mostrar_articulos(articulos)
#             case 3:
#                 actualizar_articulo(articulos)
#             case 4:
#                 borrar_articulos(articulos)
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, ingresa una opcion valida")
#     except Exception as e:
#         print("Error")


# ----------------------------------------------------------------------------------------

# # carrito de compras 
# # registrar un articulo 
# # muestra articulos
# # actualizar producto 
# # borrar producto
# # salir

# productos = {
#     1: {"nombre": "Helado", "precio": 1000, "codigo": "HHee10"},
#     2: {"nombre": "Chocolate", "precio": 1200, "codigo": "CChh12"}
# }

# def mostrar_productos(dic):
#     for key, producto in dic.items():
#         print(key, producto)

# def borrar_productos(dic):
#     mostrar_productos(dic)
#     try:
#         borrar = int(input("Que producto deseas borrar (ID): "))
#         if borrar in dic:
#             del dic[borrar]
#             print("Producto borrado.")
#         else:
#             print("ID no encontrado.")
#     except Exception:
#         print("Error al borrar producto.")

# def validar_code(codigo):
#     mayuscula = False
#     minuscula = False
#     numeros = False
#     for c in codigo:
#         if c.isupper():
#             mayuscula = True
#         if c.islower():
#             minuscula = True 
#         if c.isdigit():
#             numeros = True
#     if mayuscula and minuscula and numeros and len(codigo) == 6:
#         print("Los parametros estan bien")
#         return True
#     else:
#         print("No cumple los parametros")
#         return False

# def actualizar_producto(dic):
#     mostrar_productos(dic)
#     try:
#         actualizar = int(input("Que producto desea actualizar (ID): "))
#         if actualizar not in dic:
#             print("ID no encontrado.")
#             return
#         while True:
#             print("""
#               1.-Nombre 
#               2.-Precio
#               3.-Codigo
#               4.-Salir
#               """)
#             dato = int(input("Que dato deseas actualizar: "))
#             match dato:
#                 case 1:
#                     n = input("Ingrese el nuevo nombre: ")
#                     dic[actualizar]["nombre"] = n
#                 case 2:
#                     try:
#                         n = int(input("Ingrese el nuevo precio: "))
#                         dic[actualizar]["precio"] = n
#                     except Exception:
#                         print("Precio invalido.")
#                 case 3:
#                     n = input("Ingrese el nuevo codigo: ")
#                     if validar_code(n):
#                         dic[actualizar]["codigo"] = n
#                     else:
#                         print("El codigo no es correcto")
#                 case 4:
#                     print("Saliendo...")
#                     break
#                 case _:
#                     print("Error, ingresa una opcion valida")
#     except Exception:
#         print("Error al actualizar producto.")

# def ingresa_articulo(dic):
#     nombre = input("Ingrese el nombre: ")
#     try:
#         precio = int(input("Ingrese el precio: "))
#     except Exception:
#         print("Precio invalido.")
#         return
#     codigo = input("Ingrese el codigo: ")
#     if validar_code(codigo):
#         if dic:
#             nuevo_id = max(dic.keys()) + 1
#         else:
#             nuevo_id = 1
#         dic[nuevo_id] = {
#             "nombre": nombre,
#             "precio": precio,
#             "codigo": codigo
#         }
#         print("Articulo agregado.")
#     else:
#         print("El parametro no es correcto")

# while True:
#     try:
#         print("""
#               °°°Menu Opciones°°°
#                 1.-Registrar un articulo 
#                 2.-Muestra articulos
#                 3.-Actualizar producto  
#                 4.-Borrar producto
#                 5.-Salir
#               """)
#         opciones = int(input("Elige una opcion: "))
#         match opciones:
#             case 1:
#                 ingresa_articulo(productos)
#             case 2:
#                 mostrar_productos(productos)
#             case 3:
#                 actualizar_producto(productos)
#             case 4:
#                 borrar_productos(productos)
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, ingresa una opcion valida")
#     except Exception:
#         print("Error.")
