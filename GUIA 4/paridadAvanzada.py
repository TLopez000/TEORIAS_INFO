# fila 0       → bits de paridad longitudinal + cruzada
# filas 1...n  → 7 bits ASCII + bit de paridad
#LA MATRIZ QUEDA CONFORMADA POR FILAS, CADA BYTE ES UNA FILA

#genera una fila por cada caracter, agregando al final el byte de LRC
#luego se recorren las columnas y se agrega el byte de VRC en una lista que luego se inserta en la fila 0
#cada fila de la matriz es convertida a un byte, y se guarda la representacion entera de cada uno en un arreglo

def codificar(mensaje):
    if not mensaje:
        return bytearray()

    matriz = []
    # Genero una fila por cada caracter
    for caracter in mensaje:
        ascii = ord(caracter)
        binario = bin(ascii)[2:].zfill(7)
        fila = []
        for bit in binario:
            fila.append(int(bit))
        # Agrego Bit de paridad de la fila (LRC)
        paridad = sum(fila) % 2
        fila.append(paridad)
        matriz.append(fila)

    # Generamos la fila de VRC
    control = []
    for columna in range(7):
        suma = 0
        for fila in matriz:
            suma += fila[columna]

        control.append(suma % 2)

    # Bit de paridad cruzada (al final de la VRC)
    paridad_cruzada = sum(control) % 2
    control.append(paridad_cruzada)

    # La fila de control va primera
    matriz.insert(0, control)

    # Convertimos cada fila de 8 bits en un byte
    resultado = bytearray()

    for fila in matriz:
        binario = ""
        for bit in fila:
            binario += str(bit)
        resultado.append(int(binario, 2))

    return matriz, resultado

#se toma el arreglo de enteros y se convierte cada byte a 8 bits, que formaran de nuevo la misma matriz (ya vienen incluidos la fila VRC + bite cruzado y al final de cada ascii de 7 bits esta el bit 8 de LRC)
#se verifica cuantas filas y columnas tienen falla de paridad, guardando su indice
#si es 1 sola interseccion, se va a la interseccion y se corrige de forma inmediata haciendo la inversion del bit
#si es mas de una o solo hay filas o columnas con fallas sin interseccion, no se puede corregir
#por ultimo se recupera el mensaje recorriendo la matriz desde la fila 1 hasta la columna 6 (los primeros 7 bits son el Ascii del caracter)

def decodificar(secuencia):
    if not secuencia:
        return ""
    
    matriz = []
    # Convertimos cada byte a 8 bits
    for byte in secuencia:
        binario = bin(byte)[2:].zfill(8)
        fila = []
        for bit in binario:
            fila.append(int(bit))
        matriz.append(fila)

    filas_error = []
    columnas_error = []
    # Verificamos las filas
    for i in range(len(matriz)):
        if sum(matriz[i]) % 2 != 0:
            filas_error.append(i)
    # Verificamos las columnas
    for columna in range(8):
        suma = 0
        for fila in range(len(matriz)):
            suma += matriz[fila][columna]
        if suma % 2 != 0:
            columnas_error.append(columna)

    # Caso 1: no hay errores
    if len(filas_error) == 0 and len(columnas_error) == 0:
        pass

    # Caso 2: un unico error -> se puede corregir
    elif len(filas_error) == 1 and len(columnas_error) == 1:
        fila = filas_error[0]
        columna = columnas_error[0]
        if matriz[fila][columna] == 0:
            matriz[fila][columna] = 1
        else:
            matriz[fila][columna] = 0

    # Caso 3: errores que no podemos corregir
    else:
        return ""

    # Recuperamos el mensaje ASCII
    mensaje = ""

    # Empezamos desde 1 porque la fila 0 es de control
    for i in range(1, len(matriz)):
        binario = ""
        # Solo los primeros 7 bits son ASCII
        for j in range(7):
            binario += str(matriz[i][j])
        numero = int(binario, 2)
        mensaje += chr(numero)

    return mensaje

mensaje = "CASA"

matriz, codificado = codificar(mensaje)
print(matriz)

print("Codificado:")
print(list(codificado))

decodificado = decodificar(codificado)

print("Decodificado:")
print(decodificado)


#Se genera una matriz de bits para realizar las operaciones, transformando la secuencia de bytes en una lista de cadenas de
#caracteres binarias y despues cada cadena de caracteres se transforma en el numero entero que representan esos bits
#Se puede detectar multiples errores pero solo corregir 1 de forma univoca.