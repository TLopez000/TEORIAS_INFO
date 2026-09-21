
from FuenteConMemoria import vector_estacionario_porColumnas, calcular_entropia_fuenteConMem_porColumnas

# Matriz P (convención por columnas)
P = [
    [1/2, 0, 0, 1/2],
    [1/2, 0, 0, 0],
    [0, 1/2, 0, 0],
    [0, 1/2, 1, 1/2],
]

# a. Vector estacionario
v = vector_estacionario_porColumnas(P)
print("Vector Estacionario (v):", v)

# b. Entropía de la fuente
H = calcular_entropia_fuenteConMem_porColumnas(v, P)
print(f"\nEntropía de la fuente H(S): {H:.4f} bits/símbolo")