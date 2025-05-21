import random
import time 

aleatorio = random.randint(1, 9)
print("Binvenido a la bola magica")
time.sleep(1)
pregunta = input("Que quieres saber... ")

if aleatorio == 1:
    respuesta = "Sí, definitivamente."
elif aleatorio == 2:
    respuesta = "Definitivamente así es."
elif aleatorio == 3:
    respuesta = "Sin duda."
elif aleatorio == 4:
    respuesta = "No lo se."
elif aleatorio == 5:
    respuesta = "Pregunta más tarde."
elif aleatorio == 6:
    respuesta = "Mejor no te lo digo ahora."
elif aleatorio == 7:
    respuesta = "Mis fuentes dicen que no."
elif aleatorio == 8:
    respuesta = "El pronóstico no es muy bueno."
elif aleatorio == 9:
    respuesta = "Muy dudoso."
else: 
    print("Respuesta confusa, inténtalo de nuevo.")
    
print("Dejame pensar!")
time.sleep(3)
print("mmmm... ")
time.sleep(1)
print("Creo que " + respuesta)
















