# # validaciones de datos 

# # verifico si el caracter @ existe dentro de mi variable

# # email = input("Ingrese su email: ")

# # if "@" in email:
# #     print("la variable tiene formato mail")
# # else:
# #     print("la variable no tiene formato mail")


# # while True:
# #     try:  
# #         pin = int(input("Ingrese su pin: "))
# #         break
# #     except Exception:
# #         print("Error, solo ingrese numeros")

# # # verifico que tenga al menos 5 caracteres
# # # la funcion len() verifica el largo de un objeto
# # # en este caso la variable es clave 

# # clave = input("Ingrese su clave")
# # if len(clave)>=5:
# #     print("La clave tiene el largo correcto")
# # else:
# #     print("La clave tiene que tener minimo 5 caracteres")

# # # ahora verificamos que tenga que tenga entre 5 a 12 caracteres
# # clave = input("Ingrese su clave")
# # if len(clave)>=5 and len(clave)<=12:
# #     print("La clave tiene el largo correcto")
# # else:
# #     print("La clave tiene que tener minimo 5 caracteres")

# # verifico si tiene mayusculas o minisculas 
# # y tiene por lo menos un numero
# clave = input("Ingresa tu clave")

# tieneMayusculas = False
# tieneMinusculas = False
# tieneNumero = False

# for letra in clave:
#     # verifico si la letra es mayuscula
#     if letra.isupper(): 
#         tieneMayusculas=True
#     # verifico si la letra es minuscula
#     if letra.islower():
#         tieneMinusculas=True
#     if letra.isdigit():
#         tieneNumero=True
        
# # # No es necesariio usar esto es mas que nada para que se vea el resultado
# # if tieneMayusculas:
# #     print("Tiene por lo menos una mayuscula")
# # else:
# #     print("NO tiene por lo menos una mayuscula")
    
# # if tieneMinusculas:
# #     print("Tiene por lo menos una mayuscula")
# # else:
# #     print("NO tiene por lo menos una mayuscula")
    
# if tieneMinusculas and tieneMayusculas and tieneNumero:
#     print("La clave esta ok")
# else:
#     print("Debe interntarlo de nuevo")
    
# especial="!@#$%^&*()_+[]{}"
# clave = "visa%"

# for caracter in clave:
#     if caracter in especial:
#         print("La clave tiene un caracter especial")
#         break


# --------------------------------------------------------------------------------
# # repaso listas y diccionarios.

# # perros de casa 

# def valida_pass(clave):
#     Mayuscula = False
#     Minuscula = False
#     Numero = False
#     for caracter in clave:
#         if caracter.isupper():
#             Mayuscula = True
#         if caracter.islower():
#             Minuscula = True
#         if caracter.isdigit():
#             Numero = True
#     if Mayuscula and Minuscula and Numero and len(clave) == 6:
#         print("La clave está bien escrita")
#         return True
#     else:
#         print("La clave está mal escrita")
#         return False

# perros = {
#     1: {"Nombre": "Droopy",
#         "raza": "Dog Hount",
#         "codigo": "Dphh06"},
#     2: {"Nombre": "Layka",
#         "raza": "poddle",
#         "codigo": "la23A1"}
# }

# def mostrar_perros(perros):
#     for key, perro in perros.items():
#         print(f"{key}: Nombre: {perro['Nombre']}, Raza: {perro['raza']}, Código: {perro['codigo']}")

# def ingresar_perro(perros):
#     nombre = input("Ingrese un nombre: ")
#     raza = input("Ingrese la raza: ")
#     while True:
#         codigo = input("Ingrese el código (6 caracteres, mayúscula, minúscula y número): ")
#         if valida_pass(codigo):
#             break
#         else:
#             print("El parámetro de la clave no es correcto. Intente de nuevo.")
#     if perros:
#         nuevo_id = max(perros.keys()) + 1
#     else:
#         nuevo_id = 1
#     perros[nuevo_id] = {"Nombre": nombre, "raza": raza, "codigo": codigo}
#     print("Perro registrado correctamente.")

