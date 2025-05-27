# cine 
# preguntar al usuario cuantas entradas quieres 
# preguntar si quiere promo de cabritas + bebida 
# categoria de sala 
# categoria de genero de pelicula
# 3 peliculas por genero
# resumen de la compra en boletas 


total = 0

print("---Bienvenido al Cine---")
while True:
    try:
        entradas = int(input("Ingrese la cantidad de entradas que desea comprar: "))
        if entradas <= 0:
            print("Debe ingresar al menos una entrada.")
        break
    except Exception:
        print("Ingrese un número valido.")

print(""" 
Gracias por tu compra
Deseas llevar tu promo Box?
Llevas Cabritas + 2 bebidas por $5.000""")

while True:
    try:
        box = int(input("Le gustaría llevar el Box? (1.-Si / 2.-No): "))
        match box:
            case 1:
                total += 5000
                print("Llevas la promo Box")
                break
            case 2:
                print("Te perdiste la promo")
                break
            case _:
                print("Opción invalida")
    except Exception:
        print("Ingrese una opción válida.")

while True:
    try:
        print("""
Seleccione una categoría de sala:
1.-Sala Normal $5.000
2.-Sala Pro $10.000
3.-Sala Vip $15.000
""")
        sala = int(input("En que sala quieres ver tu pelicula? "))
        match sala:
            case 1:
                total += 5000 * entradas
                salaNombre = "Normal"
                break
            case 2:
                total += 10000 * entradas
                salaNombre = "Pro"
                break
            case 3:
                total += 15000 * entradas
                salaNombre = "Vip"
                break
            case _:
                print("Seleccione una opcion valida.")
    except Exception:
        print("Ingrese una opcion valida.")

while True:
    try:
        print("""
Seleccione un género:
1.-Terror
2.-Acción
3.-Comedia
""")
        genero = int(input("Que genero de pelicula prefieres? "))
        match genero:
            case 1:
                generoNombre = "Terror"
                break
            case 2:
                generoNombre = "Accion"
                break
            case 3:
                generoNombre = "Comedia"
                break
            case _:
                print("Seleccione una opción válida.")
    except Exception:
        print("Ingrese una opción válida.")

while True:
    try:
        if genero == 1:
            print("""
1.-IT
2.-La Llorona
3.-Annabel
""")
            pelicula = int(input("Qué pelicula quieres ver? "))
            match pelicula:
                case 1:
                    peliculaNombre = "IT"
                    break
                case 2:
                    peliculaNombre = "La Llorona"
                    break
                case 3:
                    peliculaNombre = "Annabel"
                    break
                case _:
                    print("Seleccione una opcion valida.")
        elif genero == 2:
            print("""
1.-Rapidos y Furiosos 23 en silla de ruedas
2.-Terminator
3.-Mision Imposible
""")
            pelicula = int(input("Que película quieres ver? "))
            match pelicula:
                case 1:
                    peliculaNombre = "Rapidos y Furiosos 23 en silla de ruedas"
                    break
                case 2:
                    peliculaNombre = "Terminator"
                    break
                case 3:
                    peliculaNombre = "Misión Imposible"
                    break
                case _:
                    print("Seleccione una opción válida.")
        elif genero == 3:
            print("""
1.-El Boxeador Manco
2.-El Mino Parlanchin
3.-El Payasito Plin-Plin
""")
            pelicula = int(input("Que película quieres ver? "))
            match pelicula:
                case 1:
                    peliculaNombre = "El Boxeador Manco"
                    break
                case 2:
                    peliculaNombre = "El Mino Parlanchin"
                    break
                case 3:
                    peliculaNombre = "El Payasito Plin-Plin"
                    break
                case _:
                    print("Seleccione una opción válida.")
    except Exception:
        print("Ingrese una opción válida.")

print("\n--- Resumen Boleta ---")
print(f"Entradas: {entradas}")
print(f"Sala: {salaNombre}")
print(f"Género: {generoNombre}")
print(f"Película: {peliculaNombre}")
print(f"Promo Box: {'Sí' if box == 1 else 'No'}")
print(f"Total a pagar: ${total}")
