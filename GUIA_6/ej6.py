import matriz_transicion
import probabilidades

alfabeto_entrada = ['a', 'b', 'c']
alfabeto_salida = [1, 2, 3]
probabilidades_a_priori = [0.3, 0.3, 0.4]
matriz_canal = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]

probabilidades_salida = probabilidades.obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)
print(probabilidades_salida)

matriz_posteriori = probabilidades.obtener_probabilidades_a_posteriori(probabilidades_a_priori, matriz_canal)
matriz_transicion.imprimeMatriz(alfabeto_entrada, alfabeto_salida, matriz_posteriori)

matriz_simultaneos = probabilidades.obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)
matriz_transicion.imprimeMatriz(alfabeto_entrada, alfabeto_salida, matriz_simultaneos)