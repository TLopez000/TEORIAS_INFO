import math
import probabilidades

#Incertidumbre sobre el simbolo de salida (sin haber recibido entrada) -- H(A)
def entropia_a_priori(probabilidades_a_priori):
    entropia = 0
    for probabilidad in probabilidades_a_priori:
        if probabilidad > 0:
            entropia -= probabilidad * math.log2(probabilidad)
    return entropia

#Incertidumbre sobre el simbolo de entrada (habiendo recibido salida) -- H(A/Bj)
def entropia_a_posteriori(probabilidades_a_priori, matriz_transicion):
    cantidad_entradas = len(matriz_transicion)
    cantidad_salidas = len(matriz_transicion[0])
    entropias_a_posteriori = [0 for j in range(cantidad_salidas)]
    matriz_a_posteriori = probabilidades.obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_transicion)
    for j in range(cantidad_salidas):
        for i in range(cantidad_entradas):
            if (matriz_a_posteriori[i][j] > 0): 
                entropias_a_posteriori[j] += matriz_a_posteriori[i][j] * math.log(1 / matriz_a_posteriori[i][j], 2)
    return entropias_a_posteriori


# H(A/B) = ruido o equivocacion
def obtener_ruido(probabilidades_a_priori, matriz_canal):
    cantidad_salidas = len(matriz_canal[0])
    probabilidades_salida = probabilidades.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
    entropias_a_posteriori = entropia_a_posteriori(probabilidades_a_priori, matriz_canal)
    ruido = 0
    for j in range(cantidad_salidas):
        ruido += probabilidades_salida[j] * entropias_a_posteriori[j]
    return ruido

# H(B/A) = perdida
def obtener_perdida(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    perdida = 0
    for i in range(cantidad_entradas):
        entropia_fila = 0
        for j in range(cantidad_salidas):
            p = matriz_canal[i][j]
            if p > 0:
                entropia_fila += p * math.log2(1 / p)
        perdida += probabilidades_a_priori[i] * entropia_fila
    return perdida

# I(A,B) = H(A) - H(A/B) (informacion sobre A que atraviesa con exito el canal)
def obtener_informacion_mutua(probabilidades_a_priori, matriz_canal):
    return entropia_a_priori(probabilidades_a_priori) - obtener_ruido(probabilidades_a_priori, matriz_canal)

# H(A,B) = H(A) + H(B/A)
def obtener_entropia_afin(probabilidades_a_priori, matriz_canal):
    return entropia_a_priori(probabilidades_a_priori) + obtener_perdida(probabilidades_a_priori, matriz_canal)