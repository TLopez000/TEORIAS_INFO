from math import log2

def obtener_alfabeto(mensaje):
    alfabeto = [] 

    for simbolo in mensaje: 
        if simbolo not in alfabeto: 
            alfabeto.append(simbolo) 
    
    return alfabeto

#Se recorre el mensaje y se añade cada simbolo que no se encuentre en el alfabeto.

def obtener_probabilidades(alfabeto, mensaje):
    probabilidades = []
    
    for simbolo in alfabeto:
        cantidad = mensaje.count(simbolo)
        probabilidad = cantidad/len(mensaje)
        probabilidades.append(probabilidad)
        
    return probabilidades    

#Se cuenta la cantidad de veces que aparece un simbolo en el mensaje y se divide por el largo del mensaje.

def calcula_cantInfo(prob):
    if (prob > 0):
        cantInfo = log2(1/prob)
    else:
        cantInfo = 1
        
    return cantInfo

#Calcula la cant de info que proporciona un simbolo

