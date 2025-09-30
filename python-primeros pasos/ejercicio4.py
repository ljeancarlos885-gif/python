
matriz = [
    [3, 5, 1, 8],
    [7, 2, 9, 4],
    [6, 0, 3, 5]
]

for i, fila in enumerate(matriz):
    menor = min(fila)
    mayor = max(fila)
    print(f"Fila {i + 1}: menor = {menor}, mayor = {mayor}")
