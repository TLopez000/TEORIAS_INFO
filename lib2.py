import math, random

def obtener_alfabeto(codigo: list[str]):
    alfabeto = [] 

    for palabra in codigo: 
        for simbolo in palabra:
            if simbolo not in alfabeto: 
                alfabeto.append(simbolo)
    
    return alfabeto

def obtener_longitudes_codigo(codigo: list[str]):
    return [len(palabra) for palabra in codigo]

def inecuacion_kraft(alfabeto: list[str], longitudes: list[int]):
    r = len(alfabeto) #cantidad de simbolos del alfabeto
    suma = 0
    for longitud in longitudes: 
        suma += 1/(r ** longitud) 

    return suma


#FUNCIONES PARA DETERMINAR EL TIPO DE CODIGO

def esNo_singular(codigo: list[str]):
    codigoSinRepeticiones = set(codigo)
    return len(codigo) == len(codigoSinRepeticiones)

def esInstantaneo(codigo: list[str]):
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            
            if i != j:
                if codigo[j].startswith(codigo[i]):
                    return False

    return True

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

#FUNCIONES DE CALCULO DE ENTROPIA BASE R Y LONGITUD MEDIA

def calcula_entropia_baseR(r: int, probabilidades: list[float]):
    
    entropia = 0
    for i in range(len(probabilidades)):
        if (probabilidades[i] > 0):
            entropia += probabilidades[i] * math.log(1/probabilidades[i], r)

    return entropia

def long_media(probabilidades: list[float], longitudes: list[int]):
    L = 0
    for i in range(len(probabilidades)):
        L += probabilidades[i] * longitudes[i]

    return L

#FUNCION PARA DETERMINAR SI ES COMPACTO

def escompacto(codigo: list[str], probabilidades: list[float]):
    cumple = True
    if esInstantaneo(codigo):
         longitudes = obtener_longitudes_codigo(codigo)
         alfabeto = obtener_alfabeto(codigo)
         r = len(alfabeto)

         i = 0
         while i<len(longitudes) and cumple:
             techoinfo = math.log(1/probabilidades[i],r)
             if longitudes[i] > math.ceil(techoinfo):
                 cumple = False
             i+=1
    else:
        cumple = False
 
    return cumple

#Longitudes maximas para que el codigo sea compacto:

def longitudes_maximas(probabilidades: list[float], r: int):
    longitudes = []
    for p in probabilidades:
        l = math.ceil(-math.log(p, r))
        longitudes.append(l)
    return longitudes

#GENERAR UN MENSAJE N

def genera_mensajeN(n, codigo, probabilidades):
    mensajeN = []
    
    for i in range(n):
        simbolo = random.choices(codigo, weights=probabilidades)[0]
        mensajeN.append(simbolo)
        
    return mensajeN  



codigo = ["/+", "*", "+-", "-", "*/"]
probabilidades = [0.15,0.25,0.05,0.45,0.1]

alfabeto = obtener_alfabeto(codigo)
print("Alfabeto codigo: ", alfabeto)
longitudes = obtener_longitudes_codigo(codigo)
print("Longitudes: ", longitudes)
kraft = inecuacion_kraft(alfabeto,longitudes)
print("In de Kraft: ", kraft)

baseR = len(alfabeto)
entropia = calcula_entropia_baseR(baseR, probabilidades)
longitudprom = long_media(probabilidades, longitudes)

print("ENTROPIAr: ", entropia)
print("L : ", longitudprom)

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

if (escompacto(codigo, probabilidades)):
    print("CODIGO COMPACTO")
else:
    print("CODIGO NO COMPACTO")