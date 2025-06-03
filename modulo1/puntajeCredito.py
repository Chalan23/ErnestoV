# calcular el puntaje de credito 
# # debe calcular que tanto credito tiene una persona 
# # en cierta entidad financiera, debe considerar
# # cantidad de ingresos, nivel educacional y nacionalidad
# # cantidad de ingresos
# # 500.000 a 1.000.000 : 300.000
# # 1.000.000 a 1.500.000 : 650.000
# # 1.500.001 o mas : 1.000.000
# # nivel educacional
# # basico: 1x, medio: x1.3, superior: x1.5


# credito = 0
# nacionalidad = int(input("Ingrese nacionalidad (1 chileno, 2 extranjero): "))
# sueldo = int(input("Ingrese sueldo mensual: "))
# educacion = int(input("Ingrese educación (1 básico, 2 medio, 3 superior): "))

# if nacionalidad == 1:
#     credito = sueldo * 1.5
# elif nacionalidad == 2:
#     credito = sueldo * 1.3
# else:
#     credito = sueldo * 1.1


# if sueldo >= 500000 and sueldo <= 1000000:
#     credito += 300000
# elif sueldo > 1000000 and sueldo <= 1500000:
#     credito += 650000
# elif sueldo > 1500000:
#     credito += 1000000

# if educacion == 1:
#     credito *= 1
# elif educacion == 2:
#     credito *= 1.3
# elif educacion == 3:
#     credito *= 1.5
# else:
#     credito = 0

# print(f"El puntaje de crédito es {credito}")



