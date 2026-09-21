# DADA UNA SECUENCIA DE CARACTERES: DEVUELVE SU ALFABETO (PROBS Y CANT INFO DE CADA Si) Y ENTROPIA DE LA FUENTE

from AlfabetoProbs import obtener_alfabeto,obtener_probabilidades,calcula_cantInfo,calcula_entropiaSinMem

cad = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"
alfabeto = obtener_alfabeto(cad)
probabilidades = obtener_probabilidades(alfabeto, cad)


print("Alfabeto: ", alfabeto, "Probs: ", probabilidades)
print("Cant info: ", [calcula_cantInfo(prob) for prob in probabilidades])
print("Entropia de la fuente: ", calcula_entropiaSinMem(probabilidades))