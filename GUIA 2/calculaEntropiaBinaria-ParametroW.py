#CALCULA CANT INFO Y ENTROPIA DE LA FUENTE BINARIA NO NULA, A PARTIR DE W (la prob de un simbolo);
from math import log2

def calculaProbs(w):
    probabilidades = []
    probabilidades.append(w)
    w2 = 1-w
    probabilidades.append(w2)
    return probabilidades

def cantInfo(w):
    if (w>0):
        return log2(1/w)
    else:
        return 1
    
    
w = 0.5
probabilidades = calculaProbs(w)

print("Cant Info: ", [cantInfo(prob) for prob in probabilidades])

print("Entropia de la fuente: ", sum([prob * cantInfo(prob) for prob in probabilidades]))