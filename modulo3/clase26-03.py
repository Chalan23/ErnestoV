# # repaso preba 

# # validaciones 
# # validar si un texto tiene por lo menos 3 numeros 

# texto = "DarkLink128"
# cantidad_numeros=0

# for p in texto:
#     print(p)
#     if p.isdigit():
#         print("Es digito")
#         cantidad_numeros+=1
# if cantidad_numeros >= 3:
#     print("La cantidad de numeros es", cantidad_numeros)
#     print("La palabra cumple con el parametro")
# else:
#     print("La cantidad de numeros es", cantidad_numeros)
#     print("La palabra no cumple con el parametro")

# ------------------------------------------------------------------------

# anio=1985

# print(len(str(anio)))

# if len(str(anio)) == 4:
#     print("Tiene largo de 4")

# -------------------------------------------------------------------------









# creacion de contraseña
# debe tener 3 mayusculas 1 minuscula
# un signo # y 3 numeros.

# def validar_pass(clave):
#     mayusculas = 0
#     minusculas = 0
#     numeros = 0
#     tiene_signo = False
#     for caracter in clave:
#         if caracter.isupper():
#             mayusculas += 1
#         elif caracter.islower():
#             minusculas += 1
#         elif caracter.isdigit():
#             numeros += 1
#         if caracter == "#":
#             tiene_signo = True
#     return mayusculas >= 3 and minusculas >= 1 and numeros >= 3 and tiene_signo


# while True:
#     try:
#         print("""---Menu simple---
#                     1.-Ingresar contraseña
#                     2.-Salir
#               """)
#         opcion=int(input("Elige una opcion: "))
#         match opcion:
#             case 1:
#                 validar_pass()
#             case 2:
#                 print("Saliendo...")
#                 break
#             case 1:
#                 clave_usuario = input("Ingrese su contraseña: ")
#                 if validar_pass(clave_usuario):
#                     print("Contraseña valida.")
#                 else:
#                     print("Contraseña invalida. Minimo debe tener 3 mayusculas, 1 minuscula, 3 numeros y el signo #")
#     except Exception as e:
#         print("Error")


# ----------------------------------------------------------------

# def valida_pass(pasword):
#     while True:
        
#         cMayusculas = 0
#         Cminisculas = 0
#         cNumeros = 0
#         tiene_gato = False

#         for l in password:
#             if l.isupper():
#                 cMayusculas+=1
#             if l.islower():
#                 Cminisculas+=1
#             if l.isdigit():
#                 cNumeros+=1
#             if l == "#":
#                 tiene_gato=True
                
#         if cMayusculas<3:
#             print("Debe tener al menos 3 letras en mayuscula")
#         elif Cminisculas<1:
#             print("Debe tener al menos 1 letras en minuscula")
#         elif cNumeros<3:
#             print("Debe tener al menos 3 numeros")
#         elif tiene_gato==False:
#             print("Debe incluir un caracter #")
#         else:
#             print("Contraseña creada")
#             return True
#         break
    
# pp = False
# while pp:
#     clave = input("Ingrese su contraseña ")

# valida_pass("supermario128")

# ------------------------------------------------------------------

# Ingreso de producto 
# diccionario para productos 
# code debe tener 2 mayusculas 
# 2 minusculas y 4 numeros.
# nombre debe tener 2 palabras
# precio debe ser entre 8000 y 100000

prods = {
    1:{"nombre":"Zelda TOTK",
        "precio": 80000,
        "code": "ZZKK1985"},
    2:{"nombre":" Fifa 25",
        "precio": 80000,
        "code": "FFFF25"}
}

def ingrese_perro(dict):
    nombre=input("Ingrese un nombre: ")
    while True:
        if valida_nombre(nombre):
            print("nombre correcto")
            break
        else:
            print("El nombre debe tener dos palabras")
    precio=input("Ingrese la precio: ")
    while True:
        if valida_precio(precio):
            print("Precio correcto")
            break
        else:
            print("El precio debe ser mayor a 8.000 y menor a 100.000")
        while True: 
            codigo=input("Ingrese su codigo: ")
            if valida_nombre(nombre):
                largo=list(dict.keys())[-1]
                dict[largo+1]={"nombre": nombre,
                            "precio": precio,
                            "codigo": codigo}
    else:
        print("El juego no pudo ser ingresado")
        # print("el paramatro de la clave no es correcto")
        # print('''
        # el codigo debe tener, una mayuscula, una minuscula, 
        # un numero y un largo exacto de 6''')


def valida_code(pasword):
    while True:
        
        cMayusculas = 0
        Cminisculas = 0
        cNumeros = 0
        tiene_gato = False
        for l in pasword:
            if l.isupper():
                cMayusculas+=1
            if l.islower():
                Cminisculas+=2
                cNumeros+=1
            if l == "#":
                tiene_gato=True
        if cMayusculas!=2:
            print("Debe tener al menos 3 letras en mayuscula")
        elif Cminisculas!=2:
            print("Debe tener al menos 1 letras en minuscula")
        elif cNumeros!=2:
            print("Debe tener al menos 3 numeros")
        elif tiene_gato!=4:
            print("Debe incluir un caracter #")
        else:
            print("Contraseña creada")
            return True

def mostrar_juegos(dict):
    for key, juegos in dict.items():
        print(key , juegos)

def valida_nombre(nombre):
    if " " not in nombre:
        print("Debe tener dos palabras")
        return False
    else:
        return True
    
def valida_precio(precio):
    if precio < 8000 and precio > 100000:
        print("Precio fuera de rango")
        return False
    else:
        return True

def mostrar_juegos(dict):
    for key, juedos in dict.items():


def borrar_perros(dict):
    mostrar_p(dict)
    borrar=int(input("Seleccione el perro a borrar: "))
    del dict[borrar]

while True:
    try:
        print("""
              1.-Registrar juegp
              2.-Actualizar juego
              3.-Mostrar juegos
              4.-Borrar perro
              5.-Salir
              """)
        op = int(input("Selecciona una opción: "))
        match op:
            case 1:
                ingresar_juegos(juegos)
            case 2:
                actualizar_juegos(juegos)
            case 3:
                mostrar_juegos(prods)
            case 4:
                borrar_juegos(juegos)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta.")
    except Exception as e:
        print("El error es:", e)


