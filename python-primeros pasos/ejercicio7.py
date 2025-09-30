
def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return [[matriz[i][j] for i in range(filas)] for j in range(columnas)]

def imprimir_matriz(matriz, titulo="Matriz"):
    print(f"\n{titulo}:")
    for fila in matriz:
        print(fila)

matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

matriz2_transpuesta = transponer(matriz2)

if len(matriz1) != len(matriz2_transpuesta) or len(matriz1[0]) != len(matriz2_transpuesta[0]):
    print("Error: Las matrices no tienen dimensiones compatibles para la suma.")
else:
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2_transpuesta[i][j]
            fila.append(suma)
        resultado.append(fila)

    imprimir_matriz(matriz1, "Matriz 1")
    imprimir_matriz(matriz2, "Matriz 2")
    imprimir_matriz(matriz2_transpuesta, "Transpuesta de Matriz 2")
    imprimir_matriz(resultado, "Resultado (Matriz 1 + Transpuesta de Matriz 2)")
