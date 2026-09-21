from math import log2

def calcula_entropiaSinMem(probabilidades):
    entropia = 0
    for prob in probabilidades:
        entropia += prob * log2(1/prob)
    return entropia

# Entropia de fuente sin memoria = sumatoria de prob * log2(1/prob) para todo simbolo

#La función extiende genera todas las secuencias posibles de longitud n a partir del alfabeto s. 
#Se comienza con una secuencia vacía de combinaciones de probabilidad 1.
#En cada iteración agrega un símbolo a las combinaciones existentes y calcula su probabilidad multiplicando la probabilidad anterior 
#por la del nuevo símbolo. Al final, guarda las secuencias en sext y sus probabilidades correspondientes en pext.

def extiende(n, s, p, sext, pext):
    # Inicializamos la base de la extensión
    combinaciones = [[]]
    probabilidades = [1.0]

    for k in range(n):
        nuevas_comb = []
        nuevas_prob = []
        
        # Iteramos usando un índice 'i' para garantizar que
        # la cadena en la posición 'i' corresponda SIEMPRE a la probabilidad 'i'
        for i in range(len(combinaciones)):
            cadena_actual = combinaciones[i]
            prob_actual = probabilidades[i]
            
            for j in range(len(s)):
                nuevas_comb.append(cadena_actual + [s[j]])
                nuevas_prob.append(prob_actual * p[j])

        combinaciones = nuevas_comb
        probabilidades = nuevas_prob

    # Limpiamos las listas recibidas por si traían basura previa
    sext.clear()
    pext.clear()

    # Cargamos los datos limpios y alineados
    sext.extend(combinaciones)
    pext.extend(probabilidades)