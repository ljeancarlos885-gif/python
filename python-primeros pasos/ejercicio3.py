
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


num_columnas = len(matriz[0])

for j in range(num_columnas):
    suma_columna = sum(fila[j] for fila in matriz)
    print(f"Suma de la columna {j + 1}: {suma_columna}")
