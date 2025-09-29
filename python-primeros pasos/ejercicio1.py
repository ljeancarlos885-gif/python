
n = int(input("Ingrese el número de elementos del array: "))

array = []
for i in range(n):
    if i % 2 == 0:
        array.append(0)  # Posición par
    else:
        array.append(1)  # Posición impar

print("Array resultante:", array)
