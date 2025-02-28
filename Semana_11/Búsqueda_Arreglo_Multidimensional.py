
def buscar_numero(matriz, numero):
    """Función que busca un número en una matriz y devuelve su posición."""
    posiciones = []

    for i in range(len(matriz)):  # Recorre filas
        for j in range(len(matriz[i])):  # Recorre columnas
            if matriz[i][j] == numero:
                posiciones.append((i, j))  # Guarda la posición encontrada

    return posiciones


# Definir una matriz de ejemplo
matriz = [
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [50, 55, 60, 65]
]

# Mostrar la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

# Pedir número al usuario
numero_buscar = int(input("\nIngrese el número que desea buscar: "))

# Buscar el número en la matriz
resultado = buscar_numero(matriz, numero_buscar)

# Mostrar el resultado
if resultado:
    print(f"\nEl número {numero_buscar} se encontró en las posiciones: {resultado}")
else:
    print(f"\nEl número {numero_buscar} no está en la matriz.")
