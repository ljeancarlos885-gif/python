n = int(input("Ingrese el número de filas (n): "))
m = int(input("Ingrese el número de columnas (m): "))

matriz = []

suma_pares = 0
producto_impares = 1
impares = False  

print("Ingrese los elementos de la matriz:")
for i in range(n):
    fila = []
    for j in range(m):
        num = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(num)

        if num % 2 == 0:
            suma_pares += num
        else:
            producto_impares *= num
            hay_impares = True

    matriz.append(fila)

# Imprimir matriz (opcional)
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Mostrar resultados
print("\nSuma de números pares:", suma_pares)
if hay_impares:
    print("Producto de números impares:", producto_impares)
else:
    print("No hay números impares en la matriz.")
