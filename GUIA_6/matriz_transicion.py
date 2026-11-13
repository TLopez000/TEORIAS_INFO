# Las filas son las entradas y las columnas las salidas 
# M[i,j] es la probabilidad de que salga j si entro i
# La función calcula la matriz de canal de la siguiente manera:
#1. Obtiene los símbolos únicos de entrada y salida.
#2. Crea una matriz de ceros, donde las filas son los símbolos de entrada y las columnas los de salida.
#3. Recorre ambas secuencias simultáneamente y cuenta cuántas veces aparece cada par entrada-salida.
#4. Divide cada valor de la fila por la cantidad de veces que aparece ese símbolo de entrada.
#Resultado: obtiene las probabilidades condicionadas \(P(\text{salida} \mid \text{entrada})\), formando la matriz de transición del canal.

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

#M(AC) = M(AB) * M(BC)
#La funcion calcula la matriz compuesta por el canal 1 M(AB) y el canal 2 M(BC).
#Primero se verifica la posibilidad de combinacion y luego se obtiene la matriz compuesta multiplicando las matrices de ambos canales 
#las probabilidades a priori del canal compuesto son las mismas que las del canal 1, porque ambos comienzan con la misma fuente A.
#lo que cambia al componer los canales son las probabilidades de transición (la matriz del canal), pero no la distribución inicial de los símbolos.
#Comparación de las matrices de canal
#- Canal 1 (A → B): permite analizar qué probabilidades tiene cada símbolo de entrada de convertirse en un símbolo intermedio.
#- Canal 2 (B → C): permite analizar cómo se comporta la segunda transmisión.
#- Canal compuesto (A → C): permite observar el resultado de atravesar ambos canales consecutivamente.
#2. Posibles conclusiones
#1. Pérdida de información: al atravesar dos canales, pueden acumularse errores de transmisión, haciendo que sea más difícil identificar el símbolo original.

#2. Mayor incertidumbre: el canal compuesto puede presentar distribuciones de salida más similares entre distintas entradas, dificultando distinguirlas.

#3. Un canal puede afectar más que otro: si uno de los canales introduce más errores o incertidumbre, puede tener mayor influencia en el resultado final.
#4. Propagación de errores: un error producido en el primer canal puede afectar también la salida del segundo.
#5. Conservación de la información: si ambos canales transmiten correctamente los símbolos, el canal compuesto también puede conservar la información original.
def obtener_matriz_canal_compuesto(matriz_canal_1, matriz_canal_2):
    cantidad_entradas = len(matriz_canal_1)
    cantidad_intermedios = len(matriz_canal_1[0])
    cantidad_salidas = len(matriz_canal_2[0])
    if cantidad_intermedios != len(matriz_canal_2):
        raise ValueError("Las salidas del primer canal deben coincidir con las entradas del segundo")
    matriz_compuesta = [[0 for k in range(cantidad_salidas)] for i in range(cantidad_entradas)]
    for i in range(cantidad_entradas):
        for k in range(cantidad_salidas):
            for j in range(cantidad_intermedios):
                matriz_compuesta[i][k] += (matriz_canal_1[i][j] * matriz_canal_2[j][k])
    return matriz_compuesta

def imprimeMatriz(alf_entrada, alf_salida, matriz):
    print("    " + "  ".join(f"{simbolo}" for simbolo in alf_salida))
    for fila, simbolo_entrada in zip(matriz, alf_entrada):
        print(f"{simbolo_entrada}: " + "  ".join(f"{valor}" for valor in fila))

def mostrar_matriz(matriz):
    # Recorre cada fila y muestra sus valores alineados en columnas.
    for fila in matriz:
        print(" | ".join(f"{valor:.4f}" for valor in fila))