# prod_college=[
#     {"nombre":"goma", "precio":200},
#     {"nombre":"lapiz", "precio":400}
# ]
# ListProd=[
#     {"nombre":"zapato", "precio":20000},
#     {"nombre":"pelota", "precio":24000}
# ]

# def prod_sport(lista):
#     for producto in lista:
#         print(f"{producto['nombre']} - ${producto['precio']}")

# def mostrar_articulos(lista):
#     for n,p in enumerate(lista):
#         print(i+1,".-",p["nombre"], "$", p["precio"])


# def insertar(lista):
#     nom=input("Ingrese el numbre del producto: ")
#     pre=int(input("Ingrese el precio: "))
#     ListProd.insert(0,{"nombre":nom, "precio":pre})

# def actualiar(lista):
#     mostrar_articulos(prod_sport)
#     for numero, producto in enumerate(ListProd): 
#         print(numero+1, ".-", producto["nombre"], "$", producto["precio"])
#     op=int(input("Seleccionar una opcion: "))   
#     print("Productos actualizados")
#     print(ListProd[op-1])
#     nn=input("Ingrese nuevo nombre: ")
#     np=int(input("Ingrese nuevo precio: "))
#     ListProd[op-1]["nombre"]=nn
#     ListProd[op-1]["precio"]=np

# def borrar(lista):
#     for numero, producto in enumerate(ListProd): 
#         print(numero+1, ".-", producto["nombre"], "$", producto["precio"])
#         op=int(input("Seleccionar una opcion a borrar: "))
#         ListProd.pop(-1)


# ListProd[0]["nombre"]
# for i,p in enumerate(ListProd):
#     print(i+1,".-",p["nombre"], "$", p["precio"])


# def menu(listProd):
#     while True:
#         print("""
#             1.-Agregar productos
#             2.-Mostrar productos
#             3.-Actualizar productos
#             4.-Borrar productos
#             5.-Salir  
#     """)
#         op=int(input("Seleccionar una opcion: "))
#         match op:
#             case 1:
#                 insertar(listProd)
#             case 2:
#                 mostrar_articulos(listProd)
#             case 3:
#                 actualiar(listProd)
#             case 4:
#                 borrar(listProd)
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, opcion invalida")

# ------------------------------------------------------------------------------------

# # crear programa del siguiente diccionario

# personas={
#     1:{"nombre": "diego rivera",
#        "numeros": [12345678,87654321],
#        "estadoCivil": "casado",
#        "trabajando" : True,
#        "edad": 64},
#     2:{"nombre": "ernesto vilches",
#        "numeros": [12345678,87654321],
#        "estadoCivil": "soltero",
#        "trabajando" : False,
#        "edad": 32},
#     3:{"nombre": "cristiano ronaldo",
#        "numeros": [12345678,87654321],
#        "estadoCivil": "casado",
#        "trabajando" : True,
#        "edad": 35},
# }

# while True:
#     try:
#         print("""
#               1.-Ingresar persona
#               2.-consultar estado 
#               3.-Actualizar persona
#               4.-Borrar persona
#               5.-Salir
#               """)
#         op=int(input("seleccione una opcion: "))
#         match op:
#             case 1:
#                 nombre=input("ingrese el nombre: ")
#                 numero=int(input("ingrese el numero: "))
#                 estado=int(input("Estado civil 1.-casado - 2.-soltero: "))
#                 if estado==1:
#                     estadoCivil="casado"
#                 else:
#                     estadoCivil="soltero"
#                 edad=int(input("ingrese su edad: "))
#                 netxkey = len(personas) + 1
#                 personas[netxkey] = {
#                     "nombre": nombre,
#                     "numeros": [numero],
#                     "estadoCivil": estadoCivil,
#                     "trabajando": True,
#                     "edad": edad}
#             case 2:
#                 for key, val in personas.items():
#                     print(key, val)
#             case 3:
#                 for key, val in personas.items():
#                     print(key, val)
#                 pide = int(input("Ingrese el ID de la persona que desea actualizar: "))
#                 if pide in personas:
#                     nombre = input("Nuevo nombre (dejar vacío para mantener): ")
#                     numero = input("Nuevo número (dejar vacío para mantener): ")
#                     estado = input("Nuevo estado civil (1.-casado / 2.-soltero / dejar vacío para mantener): ")
#                     edad = input("Nueva edad (dejar vacío para mantener): ")
#                     trabajando = input("¿Está trabajando? s/n) :").lower()
#                     if nombre:
#                         personas[pide]["nombre"] = nombre
#                     if numero:
#                         personas[pide]["numeros"] = [int(numero)]
#                     if estado == "1":
#                         personas[pide]["estadoCivil"] = "casado"
#                     elif estado == "2":
#                         personas[pide]["estadoCivil"] = "soltero"
#                     if edad:
#                         personas[pide]["edad"] = int(edad)
#                     if trabajando == "s":
#                         personas[pide]["trabajando"] = True
#                     elif trabajando == "n":
#                         personas[pide]["trabajando"] = False
#                 else:
#                     print("ID no encontrado.")
#             case 4:
#                 for key, val in personas.items():
#                     print(key, val)
#                 dell = int(input("Seleccione cual desea borrar: "))
#                 if dell in personas:
#                     del personas[dell]
#                     print("Persona borrada")
#                 else:
#                     print("ID no encontrado")
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Error, opcion invalida")

#     except Exception as e:
#         print("Error")

