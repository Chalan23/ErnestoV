# # En las listas se comienza por el numero cero 
# # Ejemplo si aqui quiero llamar al numero 1 de mi lista tengo que llamar al cero
# # asi se imprimira en pantalla el numero 1 
# # tengop que llamar la lista de numeros y entre corchetes poner el numero que deseo llamar 
# # en este caso quiero llamar al 1 por lo tango ingreso 0
# # Ejemplo 1 

# numeros = [1,2,3,4,5]

# print (numeros[0])

# ---------------------------------------------------------------------------------------------------------
# # Se pueden llamar varias listas las cuales se imprimiran juntos 
# # esto se hace de la siguiente manera.
# # aqui podemos ver que las listas se imprimieron juntas del 1 al 10 
# # Ejemplo 2 

# numeros = [1,2,3,4,5]
# numeros2 = [5,7,8,9,10]

# print (numeros + numeros2)

# ---------------------------------------------------------------------------------------------------------
# # Tambien podemos ver cuantos elementos tiene una lista. 
# # esto se puede ver con la funcion len
# # luego en consola me muestra que tengo 10 elementos en la lista numeros2
# # Ejemplo 3

# numeros = [1,2,3,4,5]
# numeros2 = [5,7,8,9,10,11,12,13,14,15]

# print (len(numeros2))

# ---------------------------------------------------------------------------------------------------------
# # Podemos preguntarle a una lista si tenemos un elemento dentro de ella
# # este se hace con el operador in donde me devuelve un True o False
# # aqui me fije que la lista te la entrega tal cual como se ve por ejemplo del 1 al 5
# # si llamo al 0 en mi lista que deberia ser el 1 como ya lo vimos antes me devuelve un falso
# # comprendo que este operador in toma literal la informacion que se ve en la lista 
# # Ejemplo 4

# numeros = [1,2,3,4,5]

# print (3 in numeros)

# ---------------------------------------------------------------------------------------------------------
# # Aqui vemos como poder modificar o cambiar un elemento de mi lista 
# # y se hace de la siguiente forma donde lo vemos aca abajo.

# listas = [1,2]
# listas[0] = 23 #Aqui vemos que yo llamo al numero 1 de mi lista y lo cambio por un numero 23

# print(listas)

# ---------------------------------------------------------------------------------------------------------
# # Tuplas y listas diferencias 
# # Aqui veremos un ejemplo de como son las tuplas y la diferencia que tienen con las listas 
# # las tuplas son inmutables esto quiere decir que no se pueden modificar 
# # las tuplas llevas parentecis y las listas corchetes
# # a diferencia de las tuplas nuestras listas si se pueden modificar 
# # Ejmplo 5

# tuplas = (1,2)
# listas = [1,2]
# listas[0] = 23 #Aqui vemos que yo llamo al numero 1 de mi lista y lo cambio por un numero 23

# print(tuplas) #aqui vemos en consola que se imprime la tuplas y listas mostrando 1,2 
# print(listas)

# ---------------------------------------------------------------------------------------------------------
