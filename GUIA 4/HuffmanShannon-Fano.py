import cumpleShannon

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

def compresion_sin_perdida(probs, metodo):
     items = [[p, ""] for p in probs]
     if (metodo == 1):
         huffman(sorted(items))
     else:
         shannon_fano(sorted(items))
     return [code for _, code in items]

##### HUFFMAN #####

def huffman(items):
     # Cada grupo contiene: [probabilidad total, elementos originales del grupo]
    grupos = [[item[0], [item]] for item in items]

    # Se combinan grupos hasta que todos formen uno solo
    while len(grupos) > 1:
        grupos.sort(key=lambda grupo: grupo[0])  # Ordena grupos por probabilidad creciente

        prob1, hojas1 = grupos.pop(0)  # Probabilidad y elementos del grupo menos probable
        prob2, hojas2 = grupos.pop(0)  # Probabilidad y elementos del segundo menos probable

        for hoja in hojas1:            # Elementos originales del primer grupo
            hoja[1] = "0" + hoja[1]    # Añade el bit 0 a sus códigos

        for hoja in hojas2:            # Elementos originales del segundo grupo
            hoja[1] = "1" + hoja[1]    # Añade el bit 1 a sus códigos

        # Crea un grupo con la probabilidad combinada y todas sus hojas
        grupos.append([prob1 + prob2, hojas1 + hojas2])

########## SHANNON FANO ###############

def shannon_fano(items):
    indices = list(range(len(items)))  # Posiciones de los elementos
    indices.sort(
        key=lambda i: items[i][0],
        reverse=True
    )  # Ordena las posiciones por probabilidad descendente

    grupos = [indices]  # Grupos de posiciones pendientes de dividir

    while grupos:
        grupo = grupos.pop(0)  # Siguiente grupo pendiente

        if len(grupo) <= 1:  # Un elemento ya no necesita dividirse
            continue

        total = sum(items[i][0] for i in grupo)  # Probabilidad total del grupo
        acumulado = 0  # Probabilidad acumulada desde el inicio del grupo
        mejor_corte = 1  # Posición donde se dividirá el grupo
        menor_diferencia = float("inf")  # Menor diferencia entre las dos partes

        # Busca las partes con sumas de probabilidad más parecidas
        for k in range(1, len(grupo)):
            acumulado += items[grupo[k - 1]][0]
            diferencia = abs(acumulado - (total - acumulado))

            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                mejor_corte = k

        izquierda = grupo[:mejor_corte]  # Posiciones de la primera parte
        derecha = grupo[mejor_corte:]  # Posiciones de la segunda parte

        for i in izquierda:
            items[i][1] += "0"  # Añade 0 directamente al código en items

        for i in derecha:
            items[i][1] += "1"  # Añade 1 directamente al código en items

        grupos.append(izquierda)  # Pendiente de dividir la primera parte
        grupos.append(derecha)  # Pendiente de dividir la segunda parte


########################################### EJERCICIOS #####################################################

prob1 = [0.7,0.3]
cod1 = ['1', '0']

prob2 = extiende_probabilidades(prob1,2)

codificaHuffman = compresion_sin_perdida(prob1,1)  #1 = huffman sobre la fuente()
codificaShannon = compresion_sin_perdida(prob2,0)  #0 = shannon-fano sobre la extension 2

print(codificaHuffman, codificaShannon)

if (cumpleShannon.extension_verifica_Shannon(prob1,codificaHuffman,1)):
    print("Codigo de Huffman cumple el teorema de Shannon")

if (cumpleShannon.extension_verifica_Shannon(prob1,codificaShannon,2)):
    print("Codigo de Shannon-Fano cumple el teorema de Shannon")
