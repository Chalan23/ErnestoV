# Tarea
# Crear programa de manejo de notas
# 1.- Ingresar nota
# 2.- Borrar nota
# 3.- Mostar notas
# 4.- Sacar promedio, nota mayor y nota menor
# 5.- Limpiar todas las notas
# 6.- Salir

notas = []

while True:
    print("""
            1.- Ingresar nota
            2.- Borrar nota
            3.- Mostar notas
            4.- Sacar promedio, nota mayor y nota menor
            5.- Limpiar todas las notas
            6.- Salir
        """)
    opcion = int(input("Ingresa una opcion: "))
    match opcion:
        case 1:
            nota = float(input("Ingresa una nota: "))
            notas.append(nota)
        case 2:
            nota = float(input("Ingresa la nota que quieres borrar: "))
            notas.remove(nota)
        case 3:
            print("Las notas que ingresaste son:")
            for nota in notas:
                print(nota)
        case 4:
            if notas:
                promedio = sum(notas) / len(notas)
                notaMayor = max(notas)
                notaMenor = min(notas)
                print(f"Promedio: {promedio}, Nota Mayor: {notaMayor}, Nota Menor: {notaMenor}")
            else:      
                print("No hay notas para calcular.")
        case 5:
            notas.clear()
            print("Todas las notas han sido eliminadas.")
        case 6:
            print("Saliendo...")
            break
        case _:
            print("Error, ingresa una opcion valida.")
