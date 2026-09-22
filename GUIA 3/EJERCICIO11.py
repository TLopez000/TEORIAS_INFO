from AlfabetoProbsKraft_Codigos import obtener_alfabeto, obtener_longitudes_codigo
from EntropiaFuente import long_media, calcula_entropia_baseR

codigo_A = ["==", "<", "<=", ">", ">=", "<>"]
codigo_B = [")", "[]", "]]", "([", "[()]","([)]"]
codigo_C = ["/", "*", "-", "*", "++","+-"]
codigo_D = [".,", ";", ",,", ":", "...",",:;"]

probabilidades = [0.10,0.5,0.1,0.2,0.05,0.05]

alfabeto = obtener_alfabeto(codigo_B)
longitudes = obtener_longitudes_codigo(codigo_A)
baseR = len(alfabeto)

entropiafuente = calcula_entropia_baseR(baseR, probabilidades)
longitudprom = long_media(probabilidades, longitudes)

print(entropiafuente)
print(longitudprom)

#Un codigo necesita como minimo la informacion necesaria promedio para representar la fuente (su entropia o mas)
#Cuanto mas eficiente sea el codigo, mas se acerca a la entropia