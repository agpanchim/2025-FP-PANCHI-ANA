# Matriz 3D: ciudades x semanas x días
# Ciudades, semanas
ciudades = ["Latacunga", "Guayaquil", "Puyo"]
semanas = ["Semana 1", "Semana 2"]

# Temperaturas promedio diarias (°C)
temperaturas = [
    [  # Latacunga
        [16, 17, 16, 15, 16, 17, 16],  # Semana 1
        [17, 18, 17, 16, 17, 18, 17]  # Semana 2
    ],
    [  # Guayaquil
        [28, 29, 28, 27, 28, 29, 28],  # Semana 1
        [29, 30, 29, 28, 29, 30, 29]  # Semana 2
    ],
    [  # Puyo
        [27, 28, 27, 26, 27, 28, 27],  # Semana 1
        [28, 29, 28, 27, 28, 29, 28]  # Semana 2
    ]
]
# bucles anidados
# Recorrido
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperaturas en {ciudad}:")

    for j, semana in enumerate(temperaturas[i]):
        promedio = sum(semana) / len(semana)
        print(f"  {semanas[j]} → {promedio:.2f}°C")
