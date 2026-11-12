import GUIA_6.matriz_transicion as matriz_transicion
import probabilidades

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"


## EJERCICIO 3 ##

entrada1 = "1101011001101010010101010100011111"
salida1 = "1001111111100011101101010111110110"

entrada2 = "110101100110101100110101100111110011"
salida2 = "110021102110022010220121122100112011"

alf_entrada, alf_salida, matriz = matriz_transicion.obtener_matriz_canal(entrada2, salida2)
matriz_transicion.imprimeMatriz(alf_entrada, alf_salida, matriz)

alfabeto_entrada, probabilidades_a_priori = probabilidades.obtener_probabilidades_a_priori(entrada2)
print(probabilidades_a_priori)