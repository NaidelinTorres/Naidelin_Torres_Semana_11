"""Programa 1 para realizar la busqueda en la Matriz"""
def buscar_numero(matriz, numero):
    """Función que busca un número en una matriz y devuelve su posición."""
    for fila in range(len(matriz)):  # Recorre filas
        for columna in range(len(matriz[fila])):  # Recorre columnas
            if matriz[fila][columna] == numero:
                return fila, columna # Retorno la posicion (fila , columna)
    return None # Retorna None si el valor no fue encontrado

# Definir una matriz de ejemplo (3x3)
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
