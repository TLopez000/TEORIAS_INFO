import math, random

def obtener_alfabeto(mensaje):
    alfabeto = [] 

    for simbolo in mensaje: 
        if simbolo not in alfabeto: 
            alfabeto.append(simbolo) 
    
    return alfabeto

def obtener_probabilidades(alfabeto, mensaje):
    probabilidades = []
    
    for simbolo in alfabeto:
        cantidad = mensaje.count(simbolo)
        probabilidad = cantidad/len(mensaje)
        probabilidades.append(probabilidad)
        
    return probabilidades    

#FUNCIONES PARA FUENTES SIN MEMORIA

def calcula_entropiaSinMem(probabilidades):
    entropia = 0
    for prob in probabilidades:
        entropia += prob * math.log2(1/prob)
    return entropia

def extiende(n: int, s: list[str], p: list[float], sext:list[str], pext: list[float]):

    combinaciones = [[]]
    probabilidades = [1.0]

    for k in range(n):
        nuevas_comb = []
        nuevas_prob = []
        
        for i in range(len(combinaciones)):
            cadena_actual = combinaciones[i]
            prob_actual = probabilidades[i]
            
            for j in range(len(s)):
                nuevas_comb.append(cadena_actual + [s[j]])
                nuevas_prob.append(prob_actual * p[j])

        combinaciones = nuevas_comb
        probabilidades = nuevas_prob

    sext.clear()
    pext.clear()

    sext.extend(combinaciones)
    pext.extend(probabilidades)

def genera_cadenaN_SinMemoria(n: int, alfabeto: list[str], probabilidades: list[float]):
    cadena = ""
    
    for i in range(n):
        letra = random.choices(alfabeto, weights=probabilidades)[0]
        cadena += letra
        
    return cadena    

#FUNCIONES PARA OBTENER MATRIZ Y VERIFICAR SI ES MARKOVIANA O NO

def obtener_matrizTrans_porColumnas(alfabeto: list[str], mensaje: list[str]):
    n = len(alfabeto)

    # Matriz de conteos
    matriz = [[0 for j in range(n)] for i in range(n)]

    # Contar las transiciones
    for i in range(len(mensaje) - 1):
        actual = mensaje[i]
        siguiente = mensaje[i + 1]

        # Buscar la posición de cada símbolo
        for j in range(n):
            if alfabeto[j] == actual:
                columna = j

            if alfabeto[j] == siguiente:
                fila = j

        matriz[fila][columna] += 1

    # Convertir los conteos a probabilidades
    for j in range(n):
        total = 0

        for i in range(n):
            total += matriz[i][j]

        if total > 0:
            for i in range(n):
                matriz[i][j] = matriz[i][j] / total

    return matriz


def tiene_memoria(matriz,  tolerancia: float):
    n = len(matriz)
    
    for i in range(n):
        max = 0
        min = 9999
        for j in range(n):
            if (matriz[i][j] > max):
                max = matriz[i][j]
            if (matriz[i][j] < min):
                min = matriz[i][j]
                
        diferencia = max - min

        if diferencia > tolerancia:
            return True

    return False

#FUNCION PARA IMPRIMIR LA MATRIZ CON UN FORMATO MAS VISUAL

def imprime_matriz(alfabeto,matriz):
    print("         ", alfabeto)
    for i in range(len(matriz)):
        print(f"{alfabeto[i]:^6}", end="")
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:^8.7f} ", end="")
        print()


#FUNCIONES PARA FUENTES MARKOVIANAS

def vector_estacionario_porColumnas(MT):
    n = len(MT)

    # A = MT - I
    A = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(MT[i][j] - 1)
            else:
                fila.append(MT[i][j])
        A.append(fila)

    # Reemplazamos una ecuación por:
    # v1 + v2 + ... + vn = 1
    A[n-1] = [1] * n
    b = [0] * (n - 1) + [1]

    # Eliminación
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]

            for k in range(n):
                A[j][k] -= factor * A[i][k]

            b[j] -= factor * b[i]

    # Sustitución hacia atrás
    v = [0] * n

    for i in range(n - 1, -1, -1):
        suma = 0

        for j in range(i + 1, n):
            suma += A[i][j] * v[j]

        v[i] = (b[i] - suma) / A[i][i]

    return v


def calcular_entropia_fuenteConMem_porColumnas(vecEst, MatrizTrans):

    n = len(MatrizTrans)
    entropia_total = 0.0

    # Cada columna representa un estado de origen j
    for j in range(n):
        entropia_condicional = 0.0

        # Recorremos las probabilidades condicionales i
        for i in range(n):
            p = MatrizTrans[i][j]

            if p > 0:
                entropia_condicional += p * math.log2(1/p)

        # Ponderamos por la probabilidad estacionaria del estado j
        entropia_total += vecEst[j] * entropia_condicional

    return entropia_total


#RESOLUCION EJERCICIO


cad = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"

alfabeto = obtener_alfabeto(cad)
probabilidades = obtener_probabilidades(alfabeto, cad)

matriz = obtener_matrizTrans_porColumnas(alfabeto, cad)

imprime_matriz(alfabeto,matriz)
print()
print("Alfabeto: ", alfabeto)
print("Probabilidades: ", probabilidades)

if (tiene_memoria(matriz, 0.05)):
    vecEst = vector_estacionario_porColumnas(matriz)
    print("vecEst: ", vecEst)
    entropia = calcular_entropia_fuenteConMem_porColumnas(vecEst, matriz)
    print("tiene memoria, entropia: ", entropia)
else:
    sext = []
    pext = []
    n = 2
    extiende(n,alfabeto,probabilidades,sext,pext)
    entropia = calcula_entropiaSinMem(probabilidades)
    print("es de memoria nula, entropia: ", entropia)
    print("Alf ext:", sext)
    print("Prob ext: ", pext)
    print("entropia extendida: ", n*entropia)