# Explicacion y uso del whil

# intentos infinitos
clave = 123
intentos = 0
password = int(input("Introduce la clave: "))
while clave != password:
    print("Clave incorrecta, vuelve a intentarlo")
    intentos = intentos + 1
    password = int(input("Introduce la clave: "))

if intentos >=3:
    print("Has superado el maximo de intentos")

    print("Clave correcta! Binevenido")
