### Conclusiones para fuente original y su extension

Al comparar la fuente original con su extensión de orden 3, se puede analizar cómo influye la codificación conjunta de varios símbolos en la eficiencia del código Huffman.

En primer lugar, se observa que la entropía de la extensión es aproximadamente tres veces la entropía de la fuente original, dado que se agrupan bloques de tres símbolos. Por lo tanto, la cantidad de información por símbolo se mantiene.

Por otro lado, al comparar las longitudes promedio por símbolo, se puede determinar si la extensión permite obtener una codificación más eficiente.

Esto también se refleja en el rendimiento: un mayor rendimiento indica que la longitud promedio del código se encuentra más cerca del límite teórico establecido por la entropía.

Finalmente, la redundancia permite observar cuánto espacio adicional se utiliza respecto de la información mínima necesaria. Una disminución de la redundancia por símbolo indica una mejor utilización de los bits disponibles.

En conclusión, la extensión de orden 3 permite evaluar si la codificación de bloques de símbolos logra mejorar el aprovechamiento del código Huffman respecto de la codificación individual.

## Conclusiones para matriz de canal y sus metricas 

A partir del análisis de la matriz del canal, se observa que se trata de un canal asimétrico, ya que las probabilidades de transición dependen del símbolo transmitido.

Se puede observar que, al transmitir el símbolo 0, el receptor obtiene siempre el símbolo 2, por lo que no existe incertidumbre en la salida. En cambio, al transmitir el símbolo 1, existen tres posibles resultados, lo que introduce incertidumbre en la transmisión.

Mediante el cálculo de la distribución óptima de entrada se busca maximizar la información mutua, obteniendo así la capacidad del canal.

Por otro lado, el ruido H(A/B) representa la incertidumbre que tiene el receptor sobre el símbolo original una vez conocida la salida. Esta incertidumbre aparece principalmente cuando se recibe el símbolo 2, ya que este puede provenir de cualquiera de las dos entradas.

La pérdida H(B/A), en cambio, representa la incertidumbre sobre el resultado recibido conociendo el símbolo transmitido. Esta se produce cuando se transmite el símbolo 1, debido a que puede generar diferentes salidas.

Finalmente, la información mutua I(A;B) permite determinar cuánta información del símbolo transmitido logra conservarse en la recepción. Cuanto mayor sea este valor, más información permite transmitir el canal.

EJ DE REGLA DE DECIOSION MAX:
entrada = "10100000101011101001111110011001"
salida =  "QQPQQPPQQQPQRRRQSPQSQRQSQQPSQQPP"
# por la regla de maxima decision, se sabe que si se emitio R o S, entro un 1.
# cuando se recibe Q o P, se decide 0 ya que es el que tiene max probabilidad a posteriori.
# Un 1 transmitido puede producir Q P R S
# Un 0 transmitido solo produce Q P
# Un 0 transmitido nunca se recupera como 1, no puede producir R S
# Un 1 transmitido puede recuperarse incorrectamente como 0 si produce Q o P

mensaje decodificado : "000000000000011101001010100010000"

Como un 0 solo produce Q o P, y ambos se decodifican como 0, nunca se recupera incorrectamente como un 1.
En cambio si se transmite un 1, se puede recuperar incorrectamente como 0, ya que puede producir Q y P pero por la regla se decide 0. 
Puede haber errores de 1 a 0 pero no de 0 a 1.
La corrección por paridad indica que se recupero un 1 donde debería haber un 0. Esto implicaría que durante la transmisión ocurrió un cambio de 0 a 1, que es imposible para este canal. Por lo tanto, bajo la hipótesis de un único error utilizada para la corrección, el mensaje recibido no pudo haberse transmitido por este canal y recuperado mediante la regla de decisión indicada.

