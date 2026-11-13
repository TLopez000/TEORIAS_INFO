import entropias, probabilidades, matriz_transicion

# Primer canal: entradas equiprobables
probabilidades_a_priori_c1 = [1/2, 1/2]
matriz_canal_1 = [
    [0.7, 0.0, 0.3, 0.0],
    [0.2, 0.6, 0.0, 0.2]
]

matriz_canal_2 = [
    [0.9, 0.0, 0.1],
    [0.0, 1.0, 0.0],
    [0.1, 0.1, 0.8],
    [0.0, 0.5, 0.5]
]

# Las entradas del segundo canal son las salidas del primero
probabilidades_a_priori_c2 = probabilidades.obtener_probabilidades_salida(probabilidades_a_priori_c1, matriz_canal_1)

# CANAL 1
print("Equivocacion: ", entropias.obtener_ruido(probabilidades_a_priori_c1, matriz_canal_1))
print("Info mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori_c1,matriz_canal_1) )

# CANAL 2
print("Equivocacion: ", entropias.obtener_ruido(probabilidades_a_priori_c2, matriz_canal_2))
print("Info mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori_c2,matriz_canal_2) )

matriz_compuesta = matriz_transicion.obtener_matriz_canal_compuesto(matriz_canal_1,matriz_canal_2)
matriz_transicion.imprimeMatriz([""," "],[""],matriz_compuesta)
probabilidades_a_priori_compuesto = probabilidades_a_priori_c1

# CANAL COMPUESTO
print("Equivocacion: ", entropias.obtener_ruido(probabilidades_a_priori_compuesto, matriz_compuesta))
print("Info mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori_compuesto, matriz_compuesta))