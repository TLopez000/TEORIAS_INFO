import tipocanal

probabilidades_a_priori = [0.5, 0.5]
matriz_canal = [
    [0.6, 0.4],
    [0.2, 0.8]
]

print(f"Probabilidad de error: {tipocanal.obtener_probabilidad_error(probabilidades_a_priori, matriz_canal):.4f}")