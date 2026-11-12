import matriz_transicion
import probabilidades

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"

alf_entrada, alf_salida, matriz_canal = matriz_transicion.obtener_matriz_canal(entrada, salida)
_, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada)
probabilidades_a_posteriori = probabilidades.obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_canal)
probabilidades_simultaneos = probabilidades.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)

matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, probabilidades_a_posteriori)
matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, probabilidades_simultaneos)

print()


entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"

alf_entrada, alf_salida, matriz_canal = matriz_transicion.obtener_matriz_canal(entrada, salida)
_, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada)
probabilidades_a_posteriori = probabilidades.obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_canal)
probabilidades_simultaneos = probabilidades.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)

matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, probabilidades_a_posteriori)
matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, probabilidades_simultaneos)

print()


entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"

alf_entrada, alf_salida, matriz_canal = matriz_transicion.obtener_matriz_canal(entrada, salida)
_, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada)
probabilidades_a_posteriori = probabilidades.obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_canal)
probabilidades_simultaneos = probabilidades.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)

matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, probabilidades_a_posteriori)
matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, probabilidades_simultaneos)

print()