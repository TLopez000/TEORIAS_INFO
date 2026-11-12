
""" Recorro el mensaje carácter por carácter.
Busco manualmente la posición de cada carácter en el alfabeto.
Obtengo su código binario y lo concateno en bits.
Recorro bits de a 8 posiciones.
Si el último grupo tiene menos de 8 bits, completo con ceros.
Convierto cada grupo a entero y lo agrego al bytearray."""

# símbolos → palabras código → cadena de 0 y 1 → bytes
def codificar(alfabeto, codificacion, mensaje): 
    mensaje_binario = ""

    # Reemplazamos cada simbolo por su palabra codigo
    for simbolo in mensaje:
        posicion = alfabeto.index(simbolo)
        mensaje_binario += codificacion[posicion]
    
    # Calculamos cuantos bits faltan para completar el ultimo byte
    relleno = (8 - len(mensaje_binario) % 8) % 8
    # Agregamos ceros de relleno
    mensaje_binario += "0" * relleno
    
    # Creamos el bytearray
    resultado = bytearray()
    # El primer byte del resultado indica cuantos bits de relleno agregamos
    resultado.append(relleno)

    # Convertimos cada grupo de 8 bits en un numero
    for i in range(0, len(mensaje_binario), 8):
        bloque = mensaje_binario[i:i + 8]
        resultado.append(int(bloque, 2))
    
    return resultado
    
"""Inicializar una cadena vacía bits.
Recorrer el bytearray y convertir cada byte a binario mediante bin().
Completar cada representación con ceros a la izquierda hasta alcanzar 8 bits.
Recorrer la cadena binaria acumulando bits en codigo.
Comparar codigo con cada elemento de la lista de codificaciones.
Cuando encuentra una coincidencia, agregar el carácter correspondiente al resultado y reiniciar codigo.
Retornar el mensaje decodificado."""


# bytes → cadena de 0 y 1 → palabras código → símbolos
def decodificar(alfabeto, codificacion, secuencia):
    # El primer byte contiene la cantidad de bits de relleno
    relleno = secuencia[0]
    mensaje_binario = ""

    # Convertimos cada byte nuevamente a 8 bits
    for i in range(1, len(secuencia)):
        binario = bin(secuencia[i])[2:]
        binario = binario.zfill(8)
        mensaje_binario += binario

    # Sacamos los ceros de relleno
    if relleno > 0:
        mensaje_binario = mensaje_binario[:-relleno]

    mensaje = ""
    palabra = ""

    # Vamos formando palabras codigo
    for bit in mensaje_binario:
        palabra += bit
        # si ya forme una palabra
        if palabra in codificacion:
            posicion = codificacion.index(palabra)
            mensaje += alfabeto[posicion]
            palabra = ""
    
    return mensaje


alfabeto = ["h", "o", "l", "a", " ", "j", "u", "n", "c", "r", "s"]
codificacion = [
    "0000",  # h
    "0001",  # o
    "0010",  # l
    "0011",  # a
    "0100",  # espacio
    "0101",  # j
    "0110",  # u
    "0111",  # n
    "1000",  # c
    "1001",  # r
    "1010"   # s
]
mensaje = "hola juan carlos"

codificado = codificar(alfabeto, codificacion, mensaje)
decodificado = decodificar(alfabeto, codificacion, codificado)
print(codificado)
print(decodificado)