# MI DICCIONARIO

informacion_personal = {
    "Nombre": "Ana Panchi",
    "Edad": 35,
    "Ciudad": "Latacunga",
    "Profesion": "Estudiante"
}
# IMPRIMIR EL DICCIONARIO INICIAL

print("-----------------")
print("Diccionario inicial:")
print("-----------------")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# ACCESO Y MODIFICACION VALOR ASOCIADO A "Ciudad"
informacion_personal["Ciudad"] = "Quito"  # Cambiamos la ciudad a Guayaquil

# AGREGAR NUEVO VALOR (Universidad)
informacion_personal["Universidad"] = "Universidad Estatal Amazónica"  # Añadimos la universidad de la persona

# VERIFICACION DE TELEFONO EXISTE; si no, agregarla
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = ("0984242774")  # Número de teléfono

# VERIFICACION DE "Edad" Y ELIMINACION
informacion_personal.pop("Edad")  # Eliminamos la edad, no es necesaria

# IMPRIMIR EL DICCIONARIO FINAL
print("")
print("-----------------")
print("Diccionario final:")
print("-----------------")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")