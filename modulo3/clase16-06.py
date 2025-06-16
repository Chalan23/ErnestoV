# funciones 

# def suma():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     print(n1+n2)

# suma()

# ------------------------------------------------------------------
# def resta(n1,n2):
#     print(n1-n2)

# # resta(7,3)

# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# resta(num1,num2)  

# ------------------------------------------------------------------------------------------
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))

# def suma(n1,n2):
#     print(n1+n2)
# suma(num1,num2)

# def resta(n1,n2):
#     print(n1-n2)
# resta(num1,num2)

# def multiplicacion(n1,n2):
#     print(n1*n2)
# multiplicacion(num1,num2)

# def division(n1, n2):
#     print(n1 / n2)
# division(num1, num2)

# ------------------------------------------------------------------------------------------

# def sumaPrint():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     print(n1+n2) 



# def sumaReturn():
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))
#     return n1+n2

# sumaPrint()
# print(sumaReturn())

# ---------------------------------------------------------------------------------------------

# def promedio(x,y,z):
#     return (x+y+z)/3

# if promedio(40,70,22) >= 40:
#     print("El alumno aprobo")
# else:
#     print("El alumno reprobo")

# --------------------------------------------------------------------------------------------

# # crear un programa para calcular un descuento
# # pedir al usuario el precio y el descuento
# # que desea aplicar. mostrar total 

# def descuento():
#     precio = int(input("Ingrese el precio del producto: "))
#     descuento = int(input("Ingrese el descuento: "))
#     total = precio - (precio * descuento / 100)
#     print(f"El precio final con descuento es: {total}")

# descuento()

# # ej profe 
# def calcularDesc(precio, desc):
#     return precio*(desc/100)

# p=int(input("Ingrese el precio: "))
# d=int(input("Ingrese el descuento: "))
# miDesc=calcularDesc(p,d)

# print("El descuento es de ", miDesc)
# print("El total es de ", p - miDesc(p,d))

# ---------------------------------------------------------------------------------------

# ListProd=[
#     {"nombre":"zapato", "precio":20000},
#     {"nombre":"pelota", "precio":24000}
# ]

# # print(ListProd[0]["nombre"])
# # print(ListProd)
# # ListProd.append({"nombre":"paleta", "precio":14000})

# while True:
#     print("""
#         1.-Agregar productos
#         2.-Mostrar productos
#         3.-Actualizar productos
#         4.-Salir  
# """)
#     op=int(input("Seleccionar una opcion: "))
#     match op:
#         case 1:
#             nom=input("Ingrese el numbre del producto: ")
#             pre=int(input("Ingrese el precio: "))
#             ListProd.insert(0,{"nombre":nom, "precio":pre})
#         case 2:
#             for p in ListProd:
#                 print(p)
#         case 3:
#             for p in ListProd:
#                 print(p)
#                 nom=input("ingrese el nuevo nombre del producto: ")         
#                 pre=input("ingrese el nuevo precio del producto: ")
#                 p["nombre"] = nom
#                 p["precio"] = pre
#             print("Productos actualizados")
#         case 4:
#             print("Saliendo...")
#             break
#         case _:
#             print("Error, opcion invalida")




# ej: profe
ListProd=[
    {"nombre":"zapato", "precio":20000},
    {"nombre":"pelota", "precio":24000}
]

# print(ListProd[0]["nombre"])
# print(ListProd)
# ListProd.append({"nombre":"paleta", "precio":14000})

while True:
    print("""
        1.-Agregar productos
        2.-Mostrar productos
        3.-Actualizar productos
        4.-Borrar productos
        5.-Salir  
""")
    op=int(input("Seleccionar una opcion: "))
    match op:
        case 1:
            nom=input("Ingrese el numbre del producto: ")
            pre=int(input("Ingrese el precio: "))
            ListProd.insert(0,{"nombre":nom, "precio":pre})
        case 2:
            for p in ListProd:
                print(p)
        case 3:
            # for n, p in enumerate(ListProd): #ejemplo 1
            #     print(n+1, ".-", p)
            for i in range(len(ListProd)): #ejemplo 2
                print(i+1, ".-", ListProd[i])
            op=int(input("Seleccionar una opcion: "))   
            print("Productos actualizados")
            print(ListProd[op-1])
            nn=input("Ingrese nuevo nombre: ")
            np=int(input("Ingrese nuevo precio: "))
            ListProd[op-1]["nombre"]=nn
            ListProd[op-1]["precio"]=np
            print("Articulos actualizados")
        case 4:
            print("Saliendo...")
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Error, opcion invalida")
