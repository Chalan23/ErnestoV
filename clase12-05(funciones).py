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


def suma():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    print("la suma es",n1+n2)
    
def resta():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    print("la resta es",n1-n2)
    
def multiplicacion():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    print("la multiplicacion es",n1*n2)
    
def division():
    try:
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print("la division es",n1/n2)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    

def calcu():
    while True:
        op = int(input('''
                    1.Suma
                    2.Resta
                    3.Multiplicacion
                    4.Division
                    5.Salir'''))
        match op: 
            case 1:
                print("Suma")
                suma()
            case 2:
                print("Resta")
                resta()
            case 3:
                print("Multiplicacion")
                multiplicacion()
            case 4:
                print("Division")
                division()
            case 5:
                print("Salir")
                break         
calcu()         
            
            
            
        
    