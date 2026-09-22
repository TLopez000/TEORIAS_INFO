import random

def genera_mensajeN(n, codigo, probabilidades):
    mensajeN = []
    
    for i in range(n):
        simbolo = random.choices(codigo, weights=probabilidades)[0]
        mensajeN.append(simbolo)
        
    return mensajeN   

codigo = ['0', '10', '110', '111']
probs = [0.333,0.333,0.167,0.167]
n = 4

print(genera_mensajeN(n,codigo,probs))