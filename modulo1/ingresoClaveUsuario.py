print("Crear usuario")
user = input("Ingresa tu nombre: ").lower()
clave = int(input("Ingresa tu clave (número): "))

print("!-----------------------------------------!")
print("Inicia sesión")

usuario = input("Ingresa tu nombre: ").lower()
contraseña = int(input("Ingresa tu clave: "))

while usuario != user or contraseña != clave:
    print("Nombre de usuario o clave incorrectos. Intenta de nuevo.")
    usuario = input("Ingresa tu nombre: ").lower()
    contraseña = int(input("Ingresa tu clave: "))

print("¡Inicio de sesión exitoso!")