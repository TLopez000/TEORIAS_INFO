import lib as lib

mensaje = "GIIHGGGHGIHHIHIIGFHH"

alfabeto, probabilidades = lib.obtener_probabilidades_a_priori(mensaje)
entropia = lib.obtener_entropia_a_priori(probabilidades)

print("Entropia: ", entropia)

cod_huffman = lib.obtener_codigo_huffman(probabilidades)
tasa_compresion = lib.tasa_compresion(mensaje, cod_huffman)
rendimiento = lib.rendimiento(probabilidades, cod_huffman)
redundancia = lib.redundancia(probabilidades, cod_huffman)
long_media = lib.calcular_longitud_media(cod_huffman,probabilidades)

print("Tasa: ", tasa_compresion)
print("Rendimiento: ", rendimiento)
print("Redundancia: ", redundancia)
print("L: ", long_media)

alf_ext, probabilidades_ext = lib.obtener_extension(alfabeto, probabilidades, 3)
cod_huffman_ext = lib.obtener_codigo_huffman(probabilidades_ext)
rendimiento = lib.rendimiento(probabilidades_ext, cod_huffman_ext)
redundancia = lib.redundancia(probabilidades_ext, cod_huffman_ext)
long_media = lib.calcular_longitud_media(cod_huffman_ext,probabilidades_ext)
entropia_ext = lib.calcular_entropia(probabilidades_ext)

print("Entropia ext: ", entropia_ext)
print("Rendimiento: ", rendimiento)
print("Redundancia: ", redundancia)
print("L: ", long_media)

if (lib.extension_verifica_Shannon(probabilidades, cod_huffman, 1)):
    print("Extension de orden 1 cumple Shannon")
    
if (lib.extension_verifica_Shannon(probabilidades, cod_huffman_ext, 3)):
    print("Extension de orden 3 cumple Shannon")
    
#EXPLICACIONES
#Las probabilidades fueron calculadas a partir de sus frecuencias 
#relativas y la entropía, como el promedio ponderado por la 
#probabilidad de la cantidad de información.
#El código binario óptimo se hizo generando uno por cada método 
#(Huffman y Shannon-Fano) y nos quedamos con el código con mayor 
#rendimiento.
#La codificación de Huffman sigue este algoritmo:
#1. Se inicia un árbol binario vacío con aristas ponderadas. Para hijos 
#izquierdos, las aristas se ponderan con 0 y, para hijos derechos, se 
#ponderan con 1.
#2. Mientras el árbol no contenga a todo el alfabeto:
#   a. Ordenar alfabeto según probabilidades
#   b. Unificar los 2 símbolos o grupos de símbolos menos probables y 
#sumar sus probabilidades.
#   c. Crear un nodo vacío cuyos hijos sean éstos 2 grupos de símbolos. 
#El hijo izquierdo será el menos probable.
#Finalmente, la codificación de cada símbolo será la concatenación de 
#los 1s y 0s recorridos del árbol desde la raíz hasta donde esté 
#alojado el símbolo.

#La tasa de compresión no es más que el cociente entre el tamaño de un 
#mensaje y el tamaño del mensaje comprimido. Si éste último es 0, la 
#tasa de compresión también lo será.
#Para la extensión se hizo lo mismo que para la fuente.
#La longitud media es el promedio ponderado por la probabilidad de la 
#longitud de los códigos. El rendimiento se calculó como el cociente 
#entre la entropía de la fuente y la longitud media. Y la redundancia 
#es 1 menos el rendimiento.

#Para obtener el codigo extendido primero se hace la extension de las probabilidades originales
#al orden 3, y luego se aplica huffman a las probabilidades extendidas

#Antes que nada, ¿qué dice el Primer Teorema de Shannon? Se rige por la 
#siguiente fórmula:
#H_r(S^n) <= L_n <= H_r(S^n)+1 (1)
#Donde:
#S es el alfabeto fuente
#S^n es la extensión n de S
#L_n es la longitud media de Sn
#H_r es la entropía base r
#Sabiendo
#H(S^n)=nH(S) (2)
#Reemplazando (2) en (1), obtenemos:
#nH_r(S) <= L_n/n <= H_r(S)+1
#Dividiendo por n miembro a miembro, obtenemos:
#H_r(S) <= L_n/n <= H_r(S)+1/n (3)
#El algoritmo funciona de la siguiente manera:
#A partir de las palabras código, se genera la extensión S^n llamando a 
#una función desarrollada en la primera parte de la materia. Esta 
#función también retorna las probabilidades.
#Se calcula L_n a partir de lo calculado en el paso anterior con una 
#función implementada en la primera parte.
#Se calcula H_r(S)
#Se retorna true o false en función de si se cumple la inecuación (3).

