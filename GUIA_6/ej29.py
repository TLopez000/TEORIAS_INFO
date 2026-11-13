import tipocanal

matriz_canal = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.3, 0.3, 0.4]
]

probabilidades_a_priori = [1/3, 1/3, 1/3]
print(f"Probabilidad de error: {tipocanal.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")

print()

probabilidades_a_priori = [1/8, 3/8, 4/8]
print(f"Probabilidad de error: {tipocanal.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")

print()

probabilidades_a_priori = [4/15, 3/15, 8/15]
print(f"Probabilidad de error: {tipocanal.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")