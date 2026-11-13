import math, matriz_transicion

#Reduccion suficiente: Cualquiera que sean las probabilidades del alfabeto de entrada, las informaciones mutuas del canal original y el reducido serían idénticas. 
#Comprueba que los índices de las columnas sean válidos y que sean diferentes.
#Suma los valores de cada columna.
#Si alguna columna suma cero, devuelve True, porque representa una salida imposible.
#Divide cada elemento de ambas columnas por la suma correspondiente, normalizando sus valores.
#Compara los valores normalizados de ambas columnas.
#Si todos coinciden (con una tolerancia de \(10^{-10}\)), devuelve True; si alguno es diferente, devuelve False.
#verifica si dos símbolos de salida tienen el mismo comportamiento probabilístico respecto de las entradas. Si es así, se pueden agrupar sin perder información.                   

def verificar_reduccion_suficiente(matriz_canal, columna_1, columna_2):

    cantidad_columnas = len(matriz_canal[0])
    if not (0 <= columna_1 < cantidad_columnas and 0 <= columna_2 < cantidad_columnas):
        raise ValueError("Índice de columna fuera de rango")
    if columna_1 == columna_2:
        raise ValueError("Se deben seleccionar dos columnas distintas")
    suma_1 = sum(fila[columna_1] for fila in matriz_canal)
    suma_2 = sum(fila[columna_2] for fila in matriz_canal)
    # Una columna nula representa una salida imposible.
    # Se puede agrupar con otra sin perder información.
    if suma_1 == 0 or suma_2 == 0:
        return True
    for fila in matriz_canal:
        valor_1 = fila[columna_1] / suma_1
        valor_2 = fila[columna_2] / suma_2
        if not math.isclose(valor_1, valor_2, abs_tol=1e-10):
            return False
    return True


# Verifica que las dos columnas se puedan agrupar sin perder información.
# Identifica cuál tiene el índice menor y cuál el mayor.
# Crea una matriz con una columna menos que la original.
# Recorre las salidas originales y asigna su nueva posición:
# - La primera columna conserva su posición.
# - La segunda se agrupa con la primera.
# - Las columnas posteriores se desplazan una posición a la izquierda.
# Coloca un 1 en la posición de destino de cada salida, indicando a qué
# nuevo símbolo se transforma.
# Devuelve la matriz del canal determinista.
#Canal determinista: canal sin perdida

def obtener_canal_determinista(matriz_canal, columna_1, columna_2):
    if not verificar_reduccion_suficiente(matriz_canal, columna_1, columna_2):
        raise ValueError("Las columnas no permiten una reducción suficiente")
    cantidad_salidas = len(matriz_canal[0])
    # Conservamos la posición de la primera y eliminamos la segunda.
    primera = min(columna_1, columna_2)
    segunda = max(columna_1, columna_2)
    matriz_determinista = [[0 for j in range(cantidad_salidas - 1)]for i in range(cantidad_salidas)]
    for i in range(cantidad_salidas):
        if i == segunda:
            destino = primera
        elif i > segunda:
            destino = i - 1
        else:
            destino = i
        matriz_determinista[i][destino] = 1
    return matriz_determinista


# Copia la matriz original para no modificarla.
# Busca pares de columnas que puedan agruparse sin perder información.
# Cuando encuentra un par, construye la matriz determinista que indica
# cómo agrupar las dos salidas.
# Multiplica la matriz actual por la matriz determinista para obtener
# el canal con una columna menos.
# Repite el procedimiento hasta que no encuentre más columnas que se puedan agrupar.
# Devuelve la matriz del canal reducido.
# El canal reducido es una matriz con menos símbolos de salida, agrupando aquellos que pueden unirse sin perder información.
def obtener_canal_reducido(matriz_canal):
    # Copiamos la matriz para no modificar la original.
    matriz_reducida = [fila[:] for fila in matriz_canal]
    hubo_reduccion = True
    while hubo_reduccion:
        hubo_reduccion = False
        cantidad_columnas = len(matriz_reducida[0])
        for columna_1 in range(cantidad_columnas):
            for columna_2 in range(columna_1 + 1, cantidad_columnas):
                if verificar_reduccion_suficiente(matriz_reducida, columna_1, columna_2):
                    matriz_determinista = obtener_canal_determinista(matriz_reducida, columna_1, columna_2)
                    matriz_reducida = matriz_transicion.obtener_matriz_canal_compuesto(matriz_reducida, matriz_determinista)
                    hubo_reduccion = True
                    break
            if hubo_reduccion:
                break
    return matriz_reducida