# def actualizar_perro(perros):
#     mostrar_perros(perros)
#     try:
#         actualizar = int(input("¿Qué perro va a actualizar (número)? "))
#         if actualizar not in perros:
#             print("No existe ese perro.")
#             return
#         print("""
#               1.-Nombre
#               2.-Raza
#               3.-Código
#               """)
#         dato = int(input("¿Qué dato va a actualizar? "))
#         match dato:
#             case 1:
#                 n = input("Ingrese el nuevo nombre: ")
#                 perros[actualizar]["Nombre"] = n
#             case 2:
#                 n = input("Ingrese la nueva raza: ")
#                 perros[actualizar]["raza"] = n
#             case 3:
#                 while True:
#                     n = input("Ingrese el nuevo código: ")
#                     if valida_pass(n):
#                         perros[actualizar]["codigo"] = n
#                         break
#                     else:
#                         print("Código no válido. Intente de nuevo.")
#             case _:
#                 print("Opción incorrecta.")
#     except Exception as e:
#         print("Error al actualizar:", e)

# def borrar_perro(perros):
#     mostrar_perros(perros)
#     try:
#         borrar = int(input("Selecciona el perro que deseas borrar (número): "))
#         if borrar in perros:
#             del perros[borrar]
#             print("Perro borrado correctamente.")
#         else:
#             print("No existe ese perro.")
#     except Exception as e:
#         print("Error al borrar:", e)

# while True:
#     try:
#         print("""
#               1.-Registrar un perro
#               2.-Actualizar perro
#               3.-Mostrar perros
#               4.-Borrar perro
#               5.-Salir
#               """)
#         op = int(input("Selecciona una opción: "))
#         match op:
#             case 1:
#                 ingresar_perro(perros)
#             case 2:
#                 actualizar_perro(perros)
#             case 3:
#                 mostrar_perros(perros)
#             case 4:
#                 borrar_perro(perros)
#             case 5:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opción incorrecta.")
#     except Exception as e:
#         print("El error es:", e)
  
#-------------------------------------------------------------------------------------------------------
# # ejercicio realizado por el profe.
perros={
    1:{"nombre": "Droopy",
       "raza": "Dog Hount",
       "codigo": "Dphh06"},
    2:{"nombre": "Spike",
       "raza": "Bultierrer",
       "codigo": "BDil77"}
}

def mostrar_perros(dict):
    for key, perro in dict.items():
        print(key , perro)

def valida_pass(clave):
    Mayuscula=False 
    Minuscula=False
    Numero=False
    for palabra in clave:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Numero=True
    if Mayuscula and Minuscula and Numero and len(clave)==6:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

def ingrese_perro(dict):
    nombre=input("Ingrese un nombre: ")
    raza=input("Ingrese la raza: ")
    codigo=input("Ingrese su codigo: ")
    if valida_pass(codigo):
        largo=list(dict.keys())[-1]
        dict[largo+1]={"nombre": nombre,
                    "raza": raza,
                    "codigo": codigo}
    else:
        print("el paramatro de la clave no es correcto")
        print('''
        el codigo debe tener, una mayuscula, una minuscula, 
        un numero y un largo exacto de 6''')

def act_perros(dict):
    mostrar_perros(dict)
    act=int(input("Seleccione el perro a actulizar?: "))
    while True:
        print('''1.- Nombre
                2.- Raza
                3.- Codigo
                4.- Salir''')
        dato=int(input("que dato va a actualizar?: "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre")
                dict[act]["nombre"]=n
            case 2:
                n=input("ingrese la nueva raza")
                dict[act]["raza"]=n
            case 3:
                n=input("ingrese el nuevo codigo")
                if valida_pass(n):
                    dict[act]["codigo"]=n
                else:
                    print("el paramatro del codigo no es correcto")
                    print('''
                    el codigo debe tener, una mayuscula, una minuscula, 
                    un numero y un largo exacto de 6''')
            case 4:
                break
            case _:
                    print("Opcion invalida")

def borrar_perros(dict):
    mostrar_perros(dict)
    borrar=int(input("Seleccione el perro a borrar: "))
    del dict[borrar]

while True:
    try:
        print('''
              1.- Registrar un perro
              2.- Mostrar perros
              3.- Actualizar Perro
              4.- Borrar Perro
              5.- Salir
              ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingrese_perro(perros)
            case 2:
                mostrar_perros(perros)
            case 3:
                act_perros(perros)
            case 4 :
                borrar_perros(perros)
            case 5:
                print("Saliendo...")
                break
            case _:
                    print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)   





