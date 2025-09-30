
precios = []
print("Ingrese los precios de los 5 artículos:")
for i in range(5):
    precio = float(input(f"Precio del artículo {i + 1}: "))
    precios.append(precio)

ventas = []

for sucursal in range(4):
    print(f"\nIngrese las ventas para la sucursal {sucursal + 1}:")
    fila = []
    for articulo in range(5):
        cantidad = int(input(f"  Artículo {articulo + 1}: "))
        fila.append(cantidad)
    ventas.append(fila)

print("\nCantidad total vendida por artículo:")
for articulo in range(5):
    total_articulo = sum(ventas[sucursal][articulo] for sucursal in range(4))
    print(f"Artículo {articulo + 1}: {total_articulo} unidades")

total_sucursal_2 = sum(ventas[1])
print(f"\nCantidad total de artículos en la sucursal 2: {total_sucursal_2} unidades")

cantidad_art3_suc1 = ventas[0][2]
print(f"\nCantidad del artículo 3 en la sucursal 1: {cantidad_art3_suc1} unidades")

recaudaciones = []
print("\nRecaudación por sucursal:")
for sucursal in range(4):
    total = 0
    for articulo in range(5):
        total += ventas[sucursal][articulo] * precios[articulo]
    recaudaciones.append(total)
    print(f"Sucursal {sucursal + 1}: ${total:.2f}")
    
recaudacion_total = sum(recaudaciones)
print(f"\nRecaudación total de la empresa: ${recaudacion_total:.2f}")

mayor_recaudacion = max(recaudaciones)
indice_mayor = recaudaciones.index(mayor_recaudacion)
print(f"Sucursal con mayor recaudación: Sucursal {indice_mayor + 1} (${mayor_recaudacion:.2f})")
