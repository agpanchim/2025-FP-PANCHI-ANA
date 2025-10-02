# Trabajo con Archivos de Texto en Python

# Escritura de Archivo de Texto
# Crea el archivo 'my_notes.txt' en modo escritura ("w")
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Primera nota: \n Aprendiendo a trabajar con archivos en Python.\n \n")
    file.write("Segunda nota: \n'with open' facilita el manejo de archivos.\n \n")
    file.write("Tercera nota: \nSiempre cerrar los archivos después de usarlos.\n")

# Lectura de Archivo de Texto
# Abre el archivo en modo lectura ("r")
file = open("my_notes.txt", "r")

# Lee el contenido línea por línea usando readline()
print("")
print("Contenido del archivo my_notes.txt:\n")
linea = file.readline()
while linea:
    print(linea.strip())  # .strip() elimina saltos de línea extra
    linea = file.readline()

# Cierre de Archivo
file.close()
print("\nEl archivo ha sido cerrado correctamente.")