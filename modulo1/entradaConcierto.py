# N°2 ejercicios para la prueba (Concierto)
# el usuario cuenta con descuentos por comprar su entrada con tarjetas 
# banco bci 30%, banco de chile 20%, banco falabella 25%
# cancha $100.000, galeria $150.000, vip 250.000 (Recargo por entrada $20.000) 
# preguntar cuantas entradas desea comprar
# y seleccionar con que banco va a pagar
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

    

print("Bienvenido al sistema de compra de entradas")
print("!-----------------------------------------!")
entradas = int(input("Cuantas entradas deseas comprar: "))

print("PROMOCION DESCUENTO PAGO CON TARJETA")
print("1.-BCI 30% - 2.-Banco de Chile 20% - 3.-Banco Falabella 25%")
banco = int(input("Elije el banco con el que pagas: "))

print("Elige tu sector de preferencia")
print("1.-Cancha $100.000")
print("2.-Galeria $150.000")
print("3.-Vip $250.000")
print("Recuerda el recargo por servicio es de $20.000")

sector = int(input("En que sector quieres estar (1, 2 o 3): "))

if sector == 1:
    precioSector = 100000 
elif sector== 2:
    precioSector = 150000 
elif sector == 3:
    precioSector = 250000
else:
    print("Opcion invalida")
    exit()
    
precioEntradas = precioSector +20000
precioTotal = entradas * precioEntradas


if banco == 1:
    desc = precioTotal * 0.3
elif banco == 2:
    desc = precioTotal * 0.2
elif banco == 3:
    desc = precioTotal * 0.25
else:
    print("opcion invalida")
    exit()
    
precioFinal = precioTotal - desc    

print("!-----------------------------------------!")
print(f"Usted lleva {entradas} entradas")
print(f"El descuento total es de ${desc}")
print(f"El total a pagar es de ${precioFinal}")
print("!-----------------------------------------!")