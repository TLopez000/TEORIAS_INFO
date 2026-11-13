import tipocanal
import entropias

probabilidades_a_priori = [1/4, 1/4, 1/4, 1/4]
matriz_canal = [
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
]

print("Es un canal sin ruido: ", tipocanal.verifica_sin_ruido(matriz_canal))
print("Es un canal determinante: ", tipocanal.verifica_determinante(matriz_canal))
print("Ruido: ", entropias.obtener_ruido(probabilidades_a_priori, matriz_canal))
print("Perdida: ", entropias.obtener_perdida(probabilidades_a_priori, matriz_canal))
print("Informacion mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal))


probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 1.0, 0.0]
]

print("Es un canal sin ruido: ", tipocanal.verifica_sin_ruido(matriz_canal))
print("Es un canal determinante: ", tipocanal.verifica_determinante(matriz_canal))
print("Ruido: ", entropias.obtener_ruido(probabilidades_a_priori, matriz_canal))
print("Perdida: ", entropias.obtener_perdida(probabilidades_a_priori, matriz_canal))
print("Informacion mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal))


probabilidades_a_priori = [1/3, 1/3, 1/3]
matriz_canal = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]

print("Es un canal sin ruido: ", tipocanal.verifica_sin_ruido(matriz_canal))
print("Es un canal determinante: ", tipocanal.verifica_determinante(matriz_canal))
print("Ruido: ", entropias.obtener_ruido(probabilidades_a_priori, matriz_canal))
print("Perdida: ", entropias.obtener_perdida(probabilidades_a_priori, matriz_canal))
print("Informacion mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal))


probabilidades_a_priori = [1/4, 1/4, 1/4, 1/4]
matriz_canal = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

print("Es un canal sin ruido: ", tipocanal.verifica_sin_ruido(matriz_canal))
print("Es un canal determinante: ", tipocanal.verifica_determinante(matriz_canal))
print("Ruido: ", entropias.obtener_ruido(probabilidades_a_priori, matriz_canal))
print("Perdida: ", entropias.obtener_perdida(probabilidades_a_priori, matriz_canal))
print("Informacion mutua: ", entropias.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal))