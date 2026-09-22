import random
import math

def vector_estacionario_porColumnas(MT):
    n = len(MT)

    # A = MT - I
    A = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(MT[i][j] - 1)
            else:
                fila.append(MT[i][j])
        A.append(fila)

    # Reemplazamos una ecuación por:
    # v1 + v2 + ... + vn = 1
    A[n-1] = [1] * n
    b = [0] * (n - 1) + [1]

    # Eliminación
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]

            for k in range(n):
                A[j][k] -= factor * A[i][k]

            b[j] -= factor * b[i]

    # Sustitución hacia atrás
    v = [0] * n

    for i in range(n - 1, -1, -1):
        suma = 0

        for j in range(i + 1, n):
            suma += A[i][j] * v[j]

        v[i] = (b[i] - suma) / A[i][i]

    return v

#Se aplica M*V = V. Primero construyo en la matriz A construyo M-I (se resta 1 a la diagonal) y se plantea el sistema (M-I)*V = 0 
#Como este sistema es indeterminado, se reemplaza en A una de sus ecuaciones (su ultima fila) por la condición de normalizacion v1 + v2 + ... + vn = 1 (la ultima fila).
#Al vector de terminos independientes b se le asigna 0 en todas sus posiciones salvo en la ultima que se le asigna 1. Hasta aca se planteo A*V = b.
# Luego se resuelve el sistema por eliminación gaussiana para obtener el vector estacionario.


def calcular_entropia_fuenteConMem_porColumnas(vecEst, MatrizTrans):

    n = len(MatrizTrans)
    entropia_total = 0.0

    # Cada columna representa un estado de origen j
    for j in range(n):
        entropia_condicional = 0.0

        # Recorremos sus probabilidades condicionales
        for i in range(n):
            p = MatrizTrans[i][j]

            if p > 0:
                entropia_condicional += p * math.log2(1/p)

        # Ponderamos por la probabilidad estacionaria del estado j
        entropia_total += vecEst[j] * entropia_condicional

    return entropia_total

# Se recorre cada símbolo (columna) y se calcula su entropía condicional
# H(S|Sj) = sum_i Pji * log2(1/Pji).
# Luego, cada entropía condicional se pondera por la probabilidad estacionaria
# del símbolo de origen correspondiente y por ultimo se suman para obtener la entropía total de la fuente.