#CONCLUSIONES
#La codificación de la fuente original presenta una longitud media de 2 bits por símbolo, mientras que su entropía es de 1.7884 bits. 
#Esto significa que la longitud media se encuentra por encima del límite establecido por el Primer Teorema de Shannon, por lo que cumple con dicho teorema. 
# Su eficiencia es del 89.42%, con una redundancia del 10.58%.

#Al utilizar una extensión de orden 3, la entropía del bloque es de 5.36 bits y la longitud media del código es de 5.38 bits. 
#Al dividir ambos valores por 3, obtenemos una entropía de aproximadamente 1.7867 bits por símbolo y una longitud media de 1.7933 bits por símbolo.

#Esto demuestra que la extensión permite acercar la longitud media del código al límite teórico establecido por Shannon, 
#aumentando la eficiencia al 99.63% y reduciendo la redundancia al 0.37%.

#La utilización de extensiones permite obtener códigos más compactos en términos de bits por símbolo, ya que aprovecha las combinaciones de símbolos para 
#lograr una longitud media más cercana a la entropía. En este caso, ambas codificaciones cumplen el Primer Teorema de Shannon, 
#pero la extensión de orden 3 consigue un mejor aprovechamiento de la información y una mayor tasa de compresión.

entrada = "10100000101011101001111110011001"
salida =  "QQPQQPPQQQPQRRRQSPQSQRQSQQPSQQPP"

alf_entrada, probabilidades_a_priori = lib.obtener_probabilidades_a_priori(entrada)

print("Alfabeto: ", alf_entrada, " Probabilidades: ", probabilidades_a_priori)

alf_entrada, alf_salida, matriz_canal = lib.obtener_matriz_canal(entrada,salida)
lib.imprime_matriz(alf_entrada, alf_salida, matriz_canal)

if (lib.verifica_determinante(matriz_canal)):
    print("determinante")
if (lib.verifica_sin_ruido(matriz_canal)):
    print("determinante")
if (lib.verifica_uniforme(matriz_canal)):
    print("determinante")
    
ruido = lib.obtener_ruido(probabilidades_a_priori, matriz_canal)
perdida = lib.obtener_perdida(probabilidades_a_priori, matriz_canal)
info = lib.obtener_informacion_mutua(probabilidades_a_priori, matriz_canal)

print("Ruido: ",ruido)
print("Perdida: ", perdida)
print("Info mutua: ", info)

matriz_reducida = lib.obtener_canal_reducido(matriz_canal)
lib.imprime_matriz(alf_entrada, [], matriz_reducida)

capacidad, p_0 = lib.estimar_capacidad_canal_binario(matriz_canal)
print("capacidad: ", capacidad)
print("p(0): ", p_0 , "p(1): ", 1-p_0)

prob_error = lib.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal)
print("error: ", prob_error)

matriz_recibida = lib.construye_matriz_mensaje(entrada)
lib.mostrar_matriz(matriz_recibida)
print("se detecto un error en la fila 2 columna 5, cambio ese bit 1 por 0")
matriz_corregida = matriz_recibida
matriz_corregida[1][4] = 0
print("Matriz corregida:")
lib.mostrar_matriz(matriz_corregida)

matriz_posteriori = lib.obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal)
print("PROBABILIDADES A POSTERIORI: ")
lib.mostrar_matriz(matriz_posteriori)

# por la regla de maxima decision, se sabe que si se emitio R o S, entro un 1.
# cuando se recibe Q o P, se decide 0 ya que es el que tiene max probabilidad a posteriori.
# Un 1 transmitido puede producir Q P R S
# Un 0 transmitido solo produce Q P
# Un 0 transmitido nunca se recupera como 1, no puede producir R S
# Un 1 transmitido puede recuperarse incorrectamente como 0 si produce Q o P
# Por lo tanto, el canal permite errores de 1 a 0 pero no de 0 a 1, aplicando esta regla de decision.
# El mensaje no es compatible con el canal:
# La corrección por paridad indica que se recupero un 1 donde debería haber un 0. Esto implicaría que durante la transmisión ocurrió un cambio de 0 a 1, 
# que es imposible para este canal. Por lo tanto, bajo la hipótesis de un único error utilizada para la corrección, 
# el mensaje recibido no pudo haberse transmitido por este canal y recuperado mediante la regla de decisión indicada.

#El mensaje no es compatible con el canal bajo la hipótesis de un único error:
#La corrección por paridad indica que se recuperó un 1 donde debería haber un 0. Esto implicaría un error de decisión de 0 a 1, que es imposible según el comportamiento del canal y la regla de máxima decisión utilizada.
#Por lo tanto, bajo la hipótesis de un único error utilizada para la corrección, el mensaje recibido no pudo haberse transmitido por este canal y recuperado mediante la regla de decisión indicada.