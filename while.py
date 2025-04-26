# Explicacion y uso del while

# # intentos infinitos
# clave = 123
# intentos = 0
# password = int(input("Introduce la clave: "))
# while clave != password:
#     print("Clave incorrecta, vuelve a intentarlo")
#     intentos = intentos + 1
#     password = int(input("Introduce la clave: "))

# if intentos <=3:
#     print("Has superado el maximo de intentos")

#     print("Clave correcta! Binevenido")


#clave 3 intentos maximos 
 
clave = 123
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    password = int(input("Introduce la clave: "))
    if password == clave:
        print("¡Clave correcta! Bienvenido")
        break
    else:
        print("Clave incorrecta, vuelve a intentarlo")
        intentos += 1

if intentos == max_intentos:
    print("Has superado el máximo de intentos")

