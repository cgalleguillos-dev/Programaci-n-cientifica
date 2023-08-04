import numpy as np
from show_resources import get_resource_info

# Implementación con fors anidados para la multiplicación de matrices
def matrix_multiplication_nested():
    matriz_a = [[i for i in range(1000)] for j in range(1000)]
    matriz_b = [[j for i in range(1000)] for j in range(1000)]
    resultado = [[0 for i in range(1000)] for j in range(1000)]

    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado

# Implementación optimizada con NumPy para la multiplicación de matrices
def matrix_multiplication_optimized():
    matriz_a = np.random.rand(1000, 1000)
    matriz_b = np.random.rand(1000, 1000)
    resultado = np.dot(matriz_a, matriz_b)

    return resultado


# Medir recursos para la función matrix_multiplication_nested
print("Medición de recursos para la función matrix_multiplication_nested")
get_resource_info(matrix_multiplication_nested)

# Medir recursos para la función matrix_multiplication_optimized
print("Medición de recursos para la función matrix_multiplication_optimized")
get_resource_info(matrix_multiplication_optimized)