
N = int(input("Ingrese el número de alumnos: "))

alumnos = []

for i in range(N):
    print(f"\nAlumno {i + 1}:")
    notas = []
    for j in range(3):
        nota = float(input(f"  Ingrese calificación {j + 1}: "))
        notas.append(nota)
    alumnos.append(notas)

promedios = []
suma_total = 0

for i in range(N):
    promedio = sum(alumnos[i]) / 3
    promedios.append(promedio)
    suma_total += promedio
    print(f"Promedio del alumno {i + 1}: {promedio:.2f}")

# Paso 5: Calcular promedio general del grupo
promedio_grupo = suma_total / N
print(f"\nPromedio general del grupo: {promedio_grupo:.2f}")

# Paso 6: Encontrar alumno con mayor promedio
mayor_promedio = max(promedios)
indice_mayor = promedios.index(mayor_promedio)
print(f"El alumno con mayor promedio es el número {indice_mayor + 1} con {mayor_promedio:.2f}")
