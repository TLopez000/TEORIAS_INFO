import compresion

def imprimeByteArray(bytearray):
    datos = [];
    for i in range(0, len(bytearray), 2):
        caracter = chr(bytearray[i])
        numero = bytearray[i+1]

        datos.append(caracter)
        datos.append(numero)
    print(datos)

mensaje1= "XXXYZZZZ"
mensaje2= "AAAABBBCCDAA"
mensaje3= "UUOOOOAAAIEUUUU"

codificado1 = compresion.comprimir_RLC(mensaje1)
codificado2 = compresion.comprimir_RLC(mensaje2)
codificado3 = compresion.comprimir_RLC(mensaje3)

imprimeByteArray(codificado1)
imprimeByteArray(codificado2)
imprimeByteArray(codificado3)

print("tasa compresion 1: ", compresion.tasa_compresion(mensaje1, codificado1))
print("tasa compresion 2: ", compresion.tasa_compresion(mensaje2, codificado2))
print("tasa compresion 3: ", compresion.tasa_compresion(mensaje3, codificado3))