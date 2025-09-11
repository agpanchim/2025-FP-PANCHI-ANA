# Función para calcular promedios de temperatura

def calcular_promedios(ciudades, semanas, dias, temperaturas):
    # Calcula y muestra el promedio de temperaturas por ciudad y semana
    print("\nPromedio de temperaturas por ciudad y semana:")

    for i, ciudad in enumerate(ciudades):  # Recorremos cada ciudad
        print(f"\nPromedios de temperaturas en {ciudad}:")

        for j in range(len(semanas)):  # Recorremos cada semana
            suma = sum(temperaturas[i][j])  # suma de los 7 días
            promedio = suma / len(dias)
            print(f" {semanas[j]}: {promedio:.2f} °C")

# Matriz 3D: DATOS
ciudades = ["Latacunga", "Guayaquil", "Puyo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Temperaturas promedio diarias (°C)
temperaturas = [
    [  # Latacunga
        [16, 17, 16, 15, 16, 17, 16],  # Semana 1
        [17, 18, 17, 16, 17, 18, 17],  # Semana 2
        [18, 19, 18, 17, 18, 19, 18],  # Semana 3
        [19, 20, 19, 18, 19, 20, 19]   # Semana 4
    ],
    [  # Guayaquil
        [28, 29, 28, 27, 28, 29, 28],  # Semana 1
        [29, 30, 29, 28, 29, 30, 29],  # Semana 2
        [30, 31, 30, 29, 30, 31, 30],  # Semana 3
        [31, 32, 31, 30, 31, 32, 31]   # Semana 4
    ],
    [  # Puyo
        [27, 28, 27, 26, 27, 28, 27],  # Semana 1
        [28, 29, 28, 27, 28, 29, 28],  # Semana 2
        [29, 30, 29, 28, 29, 30, 29],  # Semana 3
        [30, 31, 30, 29, 30, 31, 30]   # Semana 4
    ]
]

# Ejecución de la función
calcular_promedios(ciudades, semanas, dias, temperaturas)