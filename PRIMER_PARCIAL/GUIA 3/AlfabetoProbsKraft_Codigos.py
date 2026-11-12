def obtener_alfabeto(codigo: list[str]):
    alfabeto = [] 

    for palabra in codigo: 
        for simbolo in palabra:
            if simbolo not in alfabeto: 
                alfabeto.append(simbolo)
    
    return alfabeto

#Se recorren las palabras codigo y se añade cada simbolo que no se encuentre en el alfabeto.

def obtener_longitudes_codigo(codigo: list[str]):
    return [len(palabra) for palabra in codigo]

#recorre cada palabra y guarda su longitud en una lista.

def inecuacion_kraft(alfabeto: list[str], longitudes: list[int]):
    r = len(alfabeto) #cantidad de simbolos del alfabeto
    suma = 0
    for longitud in longitudes: 
        suma += 1/(r ** longitud) 

    return suma

# obtengo r (la cantidad de simbolos del alfabeto)
# luego recorro la cantidad de simbolos fuente q (que la obtengo de la cantidad de longitudes)
# por ultimo hago la sumatoria de r elevado a la inversa de cada longitud