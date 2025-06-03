# # Clave solo con numeros recordar anteponer int antes del input para señal que es un integer (numero entero)

# claveCorrecta = 1234

# claveUsuario = int(input("Ingrese su contraseña de cuatro numeros: "))

# if claveUsuario == claveCorrecta:
#     print("Acceso correcto")
    
# else:
#     print("Contraseña incorrecta")

# --------------------------------------------------------------------------------------------------

# # Clave con palabra y numeros debe ir entre comillas " " ya que es un str string "una cadena de texto"
# claveCorrecta = "clave1234"

# claveUsuario = input("Ingrese su clave alfanumerica: ")

# if claveUsuario == claveCorrecta:
#     print("Acceso correcto")

# else: 
#     print("Contraseña incorrecta")

# --------------------------------------------------------------------------------------------------

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