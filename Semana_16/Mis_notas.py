# Escritura de Archivo de Texto
# Abrimos o creamos el archivo Mis_notas en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("Mi nombre es Naidelin Torres")
archivo.write("En este dia estoy aprendiendo a trabajar con archivos de texto en Python.\n")
archivo.write("Estoy practicando y aprendiendo sobre la escritura y lectura de archivos.\n")
archivo.write("Es muy importante cerrar todos los archivos después de usarlos.\n")

# Cerramos el archivo después de escribir nuestras notas personales
archivo.close()

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el archivo línea por línea usando readline() en un bucle
print("Contenido del archivo:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # Usamos strip() para quitar el salto de línea al final
    linea = archivo.readline()

# Cerramos el archivo después de leer mis notas personales
archivo.close()


