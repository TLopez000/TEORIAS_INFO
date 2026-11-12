from DeterminaTipoCodigo import esInstantaneo
from AlfabetoProbsKraft_Codigos import obtener_alfabeto, obtener_longitudes_codigo
from math import log, ceil

def escompacto(codigo: list[str], probabilidades: list[float]):
    cumple = True
    if esInstantaneo(codigo):
         longitudes = obtener_longitudes_codigo(codigo)
         alfabeto = obtener_alfabeto(codigo)
         r = len(alfabeto)

         i = 0
         while i<len(longitudes) and cumple:
             techoinfo = log(1/probabilidades[i],r)
             if longitudes[i] > ceil(techoinfo):
                 cumple = False
             i+=1
    else:
        cumple = False
 
    return cumple

#Para determinar que un codigo es compacto verifico que sea instantaneo (para que sea util y eficiente ademas de compacto)
#y que todas las longitudes de las palabras código 
#sean menores o iguales al techo de la información en base r de la palabra
#ceil redondea un float a su entero siguiente (si x = 1,2 redondea a x = 2), 
#esto es porque debo comparar longitudes minimas necesarias para representar la palabra
#con las longitudes del codigo




              
    



