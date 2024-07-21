bc = float(input("Ingrese la medida de BC en cm: "))
cd = float(input("Ingrese la medida de CD en cm: "))
da = float(input("Ingrese la medida de DA en cm: "))

# Convertir cm a metros
bc_m = bc / 100
cd_m = cd / 100
da_m = da / 100

# Calcular las varillas necesarias para el perímetro
perimetro = bc_m + cd_m + da_m + da_m  # 2*da para ambos lados mayores

# Calcular las diagonales usando el teorema de Pitágoras (manual)
ab_m = (bc_m**2 + da_m**2)**0.5  # Diagonal mayor
dc_m = cd_m  # Diagonal menor (ya dada)

# Varillas totales necesarias para un cometa
varillas_por_cometa = perimetro + ab_m + dc_m

# Calcular el área del cometa (Área del rombo: 1/2 * Diagonal mayor * Diagonal menor)
area_cometa = 0.5 * ab_m * dc_m

# Calcular el papel necesario para un cometa (con un 10% adicional para la cola)
papel_por_cometa = area_cometa * 1.10

# Calcular para 10 cometas
varillas_totales = varillas_por_cometa * 10
papel_total = papel_por_cometa * 10

# Imprimir los resultados
print(f"Para la fabricación de 10 cometas se necesitan:")
print(f"{varillas_totales:.2f} metros de varillas de plástico.")
print(f"{papel_total:.2f} metros cuadrados de papel de alta resistencia.")