num_conductores = int(input("Ingrese el número de conductores: "))
nombres = []
kms = []
total_kms = []

for i in range(num_conductores):
    nombre = input(f"Ingrese el nombre del conductor {i + 1}: ")
    nombres.append(nombre)
    
    kms_conductor = []
    print(f"Ingrese los kilómetros de {nombre} por cada día de la semana:")
    for dia in range(7):
        km = float(input(f"Día {dia + 1}: "))
        kms_conductor.append(km)
    
    kms.append(kms_conductor) 

for i in range(num_conductores):
    total = sum(kms[i])
    total_kms.append(total)

print("\n--- Resumen de kilómetros por conductor ---")
for i in range(num_conductores):
    print(f"{nombres[i]}: {total_kms[i]} km en la semana")
