def distanciaHamming(codigo: list[str]):
    dmin = len(codigo[0])

    for i in range(len(codigo)):
        for j in range(i + 1, len(codigo)):
            distancia = 0

            for k in range(len(codigo[i])):
                if codigo[i][k] != codigo[j][k]:
                    distancia += 1

            if distancia < dmin:
                dmin = distancia

    erroresDetectables = dmin - 1
    erroresCorregibles = (dmin-1)/2

    #No se puede corregir una fraccion de error
    if (1>erroresCorregibles>0):
        erroresCorregibles = 0
    
    return dmin, erroresDetectables, erroresCorregibles
        
#EJ 9

cod1=["00","01","10","11"]
cod2=["000","100","101","111"]
cod3=["0000","0011","1010","0101"]

#EJ 10

cod1=["0100100","0101000","0010010","0100000"]
cod2=["0100100","0010010","0101000","0100001"]
cod3=["0110000","0000011","0101101","0100110"]

d1,a1,b1 = distanciaHamming(cod1)
d2,a2,b2 = distanciaHamming(cod2)
d3,a3,b3 = distanciaHamming(cod3)

print("Distancia Hamming: ", d1)
print("Errores detectables ", a1)
print("Errores corregibles: ", b1)
