# Constante de precio de lámpara
PRECIO_LAMPARA = 800

# Solicitar al usuario la cantidad y marca de las lámparas
cantidad = int(input("Ingrese la cantidad de lámparas: "))
marca = input("Ingrese la marca de las lámparas: ")

# Calcular el total sin descuento
total_sin_descuento = cantidad * PRECIO_LAMPARA

# Inicializar el descuento a 0
descuento = 0

# Aplicar los descuentos basados en la cantidad y marca usando match
match cantidad:
    case _ if cantidad >= 6:
        descuento = 0.50
    case 5:
        if marca == "ArgentinaLuz":
            descuento = 0.40
        else:
            descuento = 0.30
    case 4:
        if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
            descuento = 0.25
        else:
            descuento = 0.20
    case 3:
        if marca == "ArgentinaLuz":
            descuento = 0.15
        elif marca == "FelipeLamparas":
            descuento = 0.10
        else:
            descuento = 0.05

# Calcular el total con el descuento
total_con_descuento = total_sin_descuento * (1 - descuento)

# Aplicar el descuento adicional si el importe final supera los $4000
descuento_adicional = 0
if total_con_descuento > 4000:
    descuento_adicional = 0.05
    total_con_descuento *= (1 - descuento_adicional)

# Calcular el importe del descuento inicial
importe_descuento = total_sin_descuento * descuento

# Calcular el importe del descuento adicional
importe_descuento_adicional = total_con_descuento * descuento_adicional

# Mostrar los resultados
print("\nResultados:")
print(f"Marca: {marca}")
print(f"Cantidad de lámparas: {cantidad}")
print(f"Total a pagar sin descuento: ${total_sin_descuento:.2f}")
print(f"Descuento obtenido: ${importe_descuento:.2f}" if descuento > 0 else "Descuento obtenido: $0.00")
print(f"Descuento adicional: ${importe_descuento_adicional:.2f}" if descuento_adicional > 0 else "Descuento adicional: $0.00")
print(f"Total a pagar con descuento: ${total_con_descuento:.2f}")
