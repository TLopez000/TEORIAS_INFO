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

