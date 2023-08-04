import numpy as np
#crea un array de 100 elementos enteros aleatorios entre 0 y 10
a = np.random.randint(0, 10, 100)

# Encuentra los elementos que más se repiten y su frecuencia
valores_unicos, frecuencias = np.unique(a, return_counts=True)

# Encuentra el valor máximo de frecuencia
max_frecuencia = np.max(frecuencias)

# Encuentra los elementos que se repiten la misma cantidad de veces que el máximo
elementos_mas_repetidos = valores_unicos[frecuencias == max_frecuencia]

print("Array aleatorio:")
print(a)
print("\nValores únicos:")
print(valores_unicos)
print("\nFrecuencias:")
print(frecuencias)
print("\nElementos que más se repiten:")
print(elementos_mas_repetidos)
print("\nFrecuencia máxima:")
print(max_frecuencia)