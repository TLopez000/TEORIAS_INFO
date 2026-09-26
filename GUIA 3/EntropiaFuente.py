from AlfabetoProbsKraft_Codigos import obtener_longitudes_codigo
import math

def calcula_entropia_baseR(r: int, probabilidades: list[float]):
    
    entropia = 0
    for i in range(len(probabilidades)):
        if (probabilidades[i] > 0):
            entropia += probabilidades[i] * math.log(1/probabilidades[i], r)

    return entropia

#La entropia de la fuente la obtengo recorriendo la lista de probabilidades, multiplico Pi por el Logaritmo en base r de 1/Pi
#y voy acumulando en la variable entropia

def long_media(probabilidades: list[float], longitudes: list[int]):
    L = 0
    for i in range(len(probabilidades)):
        L += probabilidades[i] * longitudes[i]

    return L

# La longitud media del codigo la obtengo  recorriendo las listas de probabilidades y longitudes, 
# multiplicando Pi * Li y haciendo la suma de cada operacion.

