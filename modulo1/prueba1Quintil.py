print("Programa beneficios subsidio")

quintil = int(input("Quintil (1,5) "))
empleado = input("Tiene trabajo (si/no) ").lower()
edad = int(input("Cual es su edad: "))

if quintil in (1,5):
    subsidio = 280000 if empleado else 350000
    bono = 60000
elif quintil == 3:
    subsidio = 200000 if empleado else 250000
    bono = 0
else:
    subsidio = 0
    bono = 0
    
if edad > 65:
    bono += 40000
    
print(f"Subsidio total es de ${subsidio + bono}")