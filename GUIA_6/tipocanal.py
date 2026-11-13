import math, entropias

#Un sin ruido tiene 1 solo elemento distinto de 0 en cada columna
#Al observar la salida, se conoce con certeza la entrada (0 ruido)
def verifica_sin_ruido(matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    for j in range(cantidad_salidas):
        elem_no_cero = False
        for i in range(cantidad_entradas):
            if (matriz_canal[i][j] > 0):
                if (elem_no_cero == False):
                    elem_no_cero = True
                else:
                    return False
    return True

#Un determinante tiene 1 solo elemento distinto de 0 en cada fila
#Toda la informacion generada por la fuente se recoge a la salida (0 perdida)
def verifica_determinante(matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    for i in range(cantidad_entradas):
        elem_no_cero = False
        for j in range(cantidad_salidas):
            if (matriz_canal[i][j] > 0):
                if (elem_no_cero == False):
                    elem_no_cero = True
                else:
                    return False
    return True


# Verifica si el canal es uniforme.
# Ordena los valores de la primera fila de menor a mayor.
# Recorre las demás filas y también ordena sus valores.
# Compara cada fila ordenada con la primera.
# Si encuentra alguna diferencia, devuelve False (no es uniforme).
# Si todas contienen los mismos valores, devuelve True (es uniforme).
# Un canal uniforme es aquel en el que todas las filas de la matriz tienen los mismos valores, aunque pueden estar en distinto orden.

def verifica_uniforme(matriz_canal):
    primera_fila = sorted(matriz_canal[0])
    for fila in matriz_canal[1:]:
        fila_ordenada = sorted(fila)
        for j in range(len(primera_fila)):
            if not math.isclose(primera_fila[j], fila_ordenada[j], abs_tol=1e-10):
                return False
    return True

# Capacidad  = maxima cantidad de informacion que puede transmitir un canal
# Segundo teorema de shannon - si una fuente tiene entropia H y un canal una capacidad C, si se cumple H<=C, la salida de la fuente
# se puede transmitir a traves del canal y recuperarse con una probabilidad pequeña de error
def obtener_capacidad(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    if (verifica_sin_ruido(matriz_canal)):
        return math.log(cantidad_entradas, 2)
    elif (verifica_determinante(matriz_canal)):
        return math.log(cantidad_salidas, 2)
    elif verifica_uniforme(matriz_canal):
        return math.log(len(matriz_canal[0]), 2) - entropias.entropia_a_priori(matriz_canal[0])
    else:
        # calculo maximo aproximado
        return 0


# La capacidad de un canal bsc se estima con la mayor informacion mutua
# información mutua mide cuánta información de la entrada podemos recuperar conociendo la salida.

def estimar_capacidad_canal_binario(matriz_canal, paso = 0.01):
    if len(matriz_canal) != 2:
        raise ValueError("El canal debe tener dos entradas")
    if not (0 < paso <= 1):
        raise ValueError("El paso debe estar entre 0 y 1")
    capacidad = -1
    mejor_probabilidad = 0
    i = 0
    while True:
        # Incluimos p = 1 aunque el paso no divida exactamente a 1.
        p = min(i * paso, 1.0)
        probabilidades = [p, 1 - p]
        informacion_mutua = entropias.obtener_informacion_mutua(probabilidades, matriz_canal)
        if informacion_mutua > capacidad:
            capacidad = informacion_mutua
            mejor_probabilidad = p
        if p == 1:
            break
        i += 1
    return capacidad, mejor_probabilidad



# Calcula la probabilidad de error de decodificación. (la probabilidad de interpretar incorrectamente el símbolo que se envió originalmente a partir del símbolo recibido.)
# Para cada símbolo de salida, busca la entrada con mayor probabilidad conjunta
# (probabilidad a priori de entrada multiplicada por la probabilidad de transición).
# Suma las probabilidades conjuntas máximas para obtener la probabilidad de acierto.
# Finalmente, resta ese resultado a 1 para obtener la probabilidad de error.
def obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):
    cantidad_entradas = len(matriz_canal)
    cantidad_salidas = len(matriz_canal[0])
    probabilidad_acierto = 0
    for j in range(cantidad_salidas):
        mayor_probabilidad_conjunta = 0
        for i in range(cantidad_entradas):
            probabilidad_conjunta = (probabilidades_a_priori[i] * matriz_canal[i][j])
            if probabilidad_conjunta > mayor_probabilidad_conjunta:
                mayor_probabilidad_conjunta = probabilidad_conjunta
        probabilidad_acierto += mayor_probabilidad_conjunta
    return 1 - probabilidad_acierto