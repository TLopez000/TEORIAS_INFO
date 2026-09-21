import random
from AlfabetoProbs import obtener_alfabeto, obtener_probabilidades

#random.choices pone [h,l,a], [0,25 , 0,25 , 0,25] y en base a eso elije una lista (con el 0 tomamos la primera)

def genera_cadenaN_SinMemoria(n, alfabeto, probabilidades):
    cadena = ""
    
    for i in range(n):
        letra = random.choices(alfabeto, weights=probabilidades)[0]
        cadena += letra
        
    return cadena      

cad = "neuquen"

alfabeto = obtener_alfabeto(cad)
probabilidades = obtener_probabilidades(alfabeto,cad)

print(alfabeto, probabilidades)

cadenaGenerada = genera_cadenaN_SinMemoria(7, alfabeto, probabilidades)
print(cadenaGenerada)
    