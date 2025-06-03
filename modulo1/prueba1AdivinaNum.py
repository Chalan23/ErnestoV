import random

print("Juego de adivinar el numero")

numMenor = int(input("Ingrese el numero menor: "))
numMayor = int(input("Ingrese el numeroo mayor: "))

if numMenor >= numMayor:
    print("El numero menor debe ser mas bajo que el numero mayor")
else:
    numAleatorio = random.randint(numMenor, numMayor)
    intentos = 0
    intentosMax = 3

    while intentos < intentosMax:
        try:
            num = int(input(f"Intento {intentos + 1} - Adivina el número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")

        if num < numAleatorio:
            print("El número es mayor.")
        elif num > numAleatorio:
            print("El número es menor.")
        else:
            print("Felicidades!!! Adivinaste el número.")
            break

        intentos += 1

    if intentos == intentosMax and num != numAleatorio:
        print(f"Perdisteeee! el numero correcto era {numAleatorio}.")