from escompacto import escompacto
#CODIGOS EJ 8
codigo_A = ["==", "<", "<=", ">", ">=", "<>"]
codigo_B = [")", "[]", "]]", "([", "[()]","([)]"]
codigo_C = ["/", "*", "-", "*", "++","+-"]
codigo_D = [".,", ";", ",,", ":", "...",",:;"]

probabilidades = [0.10,0.5,0.1,0.2,0.05,0.05]

#CODIGOS EJ 13 (VERIFICAR SI SON O NO COMPACTOS MIS CODIGOS)
codigoP = ['0', '10', '110', '111']
probsP = [0.333,0.333,0.167,0.167]

if (escompacto(codigoP,probsP)):
     print("es compacto")
else:
    print("no")