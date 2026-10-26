import math

def obtener_alfabeto(codigo: list[str]):
    alfabeto = [] 

    for palabra in codigo: 
        for simbolo in palabra:
            if simbolo not in alfabeto: 
                alfabeto.append(simbolo)
    
    return alfabeto

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


def calcula_entropia_baseR(probabilidades, r):
    entropia = 0
    for p in probabilidades:
        if p > 0:
            entropia += p * math.log(1 / p, r)
    return entropia


def obtener_longitudes_codigo(codigo: list[str]):
    return [len(palabra) for palabra in codigo]

def long_media(probabilidades: list[float], longitudes: list[int]):
    L = 0
    for i in range(len(probabilidades)):
        L += probabilidades[i] * longitudes[i]

    return L

#palabras_codigoExt tiene las palabras codigo, N indica la extension a la que corresponden las palabras codigo.

def extension_verifica_Shannon(probabilidadesOriginales, palabras_codigoExt, N):
    r = len(obtener_alfabeto(palabras_codigoExt))

    # Entropía de la fuente original
    H = calcula_entropia_baseR(probabilidadesOriginales, r)

    # Extiendo solamente las probabilidades
    probabilidades_extension = extiende_probabilidades(probabilidadesOriginales, N)

    # Si el código extendido no tiene la misma cantidad de palabras que las probabilidades extendidas, se extiende el código
    # Esto es necesario por si me pasan la fuente original y me piden verificar la extension (SOLO si no me pasan la extension N, la genero)
    if (len(probabilidades_extension) > len(palabras_codigoExt)):
        palabras_codigoExt = extiende_codigo(palabras_codigoExt, N)

    # Longitud media de las palabras código de la extensión
    longitudes_extension = obtener_longitudes_codigo(palabras_codigoExt)
    
    L = long_media(probabilidades_extension, longitudes_extension)
    print("H :", H)
    print("L :", L)
  
    # Primer Teorema de Shannon
    return (H <= L / N <= H + 1 / N)

'''
#EJ3
cod2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"] # Extension 2
cod1 = ["11", "010", "00"] # Fuente

prob = [0.5, 0.2, 0.3]

#EJ2
cod3 = ["BA", "CAB", "A", "CBA"]
prob3 = [0.3,0.1,0.4,0.2]

#EJ4
codB = ["0", "1"]
probW = [0.8, 0.2]

if (extension_verifica_Shannon(probW, codB, 3)):
    print("El código cumple con la desigualdad de Shannon")
else:
    print("El código NO cumple con la desigualdad de Shannon")'''

#Primero extiendo las probabilidades combinando las probabilidades de la fuente original, luego me fijo si el codigo pasado por parametro ya esta extendido, si no lo esta, lo extiendo.
#Por ultimo calculo la longitud media de las palabras codigo de la extension y verifico la condicion Hr(S) <= L/N <= Hr(S) + 1/N

#Si me piden proponer un codigo que cumpla el teorema, genero un codigo univoco de longitudes arbitrarias, mientras cumpla ser ud y el teorema, es valido.
#En el ejercicio 4, la extension de orden 3 generada por mi codigo ya cumple el teorema, aunque podria mejorarse acortando la longitud media, asignando a los simbolos mas probables longitudes mas cortas
