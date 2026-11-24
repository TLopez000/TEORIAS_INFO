import math

def informacion(P, r=2):
    I = [math.log(1 / p, r) if p > 0 else 0 for p in P]
    return I

def calcular_entropia(P, r=2):
    I = informacion(P,r)
    H = 0
    for i in range(len(P)):
        H += P[i] * I[i]
    return H

def rendimiento(probabilidades, codificacion, r = 2):
    return calcular_entropia(probabilidades, r) / calcular_longitud_media(codificacion, probabilidades)

def redundancia(probabilidades, codificacion, r = 2):
    return 1 - rendimiento(probabilidades, codificacion, r)

def obtener_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def calcular_longitud_media(codigo, probabilidades):
    suma = 0
    longitudes = obtener_longitudes(codigo)
    for i in range(len(longitudes)):
        suma += probabilidades[i] * longitudes[i]
    return suma

def obtener_probabilidades_a_priori(entrada):
    alfabeto = []
    for simbolo in entrada:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    probabilidades = [
        entrada.count(simbolo) / len(entrada)
        for simbolo in alfabeto
    ]
    return alfabeto, probabilidades

def obtener_entropia_a_priori(probabilidades_a_priori):
    entropia = 0
    for p in probabilidades_a_priori:
        if (p > 0):
            entropia += p * math.log(1 / p, 2)
    return entropia

def obtener_extension(alfabeto, probabilidades, orden):
    extension = [[]]
    probabilidades_extension = [1]
    for _ in range(orden):
        nueva_extension = []
        nuevas_probabilidades = []
        for i in range(len(extension)):
            for j in range(len(alfabeto)):
                nueva_extension.append(extension[i] + [alfabeto[j]])
                nuevas_probabilidades.append(probabilidades_extension[i] * probabilidades[j])
        extension = nueva_extension
        probabilidades_extension = nuevas_probabilidades
    return extension, probabilidades_extension


def obtener_codigo_huffman(probabilidades):
    codigos = ["" for _ in probabilidades]

    # Cada grupo contiene: [probabilidad total, lista de índices de sus símbolos]
    grupos = [[probabilidades[i], [i]] for i in range(len(probabilidades))]

    while len(grupos) > 1:
        # Buscamos y quitamos el grupo menos probable.
        menor = 0
        for i in range(1, len(grupos)):
            if grupos[i][0] < grupos[menor][0]:
                menor = i
        grupo_1 = grupos.pop(menor)

        # Buscamos y quitamos el segundo menos probable.
        menor = 0
        for i in range(1, len(grupos)):
            if grupos[i][0] < grupos[menor][0]:
                menor = i
        grupo_2 = grupos.pop(menor)

        # Agregamos un bit por delante de cada código.
        for indice in grupo_1[1]:
            codigos[indice] = "0" + codigos[indice]
        for indice in grupo_2[1]:
            codigos[indice] = "1" + codigos[indice]

        # Unimos ambos grupos.
        nuevo_grupo = [grupo_1[0] + grupo_2[0], grupo_1[1] + grupo_2[1]]
        grupos.append(nuevo_grupo)
    return codigos

mensaje = "011001111110111111110111011111"

alfabeto, probabilidades = obtener_probabilidades_a_priori(mensaje)
entropia = obtener_entropia_a_priori(probabilidades)

print("Entropia: ", entropia)

cod_huffman = obtener_codigo_huffman(probabilidades)
rendimiento_original = rendimiento(probabilidades, cod_huffman)
long_media = calcular_longitud_media(cod_huffman,probabilidades)
redundancia_original = redundancia(probabilidades,cod_huffman)

print("Redundancia: ", redundancia_original)
print("Rendimiento: ", rendimiento_original)
print("L: ", long_media)

alf_ext2, probabilidades_ext2 = obtener_extension(alfabeto, probabilidades, 2)
cod_huffman_ext2 = obtener_codigo_huffman(probabilidades_ext2)
rendimiento_ext2 = rendimiento(probabilidades_ext2, cod_huffman_ext2)

long_media = calcular_longitud_media(cod_huffman_ext2,probabilidades_ext2)
entropia_ext2 = calcular_entropia(probabilidades_ext2)
redundancia_ext2 = redundancia(probabilidades_ext2, cod_huffman_ext2)

print("Entropia ext2: ", entropia_ext2)
print("Rendimiento: ", rendimiento_ext2)
print("Redundancia: ", redundancia_ext2)
print("L: ", long_media)

alf_ext3, probabilidades_ext3 = obtener_extension(alfabeto, probabilidades, 3)
cod_huffman_ext3 = obtener_codigo_huffman(probabilidades_ext3)
rendimiento_ext3 = rendimiento(probabilidades_ext3, cod_huffman_ext3)
long_media = calcular_longitud_media(cod_huffman_ext3,probabilidades_ext3)
entropia_ext3 = calcular_entropia(probabilidades_ext3)
redundancia_ext3 = redundancia(probabilidades_ext3, cod_huffman_ext3)

print("Entropia ext3: ", entropia_ext3)
print("Rendimiento: ", rendimiento_ext3)
print("Redundancia: ", redundancia_ext3)
print("L: ", long_media)