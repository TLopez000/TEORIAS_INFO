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

def metricasEficiencia(probs_fuente, codificacion):
    L = long_media(probs_fuente, obtener_longitudes_codigo(codificacion))
    H = calcula_entropia_baseR(probs_fuente, len(obtener_alfabeto(codificacion)))

    rendimiento = H/L
    redundancia = 1 - rendimiento

    print("Rendimiento: ", rendimiento)
    print("Redundancia: ", redundancia)

    return rendimiento,redundancia


#EJ 7
probs1 = [0.5,0.2,0.3]
cod1 = ["11","010","00"]

probs2 = extiende_probabilidades(probs1,2)
cod2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"] 

#EJ 8
probs = [0.2,0.15,0.1,0.3,0.25]
cod81 = ["01","111","110","101","100"]
cod82 = ["00","01","10","110","111"]
cod83 = ["0110","010","0111","1","00"]
cod84 = ["11","001","000","10","01"]


metricasEficiencia(probs,cod81)
metricasEficiencia(probs,cod82)
metricasEficiencia(probs,cod83)
metricasEficiencia(probs,cod84)

'''Conclusiones:
- cod81 es el menos eficiente de los cuatro, ya que presenta la mayor redundancia (20,42 %).
- cod82 mejora el rendimiento respecto de cod81, reduciendo la redundancia al 12,62 %.
- cod83 alcanza un rendimiento del 90,95 %, con una redundancia del 9,05 %.
- cod84 presenta el mejor resultado, con un rendimiento del 99,03 % y una redundancia de apenas el 0,97 %. 
  Es el código que aprovecha mejor la entropía de la fuente.'''