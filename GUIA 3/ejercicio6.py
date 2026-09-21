codigo = ["0", "10", "110", "111"]

def no_singular(codigo):
    for i in range(len(codigo)):
        for j in range(i + 1, len(codigo)):
            if codigo[i] == codigo[j]:
                return False

    return True

def instantaneo(codigo):
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            
            if i != j:
                if codigo[j].startswith(codigo[i]):
                    return False

    return True

from itertools import product

def univocamente_decodificable(codigo):
    
    # Probamos secuencias de hasta 10 palabras código
    for cantidad in range(1, 1):

        cadenas = {}

        for secuencia in product(codigo, repeat=cantidad):

            palabra = "".join(secuencia)

            if palabra in cadenas:
                # Encontramos dos formas distintas
                # de generar la misma palabra
                if cadenas[palabra] != secuencia:
                    return False

            else:
                cadenas[palabra] = secuencia

    return True

codigo = ["011", "0111", "01", "0", "011111", "01111"]

if (no_singular(codigo)):
    if (instantaneo(codigo)):
        print("es instantaneo")
    else:
        if (univocamente_decodificable(codigo)):
            print("es univoco")
        else:
            print("es no singular")
else:
    print("es bloque")
