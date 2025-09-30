
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

filas = len(matriz)
columnas = len(matriz[0])

transpuesta = []

for j in range(columnas):
    nueva_fila = []
    for i in range(filas):
        nueva_fila.append(matriz[i][j])
    transpuesta.append(nueva_fila)

print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)
