import compresion
import metricasEficiencia
import codifica_decodifica

alfabeto = [
  " ", ",", ".", ":", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
  "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

probs = [
  0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
  0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
  0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
  0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199,
]

codigo_huffman = compresion.huffman(probs)

mensaje = "HOLA JUAN CARLOS COMO ESTAS CHUPA PIJA"

codificado = codifica_decodifica.codificar(alfabeto, codigo_huffman, mensaje)
archivo = open("codificado.bin", "wb")
archivo.write(codificado)
archivo.close()

archivo = open("codificado.bin", "rb")
codificado = archivo.read()
archivo.close()
decodificado = codifica_decodifica.decodificar(alfabeto, codigo_huffman, codificado)
print(decodificado)

metricasEficiencia.metricasEficiencia(probs, codigo_huffman)

print("tasa compresion: ", compresion.tasa_compresion(mensaje, codificado))