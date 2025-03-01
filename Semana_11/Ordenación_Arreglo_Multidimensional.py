"""Programa 2 para realizar la ordenacion en la Matriz"""

def ordenar_matriz(matriz):
    """Función que ordena una matriz de forma ascendente."""
    filas = len(matriz)
    columnas = len(matriz[0])

    # Convertir la matriz en una lista
    lista = [elemento for fila in matriz for elemento in fila]

    # Ordenar la lista
    lista.sort()

    # Reconstruir la matriz con los valores ordenados
    matriz_ordenada = [lista[i * columnas:(i + 1) * columnas] for i in range(filas)]
    return matriz_ordenada

# Definir una matriz de ejemplo
matriz = [
    [30, 5, 20],
    [10, 25, 15],
    [40, 35, 50]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la matriz
matriz_ordenada = ordenar_matriz(matriz)

# Mostrar la matriz ordenada
print("\nMatriz ordenada:")
for fila in matriz_ordenada:
    print(fila)
