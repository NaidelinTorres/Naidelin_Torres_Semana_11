# Crear un diccionario con mi información personal
informacion_personal = {
    "nombre": "Naidelin Torres",
    "edad": 18,
    "ciudad": "La Joya de los Sachas",
    "profesion": "Estudiante"
}

# Se puede acceder y modificar la clave "ciudad"
informacion_personal["ciudad"] = "La Joya de los Sachas"

# Agregar una nueva clave-valor ("telefono" con mi numero personal)
informacion_personal["telefono"] = "0969286101"

# Verificamos si la clave "telefono" existe antes de agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0969286101"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)

