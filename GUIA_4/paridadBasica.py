#Agrega bit de paridad PAR al ascii de un caracter (si es par pongo 0 si es impar pongo 1 para que siempre de par la suma de los 1)
def paridadBasica(caracter):
    ascii = ord(caracter)

    unos = 0
    for i in range(7):
        if ascii & (1 << i):
            unos += 1

    paridad = unos % 2
    
    byte = (ascii << 1) | paridad

    return byte


# Verifica si un byte tiene errores de paridad
def verificarParidad(byte):

    paridad_esperada = byte & 1
    ascii = byte >> 1

    unos = 0
    for i in range(7):
        if ascii & (1 << i):
            unos += 1

    paridad = unos % 2

    return paridad_esperada == paridad

byte = paridadBasica("A")

print(format(byte, '08b'))

byte = byte | 0x08 #pongo un 1 en el bit 4 para hacerlo erroneo

print(format(byte, '08b'))

if (verificarParidad(byte)):
    print("Es correcto")
else:
    print("Es erroneo")