# # explicacion return
# def suma():
#     n1 = int(input("Ingrese un numero"))
#     n2 = int(input("Ingrese un numero"))
#     return n1+n2

# nume=suma()

# for i in range(nume):
#     print("hola")

# ----------------------------------------------------------------

# # crear un menu de carrito con las siguientes opciones
# # 1.- ingresar nombre del usuario 
# # 2.- comprar, poner productos para comprar 
# # con su precico correspondiente.
# # 3.- sacar boleta, calcular el precio neto 
# # y el precio mas IVA. Mostrar totales.
# # 4.- salir 

# # consideraciones:
# # por lo menos 3 productos 
# # no hay limite de compra 
# # se puede salir en cualquier momento 
# # los montos de los productos son fijos
 
print("Bienvenido al carrito de compras")
nombre = input("Ingrese su nombre: ")

def productos():
    print("carrito de compras")
    print("1.-Leche $1000")
    print("2.-Cereal $1500")
    print("3.-Jugo $800")
    print("4.-Salir")
    
def carrito():
    total=0
    while True:
        productos()
        print ("Que desea comprar?")
        op = int(input("Ingrese el número del producto que desea comprar: "))
        match op:
            case 1:
                total += 1000
                print(f"Subtotal es ${total}")
            case 2:
                total += 1500
                print(f"Subtotal es ${total}")
            case 3:
                total += 800
                print(f"Subtotal es ${total}")
            case 4:
                print("Saliendo del carrito de compras")
                break
            case _:
                print("No valido")
                
    print(f"Gracias por tu compra {nombre}")
    print(f"El valor neto es de: {total}")
    print(f"El total * IVA es de: {total*1.19}")
           
carrito()  
                
            
# ----------------------------------------------------------------          


# # promedios por cantidad de alumnos
# # pedir cantidad de alumnos
# # pedir notas por cada alumno
# # promediar por cada alumno 
# # mostrar si aprueba o reprueba 
# # bonus mostrar promedio de todos los alumnos
# # ingresados 

# # ej:
# # ingrese cantidad de alumnos: 5
# # ingrese cantidad de notas del alumno 1: 3
# # ingrese la nota 1 del alumno 1: 
# # ingrese la nota 2 del alumno 1: 
# # ingrese la nota 3 del alumno 1: 
# # el promedio del alumno 1 es : 5.6
# # el alumno 1 aprobo

# canAlumnos=int(input("Ingrese la cantidad de alumnos: "))


# for alumno in range(canAlumnos):
#     total=0
#     promedio = 0
#     print(f"Del alumno {alumno+1} ingrese la cantidad de notas")
#     canNotas=int(input())
#     for notas in range(canNotas):
#         print(f"Ingrese la nota {notas+1} del alumno {alumno+1}")
#         nota=float(input())
#         total+=nota
#         promedio=total/canNotas
#     print(f"El promedio de {alumno+1} es de {promedio}")
    
#     if promedio >=4.0:
#         print("Aprobado")
#     else:
#         print("Reprobado")        



    

        