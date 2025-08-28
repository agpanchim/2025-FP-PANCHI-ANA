# programa_busqueda_3d.py

# Matriz tridimensional 3x3x3
matriz = [
    [
        [5, 8, 2],
        [9, 1, 6],
        [4, 7, 3]
    ],
    [
        [12, 14, 11],
        [19, 10, 16],
        [13, 17, 15]
    ],
    [
        [22, 25, 21],
        [29, 20, 26],
        [24, 27, 23]
    ]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            for k in range(len(matriz[i][j])):
                if matriz[i][j][k] == valor:
                    return (i, j, k)
    return None

# Valor a buscar
valor = int(input("Ingrese el valor a BUSCAR en la matriz 3D: "))

resultado = buscar_valor(matriz, valor)

if resultado:
    print(f"Valor {valor} encontrado en la posición: CAPA {resultado[0]}, FILA {resultado[1]}, COLUMNA {resultado[2]}")
else:
    print(f"Valor {valor} no se encontró en la matriz 3D.")