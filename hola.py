# caracter = str
# entero = int
# real = bool
# logico = bool


# nombre="Ernesto"
# edad=32

# print ("hola", nombre, "su edad es", edad)

# # solicitu de datos 
# print("Ingrese su nombre")
# nombre=input()
# print("Ingrese su edad")
# edad=input()
# # ejemplo de concatenacion
# print ("hola", nombre, "su edad es", edad)

# n1=3
# n2=20

# print("su suma total es", n1+n2 )

##suma de dos numeros
# print("Ingrese dos numeros")
# n1=int(input())
# n2=int(input())

# print("su suma total es", n1+n2 )


# #ingresar 3 numeros y sacar el promedio 
# print("ingresa tus notas")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# prom=(n1+n2+n3)/3
# print("Su promeio es", prom )


# if  prom>=40:
#     print("El alumno aprobo")
# else:
#     print("El alumno reprobo")

#pedir edad al usuario y determinar si es mayor de edad.


# edad=int(input("Ingrese su edad "))

# if edad >=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted no es mayor de edad")

# # mostrar segun criterio 
# # menor de 12 años es niño
# # Entre 12 y 17 es adolescente 
# # entre 18 a 64 es adulto
# # 65 y mas es adulto mayor

# edad=int(input("Ingrese su edad "))

# if edad<12:
#     print("Usted es un niño")
# elif edad>=12 and edad<18:                    #convina else y if
#     print("Usted es adolescente")
# elif edad>=18 and edad<65:                    
#     print("Usted es adulto")  
# else:                  
#     print("Usted es un tatita")  

# ingresar 3 numeros y mostrar el mayor de los 3 

# print("ingrese numero 1") 
# n1=int(input())
# print("ingrese numero 2") 
# n2=int(input())
# print("ingrese numero 3") 
# n3=int(input())

# if n1>n2 and n1>n3:
#     print("El numero mayor es ", n1)
# elif n2>n1 and n2>n3:
#     print("El numero mayor es ", n2)
# else:
#     print("El numero mayor es ", n3)


# # Clave solo con numeros recordar anteponer int antes del input para señal que es un integer (numero entero)

# claveCorrecta = 1234

# claveUsuario = int(input("Ingrese su contraseña de cuatro numeros: "))

# if claveUsuario == claveCorrecta:
#     print("Acceso correcto")
    
# else:
#     print("Contraseña incorrecta")



# # Clave con palabra y numeros debe ir entre comillas " " ya que es un str string "una cadena de texto"
# claveCorrecta = "clave1234"

# claveUsuario = input("Ingrese su clave alfanumerica: ")

# if claveUsuario == claveCorrecta:
#     print("Acceso correcto")

# else: 
#     print("Contraseña incorrecta")



# Clave con 3 intentos maximos y se bloquea el acceso uso del while (control de flujo)
claveCorrecta = 1123
intentos = 0 
IntentosMax = 3

print("Tienes 3 oportunidades para ingresar bien tu contraseña si fallas formateo tu pc! QUE COMIENCE EL JUEGO! ")

while intentos < IntentosMax:
    claveUsuario = int(input("Ingrese su clave: "))

    if claveUsuario == claveCorrecta: 
        print ("Acceso correcto, Felicidades, TE SALVASTE JUEGATE UN LOTO!")
        break #(sirve para salir del bucle)
    else:
        intentos += 1
        print("contraseña incorrecta!!!! Te quedan ", intentos, "de ", IntentosMax)

if intentos == IntentosMax:
    print("Cagaste su pc se va formatear en 3...2...1...0")


