
num_partidos = 15

equipos = []
resultados = []

print("Introduce los datos de la quiniela para una jornada:")

for i in range(num_partidos):
    print(f"\nPartido {i + 1}:")
    equipo1 = input("  Nombre del equipo local: ")
    equipo2 = input("  Nombre del equipo visitante: ")
    goles1 = int(input(f"  Goles de {equipo1}: "))
    goles2 = int(input(f"  Goles de {equipo2}: "))

    equipos.append([equipo1, equipo2])
    resultados.append([goles1, goles2])

print("\n--- Quiniela de la Jornada ---")
for i in range(num_partidos):
    eq1, eq2 = equipos[i]
    gol1, gol2 = resultados[i]
    signo = (
        "1" if gol1 > gol2 else
        "2" if gol2 > gol1 else
        "X"
    )
    print(f"{eq1} {gol1} - {gol2} {eq2}  --> {signo}")
    
    #para guardar todos los resultados de todas las jornadasde la temporada abria que añadir una
    #dimencion adicional
    #que represente cada jornada   
# Equipos[num_jornadas][15][2]
# Resultados[num_jornadas][15][2]
