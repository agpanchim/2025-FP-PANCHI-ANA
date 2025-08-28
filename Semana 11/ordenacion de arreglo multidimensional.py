# programa_ordenacion_3d.py

# Arreglo tridimensional 3x3x3
array = [
    [[5, 8, 2],
     [9, 1, 6],
     [4, 7, 3]],

    [[12, 14, 11],
     [19, 10, 16],
     [13, 17, 15]],

    [[22, 25, 21],
     [29, 20, 26],
     [24, 27, 23]]
]

def bubble_sort(fila):
    """Ordena una fila en orden ascendente usando Bubble Sort"""
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Mostrar arreglo original
print("Arreglo 3D original:")
for capa_idx, capa in enumerate(array):
    print(f"Capa {capa_idx}:")
    for fila in capa:
        print(fila)
    print()

# Solicitar la capa a ordenar completamente
capa_idx = int(input("Ingrese el índice de la capa a ordenar (0-2): "))

# Validar índice y ordenar toda la capa
if 0 <= capa_idx < len(array):
    for fila_idx in range(len(array[capa_idx])):
        array[capa_idx][fila_idx] = bubble_sort(array[capa_idx][fila_idx])
    print("\nArreglo 3D Ordenado, la capa seleccionada:")
    for capa_idx, capa in enumerate(array):
        print(f"Capa {capa_idx}:")
        for fila in capa:
            print(fila)
        print()
else:
    print("Índice de capa inválido. Debe ser entre 0 y 2.")