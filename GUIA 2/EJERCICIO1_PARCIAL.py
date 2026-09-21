import random

from AlfabetoProbs import obtener_alfabeto, obtener_probabilidades
from obtenerMatriz_Memoria import obtener_matrizTrans_porColumnas, tiene_memoria, imprime_matriz
from FuenteConMemoria import calcular_entropia_fuenteConMem_porColumnas, vector_estacionario_porColumnas
from FuenteSinMemoria import extiende, calcula_entropiaSinMem

cad = ";;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:;"

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
    print(sext)
    print(pext)
    print("entropia extendida: ", n*entropia)


#Para empezar, el alfabeto y las probabilidades se obtuvieron con una función que recorre el mensaje emitido por la fuente. Al recorrer, se pregunta si el caracter recorrido está en la lista de caracteres inicializada como una lista vacía. Si la respuesta es sí, en el mismo índice en el que ya se encuentra el caracter se le suma 1 a la lista de probabilidades también inicializada como una lista vacía. En cambio, si no estaba en la lista de caracteres, se agrega el caracter en cuestión a la lista de alfabeto y se le agregaba un 1 a la lista de probabilidades. Al finalizar, a todos los elementos de la lista de probabilidades se los divide por la longitud de la cadena.
#En cuanto a la matriz de transición, Primero obtengo el alfabeto de la misma forma que hice anteriormente. Luego, creé una matriz cuadrada de ceros de nxn siendo n la cantidad de caracteres que contiene el alfabeto. Después, al recorrer el mensaje, iba tomando de a 2 caracteres. Buscaba el primer caracter entre las columnas y el segundo caracter en las filas para sumar 1 en la celda. Finalmente, normalicé las matrices por columnas.
#para determinar si hay memoria tenés que verificar si las probabilidades de un mismo destino cambian según el origen.
#para ello recorro cada fila y obtengo su maximo y su minimo, luego obtengo la diferencia. Si para algun simbolo la diferencia es mayor a la tolerancia, la fuente tiene memoria
#En cuanto a la entropía de la fuente, tomo la lista de probabilidades obtenida anteriormente para aplicar la definición; es decir, la sumatoria entre los productos de cada probabilidad con su respectiva información, siendo la información igual al logaritmo base r (por defecto, r=2) de la inversa de la probabilidad.
#Para generar la extensión n lo que hago es, con 2 bucles for anidados, recorro las combinaciones previas y el alfabeto para agregar al nuevo alfabeto todas las combinaciones posibles entre los elementos de estas dos listas. Por último, recorro el mensaje de a 2 caracteres 
#para obtener las probabilidades de la misma forma que se hizo anteriormente. En cuanto a la entropía, simplemente aplico un teorema visto en clase (H(S^n) = nH(S))  y multiplico por 2 la entropía calculada anteriormente.
#Para obtener el vector estacionario lo que hago es aplicar la siguiente formula:
#MV* = V*
#Restando V* miembro a miembro,
#MV* - V* = 0
#Extrayendo factor común:
#(M-Id)V* = 0 (1)
#El problema acá es que el sistema de ecuaciones es compatible indeterminado. Para ello, sumamos la siguiente expresión:
#Σvi* = 1 (2)
#Para obtener un sistema de ecuaciones compatible determinado, tacho una ecuación del sistema (1) por ser combinación lineal de las demás y la suplanto por la ecuación (2). Finalmente, me queda un sistema de tipo Ax = b que simplemente lo resuelvo premultiplicando miembro a miembro por la inversa de A.

