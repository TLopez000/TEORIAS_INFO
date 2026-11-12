import cumpleShannon
import metricasEficiencia
import math


def extiende_probabilidades(probabilidades, N):
    # Extiende las probabilidades a la N-ésima potencia
    if N == 1:
        return probabilidades

    probabilidades_extension = []
    for p in probabilidades:
        for q in extiende_probabilidades(probabilidades, N - 1):
            probabilidades_extension.append(p * q)

    return probabilidades_extension

def extiende_codigo(codigo, N):
    # Extiende el código a la N-ésima potencia
    if N == 1:
        return codigo

    codigo_extension = []
    for palabra in codigo:
        for palabra_ext in extiende_codigo(codigo, N - 1):
            codigo_extension.append(palabra + palabra_ext)

    return codigo_extension

####################################################################

##### HUFFMAN #####

def huffman(probabilidades):
    codigos = [""] * len(probabilidades)

    # Cada grupo guarda: [probabilidad, índices de símbolos]
    grupos = []

    for i in range(len(probabilidades)):
        grupos.append([probabilidades[i], [i]])

    while len(grupos) > 1:
        # Ordenamos de menor a mayor probabilidad
        grupos.sort(key=lambda x: x[0])

        # Sacamos los dos menos probables
        grupo1 = grupos.pop(0)
        grupo2 = grupos.pop(0)

        # Agregamos 0 y 1 a sus códigos
        for i in grupo1[1]:
            codigos[i] = "0" + codigos[i]

        for i in grupo2[1]:
            codigos[i] = "1" + codigos[i]

        # Fusionamos ambos grupos
        nuevo_grupo = [
            grupo1[0] + grupo2[0],
            grupo1[1] + grupo2[1]
        ]

        grupos.append(nuevo_grupo)

    return codigos

########## SHANNON FANO ###############

def shannon_fano(probabilidades):
    codigos = [""] * len(probabilidades)

    # Ordenamos los indices de mayor a menor probabilidad
    indices = list(range(len(probabilidades)))
    indices.sort(key=lambda i: probabilidades[i], reverse=True)

    # Grupos que todavía tenemos que dividir
    grupos = [indices]
    while len(grupos) > 0:
        grupo = grupos.pop(0)
        # Si queda un solo simbolo, no se puede dividir mas
        if len(grupo) <= 1:
            continue
        # Calculamos la probabilidad total del grupo
        total = 0
        for i in grupo:
            total += probabilidades[i]
        # Buscamos el mejor punto de corte
        acumulado = 0
        mejor_corte = 1
        menor_diferencia = float("inf")
        for k in range(1, len(grupo)):
            acumulado += probabilidades[grupo[k - 1]]
            suma_izquierda = acumulado
            suma_derecha = total - acumulado
            diferencia = abs(suma_izquierda - suma_derecha)
            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                mejor_corte = k
        # Dividimos el grupo
        izquierda = grupo[:mejor_corte]
        derecha = grupo[mejor_corte:]
        # Asignamos los bits
        for i in izquierda:
            codigos[i] += "0"
        for i in derecha:
            codigos[i] += "1"
        # Estos grupos después deben volver a dividirse
        grupos.append(izquierda)
        grupos.append(derecha)
    return codigos


##  RLC ##

def comprimir_RLC(mensaje):
    if not mensaje:
        return bytearray()

    resultado = bytearray()
    contador = 1
    simbolo_anterior = mensaje[0]

    for simbolo in mensaje[1:]:
        if simbolo == simbolo_anterior and contador < 255:
            contador += 1
        else:
            # Primero guardamos el simbolo y despues el contador
            
            # Guardamos el ASCII del simbolo
            resultado.append(ord(simbolo_anterior))

            # Guardamos la cantidad
            resultado.append(contador)

            simbolo_anterior = simbolo
            contador = 1

    # Agregamos el ultimo grupo
    resultado.append(ord(simbolo_anterior))
    resultado.append(contador)

    return resultado

## TASA COMPRESION ##

def tasa_compresion(mensaje, codificado):
    return len(mensaje) / len(codificado) 


########################################### EJERCICIOS #####################################################

alfabeto = ["a", "b", "c", "d"]
codigo = ["11", "01", "00", "10"]

mensaje_codificado = "11 00 11 10 01 11 10 01"

probabilidades = [3/8, 2/8, 1/8, 2/8]


codigo_ext = extiende_codigo(codigo, 3)
probabilidades_ext = extiende_probabilidades(probabilidades, 3)

codificaHuffman = huffman(probabilidades_ext)  #1 = huffman sobre la fuente()
codificaShannon = shannon_fano(probabilidades_ext)  #0 = shannon-fano sobre la extension 2

print(codificaHuffman, codificaShannon)

if (cumpleShannon.extension_verifica_Shannon(probabilidades_ext,codificaHuffman,1)):
    print("Codigo de Huffman cumple el teorema de Shannon")

if (cumpleShannon.extension_verifica_Shannon(probabilidades_ext,codificaShannon,1)):
    print("Codigo de Shannon-Fano cumple el teorema de Shannon")

metricasEficiencia.metricasEficiencia(probabilidades_ext,codificaHuffman)
metricasEficiencia.metricasEficiencia(probabilidades_ext,codificaShannon)
