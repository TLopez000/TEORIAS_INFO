import entropias

probabilidades_a_priori1 = [2/5, 3/5]
matriz_canal1 = [
    [3/5, 2/5],
    [1/3, 2/3],
]

probabilidades_a_priori2 = [3/4, 1/4]
matriz_canal2 = [
    [2/3, 1/3],
    [1/10, 9/10],
]

entropia_a_priori1 = entropias.entropia_a_priori(probabilidades_a_priori1)
entropia_a_priori2 = entropias.entropia_a_priori(probabilidades_a_priori2)
entropias_a_posteriori1 = entropias.entropia_a_posteriori(probabilidades_a_priori1, matriz_canal1)
entropias_a_posteriori2 = entropias.entropia_a_posteriori(probabilidades_a_priori2, matriz_canal2)

print("Entropía a priori 1:", entropia_a_priori1)
print("Entropía a priori 2:", entropia_a_priori2)
print("Entropías a posteriori 1:", entropias_a_posteriori1)
print("Entropías a posteriori 2:", entropias_a_posteriori2)