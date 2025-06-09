# # tarea 
# # realizar un programa que realice match y llame a otras 3 funciones. 
# # Estas funciones deben incluir 
# # if elif else, for y/o while 
# # el programa debe ser recursivo   


def parImpar():
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        print("Su numero es par")
    else: 
        print("Su numero es impar")

def verEdad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Usted es mayor de edad")
    else: 
        print("Usted es menor de edad")

def verPromedio():
    nota1 = float(input("Ingrese su primera nota: "))
    nota2 = float(input("Ingrese su segunda nota: "))
    nota3 = float(input("Ingrese su tercera nota: "))
    
    promedio = (nota1+nota2+nota3)/3
    
    print(f"Su primedio total es de {promedio}")

def opcion():
    while True:
        op = int(input('''
                       Bienvenido al programa de verificacion.
                       #--------------------------------------#
                       1.-Verifica par e impar
                       2.-Verificar edad 
                       3.-Verificar tu promedio
                       4.-Salir
                       #--------------------------------------#
                       '''))
        match op:
            case 1:
                print("Verificar par e impar")
                parImpar()
            case 2:
                print("Verificar edad")
                verEdad()                            
            case 3:
                print("Verificar tu promedio")
                verPromedio()
            case _:
                print("Salir")
                break
opcion()    
