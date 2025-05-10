# # Un cine ofrece distintos tipos de entrada según la edad:
# # Si la persona tiene menos de 5 años, no puede ingresar.
# # Si tiene entre 5 y 12 años, paga entrada infantil: $2.000
# # Si tiene entre 13 y 64 años, paga entrada general: $4.000
# # Si tiene 65 años o más, paga entrada senior: $2.500
# # Escribe un programa que:
# # Pida al usuario su edad.
# # Imprima si puede entrar o no.
# # Si puede, muestre cuánto debe pagar.

# print("Bienvenido al cine")
# print("----------------------------------------------------------")
# print("Si eres menor de 5 años no puede ingresar")
# print("Si tienes entre 5 y 12 años. Valor entrada infantil $2.000")
# print("Si tiene entre 13 y 65 años. Valor entrada general $4.000 ")
# print("Si tiene 65 años o más. Valor entrada senior: $2.500")
# print("----------------------------------------------------------")

# edad = int(input("Que edad tienes?: "))
# if edad <= 5:
#     print("Lo sentimos no puedes ingresar")
# elif edad >= 6 and edad <= 12:
#     print("El valor de su entrada es de $2.000")
# elif edad >= 13 and edad <= 65:
#     print("El valor de su entrada es de $4.000")
# else:
#     print("El valor de su entrada es de $2.500")