# # N°1 ejercicios para la prueba (Cine)
# # pida al usuario selecionar categoria de sala del cine 
# # selecione una categoria de pelicula 
# # seleccionar pelicula 
# # preguntar si quiere llevar promocion de cabritas 
# # preguntar cuantas entradas desea llevar 
# print("Bienvenido al cine")
# print("Selecciona una categoria de sala de cine")
# print("1.-Sala Normal")
# print("2.-Sala 3D")
# print("3.-Sala Pro")

# sala = int(input("En que sala te gustaria disfrutar tu pelicula: "))

# print("Seleciona el numero la categoria de la pelicula que quieres ver")
# print("1.Terror")
# print("2.-Accion")
# print("3.-Comedia")

# catPelicula = int(input("Que genero de peliculas desea ver hoy: "))
# pelicula = ""

# if catPelicula == 1:
#     print("Peliculas de terror")
#     print("1.-It el payaso")
#     print("2.-La monja")
#     print("3.-El diablo en la tierra")
#     peli = int(input("Selecione una pelicula: "))
#     if peli == 1:
#         pelicula = "It el payaso"
#     elif peli == 2:
#         pelicula = "La monja"
#     elif peli == 3:
#         pelicula = "El diablo en la tierra"
#     else:
#         print("Opcion Invalida")
 
# elif catPelicula == 2:
#     print("Peliculas de accion")
#     print("1.-Rapidos y furiosos 23")
#     print("2.-El ultimo soldado")
#     print("3.-La pareja explosiva")
#     peli = int(input("Selecione una pelicula: "))
#     if peli == 1:
#         pelicula = "Rapidos y furiosos 23"
#     elif peli == 2:
#         pelicula = "El ultimo soldado"
#     elif peli == 3:
#         pelicula = "La pareja explosiva"
#     else:
#         print("Opcion Invalida") 
        
# elif catPelicula == 3:
#     print("Peliculas de comedia")
#     print("1.-Los corredores de la risa")
#     print("2.-El payaso fome")
#     print("3.-El mimo parlanchin")
#     peli = int(input("Selecione una pelicula: "))
#     if peli == 1:
#         pelicula = "Los corredores de la risa"
#     elif peli == 2:
#         pelicula = "El payaso fome"
#     elif peli == 3:
#         pelicula = "El mimo parlanchin"
#     else:
#         print("Opcion Invalida")    

# else:
#         print("Opcion invalida")

# promo = input("Deseas llevar cabritas Si/No: ").lower()

# entradas = int(input("Cuantas entradas deseas llevar (cantidad de entradas en numero): "))

# print("#---------------------------------------#")

# print(f"Pelicula seleccionada: {pelicula}")
# print(f"Llevas tu promo: {promo}")
# print(f"Total entradas: {entradas}")
