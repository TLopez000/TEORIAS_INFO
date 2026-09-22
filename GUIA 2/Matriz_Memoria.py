import math

#La función primero obtiene la n cantidad de símbolos del alfabeto y crea una matriz nxn de conteos inicializada en cero. 
# Luego recorre el mensaje de a pares consecutivos, identificando el símbolo actual como origen (columna) y el siguiente como destino (fila), 
# e incrementa el contador de esa transición. Finalmente, recorre cada columna, calcula el total de transiciones que salen de ese símbolo y 
# divide cada contador por ese total para obtener las probabilidades. Así se obtiene una matriz de transición por columnas, donde cada columna 
# representa las probabilidades de pasar desde un símbolo de origen hacia los distintos destinos.

def obtener_matrizTrans_porColumnas(alfabeto, mensaje):
    n = len(alfabeto)

    # Matriz de conteos
    matriz = [[0 for j in range(n)] for i in range(n)]

    # Contar las transiciones
    for i in range(len(mensaje) - 1):
        actual = mensaje[i]
        siguiente = mensaje[i + 1]

        # Buscar la posición de cada símbolo
        for j in range(n):
            if alfabeto[j] == actual:
                columna = j

            if alfabeto[j] == siguiente:
                fila = j

        matriz[fila][columna] += 1

    # Convertir los conteos a probabilidades
    for j in range(n):
        total = 0

        for i in range(n):
            total += matriz[i][j]

        if total > 0:
            for i in range(n):
                matriz[i][j] = matriz[i][j] / total

    return matriz


#Comparo cada valor maximo de cada fila con su valor minimo,
#si para algún simbolo la diferencia va más allá de la tolerancia, la aparición depende de la secuencia anterior y la fuente tiene memoria.

def tiene_memoria(matriz,  tolerancia):
    n = len(matriz)
    
    for i in range(n):
        max = 0
        min = 9999
        for j in range(n):
            if (matriz[i][j] > max):
                max = matriz[i][j]
            if (matriz[i][j] < min):
                min = matriz[i][j]
                
        diferencia = max - min

        if diferencia > tolerancia:
            return True

    return False


def imprime_matriz(alfabeto,matriz):
    print("         ", alfabeto)
    for i in range(len(matriz)):
        print(f"{alfabeto[i]:^6}", end="")
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:^8.7f} ", end="")
        print()