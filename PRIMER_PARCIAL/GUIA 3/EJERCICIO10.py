from AlfabetoProbsKraft_Codigos import obtener_alfabeto, obtener_longitudes_codigo, inecuacion_kraft

codigo_1 = ["011", "000", "010", "101", "001", "100"]
codigo_2 = ["110", "100", "101", "001", "110", "010"]
codigo_3 = ["10", "1100", "0101", "1011", "0", "110"]
codigo_4 = ["1101", "10", "1111", "1100", "1110", "0"]
codigo_5 = ["011", "0111", "01", "0", "011111", "01111"]
codigo_6 = ["1110", "0", "110", "1101", "1011", "10"]

codigo_A = ["==", "<", "<=", ">", ">=", "<>"]
codigo_B = [")", "[]", "]]", "([", "[()]","([)]"]

alfabeto = obtener_alfabeto(codigo_B)
longitudes = obtener_longitudes_codigo(codigo_B)

kraft = inecuacion_kraft(alfabeto,longitudes)


print(kraft)

#Si kraft > 1, el codigo no puede ser UD y por ende tampoco instantaneo, no hay forma de asignar prefijos sin solapamientos con esa longitud
#Si kraft <= 1, es posible pero no garantiza que sea no singular ni univoco ni instantaneo (puede formarse al menos 1 instantaneo con esas longitudes)
# Un codigo UD siempre cumple la inecuacion.