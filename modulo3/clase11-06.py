# elementos importantes a considerar

# append() pone un elemento al final de la lista
# sum() suma todos los elementos 
# max() muestra los elementos meyores
# min() muestra los elementos nmenores
# len() muestra el largo del objeto, de las listas
# pop() elimina un elemnto por indice
# remove() elimina un elemento por valor
# clear() limpia la lista completa
# insert() inserta un elemento en el indice indicado
# enumerate() enumera la lista con otros argumentos
# extend() agrega varios elementos a la lista
# sort() ordena la lista de mayor a menor
# reverse() voltea la lista

# -------------------------------------------------------------
# # explicacion enumerate
# notas =[4.5,6.6,7,5,7]

# for num, nota in enumerate(notas):
#     print(num+1, ".-", nota)

# n = int(input("Seleccione una nota: "))
# print("El usuario selecciono la nota", notas[n-1])

# -------------------------------------------------------------
# # Tarea
# # Crear programa de manejo de notas
# # 1.- Ingresar nota
# # 2.- Borrar nota
# # 3.- Mostar notas
# # 4.- Sacar promedio, nota mayor y nota menor
# # 5.- Limpiar todas las notas
# # 6.- Salir

notas = []

while True:
    try:
        print("""
                1.- Ingresar nota
                2.- Borrar nota
                3.- Mostar notas
                4.- Sacar promedio, nota mayor y nota menor
                5.- Limpiar todas las notas
                6.- Salir
            """)
        opcion = int(input("Ingresa una opcion: "))
        
    except Exception():
        print("Debe ingresar un numero valido")
        
    match opcion:
        case 1:
            nota = float(input("Ingresa una nota: "))
            notas.append(nota)
        case 2:
            for num, n in enumerate(notas): # sirve para enumerar elemntos
                print(num+1,".-",n) # sirve para enumerar elemntos
            nota = float(input("Ingresa la nota que quieres borrar: "))
            notas.remove(nota)
            notas.pop
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
                print("No hay notas para calcular")
        case 5:
            notas.clear()
            print("Todas las notas han sido eliminadas.")
        case 6:
            print("Saliendo del sistema")
            break
        case _:
            print("Error, ingresa una opcion valida.")

# -----------------------------------------------------------------


