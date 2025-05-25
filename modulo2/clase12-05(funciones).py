# # funciones 

# def suma():
#     n1 = int(input("Ingrese el primer número: "))
#     n2 = int(input("Ingrese el segundo número: "))
#     print("la suma es",n1+n2)
    
# suma()

# op = int(input("selecione una opcion"))

#------------------------------------------------------------------------#

# while True:
#     match op:
#         case 1:
#             print("opcion 1")
#         case 2:
#             print("opcion 2")
#         case 3:
#             print("opcion 3")
            
#         case 4:
#             print("opcion 4")
#             break
#         case _:
#             print("opcion no valida")

#------------------------------------------------------------------------#


# def suma():
#     n1 = int(input("Ingrese el primer número: "))
#     n2 = int(input("Ingrese el segundo número: "))
#     print("la suma es",n1+n2)
    
# def resta():
#     n1 = int(input("Ingrese el primer número: "))
#     n2 = int(input("Ingrese el segundo número: "))
#     print("la resta es",n1-n2)
    
# def multiplicacion():
#     n1 = int(input("Ingrese el primer número: "))
#     n2 = int(input("Ingrese el segundo número: "))
#     print("la multiplicacion es",n1*n2)
    
# def division():
#     try:
#         n1 = int(input("Ingrese el primer número: "))
#         n2 = int(input("Ingrese el segundo número: "))
#         print("la division es",n1/n2)
#     except ZeroDivisionError:
#         print("No se puede dividir entre cero")
    

# def calcu():
#     while True:
#         op = int(input('''
#                     1.Suma
#                     2.Resta
#                     3.Multiplicacion
#                     4.Division
#                     5.Salir'''))
#         match op: 
#             case 1:
#                 print("Suma")
#                 suma()
#             case 2:
#                 print("Resta")
#                 resta()
#             case 3:
#                 print("Multiplicacion")
#                 multiplicacion()
#             case 4:
#                 print("Division")
#                 division()
#             case 5:
#                 print("Salir")
#                 break         
# calcu()  


# tarea 
# realizar un programa que realice match y llame a otras 3 funciones. 
# Estas funciones deben incluir 
# if elif else, for y/o while 
# el programa debe ser recursivo   


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



