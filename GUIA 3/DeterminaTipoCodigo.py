
def esNo_singular(codigo: list[str]):
    for i in range(len(codigo)):
        for j in range(i + 1, len(codigo)):
            if codigo[i] == codigo[j]:
                return False

    return True

#Elige una palabra código y verifica que ninguna de las siguientes sea igual a la elegida 
#(si alguna es igual, retorna falso, no es singular)

def esInstantaneo(codigo: list[str]):
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            
            if i != j:
                if codigo[j].startswith(codigo[i]):
                    return False

    return True

#Elige una palabra código y verifica que no sea prefijo de ninguna de las siguientes 
# (si alguna es prefijo, retorna falso, no es instantáneo)

def esUD(codigo: list[str]):

    # Primer conjunto de sufijos
    sufijos = set()

    for palabra1 in codigo:
        for palabra2 in codigo:

            if palabra1 != palabra2:

                 # palabra2 es prefijo de palabra1
                 if palabra1.startswith(palabra2):
                     resto = palabra1[len(palabra2):]
                     sufijos.add(resto)

                 # palabra1 es prefijo de palabra2
                 elif palabra2.startswith(palabra1):
                     resto = palabra2[len(palabra1):]
                     sufijos.add(resto)

    # Sufijos que ya analizamos
    vistos = set()

    unideco = True
    while len(sufijos) and unideco:

        nuevos = set()

        # Guardamos los sufijos actuales como ya vistos
        for sufijo in sufijos:
            vistos.add(sufijo)

        # Comparamos cada sufijo con cada palabra del código
        for sufijo in sufijos:
            for palabra in codigo:

                if sufijo.startswith(palabra):
                    resto = sufijo[len(palabra):]
                    nuevos.add(resto)

                elif palabra.startswith(sufijo):
                    resto = palabra[len(sufijo):]
                    nuevos.add(resto)

        # Sacamos los que ya habíamos encontrado
        nuevos = nuevos - vistos

        # Los nuevos pasan a ser los actuales
        sufijos = nuevos

        # Si aparece el vacío, NO es unívocamente decodificable
        if "" in sufijos:
            unideco = False

    return unideco

#METODO SARDINAS PATTERSON. 
# Primero busca las palabras codigo que son prefijos de otras palabras código, y guarda el sufijo que queda.
# Luego, con esos sufijos, busca si alguno es prefijo de alguna palabra código o de los sufijos obtenidos, y guarda el sufijo que queda, asi sucesivamente.
# Si en algún momento encuentra el sufijo vacío, significa que hay una ambigüedad en la decodificación (una cadena coincide con otra), 
# y por lo tanto, el código no es univocamente decodificable.
# Si un conjunto de sufijos se repite, significa que no hay más sufijos nuevos que analizar, y por lo tanto, el código es univocamente decodificable.

codigo = ["011", "0111", "01", "11", "011111", "01111"]

if (esNo_singular(codigo)):
    if (esInstantaneo(codigo)):
        print("es instantaneo")
    else:
        if (esUD(codigo)):
            print("es univoco")
        else:
            print("es no singular")
else:
    print("es bloque")
