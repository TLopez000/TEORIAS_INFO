import entropias
import probabilidades, matriz_transicion
from matriz_transicion import imprimeMatriz, obtener_matriz_canal

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

alfabeto_entrada, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada)
alfabeto_entrada, alfabeto_salida, matriz_transicion = obtener_matriz_canal(entrada, salida)

entropia_a_priori = entropias.entropia_a_priori(probabilidades_a_priori)                                          
entropias_a_posteriori = entropias.entropia_a_posteriori(probabilidades_a_priori, matriz_transicion)


print("Entropía a priori:", entropia_a_priori)
print("Entropías a posteriori:", entropias_a_posteriori)

entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"

alfabeto_entrada, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada)
alfabeto_entrada, alfabeto_salida, matriz_transicion = obtener_matriz_canal(entrada, salida)

entropia_a_priori = entropias.entropia_a_priori(probabilidades_a_priori)                                            
entropias_a_posteriori = entropias.entropia_a_posteriori(probabilidades_a_priori, matriz_transicion)


print("Entropía a priori:", entropia_a_priori)
print("Entropías a posteriori:", entropias_a_posteriori)

entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"

alfabeto_entrada, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada)
alfabeto_entrada, alfabeto_salida, matriz_transicion = obtener_matriz_canal(entrada, salida)

entropia_a_priori = entropias.entropia_a_priori(probabilidades_a_priori)                                            
entropias_a_posteriori = entropias.entropia_a_posteriori(probabilidades_a_priori, matriz_transicion)


print("Entropía a priori:", entropia_a_priori)
print(alfabeto_salida)
print("Entropías a posteriori:", entropias_a_posteriori)

probabilidades_a_priori = [0.3,0.3,0.4]
matriz_transicion = [[0.4,0.4,0.2], [0.3,0.2,0.5], [0.3,0.4,0.3]]

entropia_a_priori = entropias.entropia_a_priori(probabilidades_a_priori)
entropias_a_posteriori = entropias.entropia_a_posteriori(probabilidades_a_priori, matriz_transicion)

print("Entropía a priori:", entropia_a_priori)
print("Entropías a posteriori:", entropias_a_posteriori)
