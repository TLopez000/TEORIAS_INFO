# Las filas son las entradas y las columnas las salidas 
# M[i,j] es la probabilidad de que salga j si entro i
import probabilidades

def obtener_matriz_canal(entrada, salida):
    if len(entrada) != len(salida):
        raise ValueError("La entrada y la salida deben tener igual longitud")
    alfabeto_entrada, _ = probabilidades.obtener_probabilidades_a_priori(entrada)
    alfabeto_salida = []
    for simbolo in salida:
        if simbolo not in alfabeto_salida:
            alfabeto_salida.append(simbolo)
    matriz = [
        [0 for columna in alfabeto_salida]
        for fila in alfabeto_entrada
    ]
    # Cuento los pares entrada-salida
    for i in range(len(entrada)):
        fila = alfabeto_entrada.index(entrada[i])
        columna = alfabeto_salida.index(salida[i])
        matriz[fila][columna] += 1
    # Divido cada fila por la cantidad de su símbolo de entrada
    for fila in range(len(alfabeto_entrada)):
        cantidad = entrada.count(alfabeto_entrada[fila])
        for columna in range(len(alfabeto_salida)):
            matriz[fila][columna] /= cantidad
    return alfabeto_entrada, alfabeto_salida, matriz

def imprimeMatriz(alf_entrada, alf_salida, matriz):
    print("    " + "  ".join(f"{simbolo}" for simbolo in alf_salida))
    for fila, simbolo_entrada in zip(matriz, alf_entrada):
        print(f"{simbolo_entrada}: " + "  ".join(f"{valor}" for valor in fila))