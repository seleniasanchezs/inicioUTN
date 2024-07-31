# En un gimnasio se necesita un programa que permita ingresar datos de 20 socios Por cada socio, se
# ingresa:
# • Nombre completo.
# • Tarifa Base (10000, no se podrá ingresar otro valor)
# • Altura (en centímetros, mayor a 100 y menor a 250).
# • Peso (en kilogramos, mayor a 30 y menor a 200).
# • Rutina de entrenamiento: Debe elegir entre las opciones "Cardio", "Musculación" o
# "Funcional".

# Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por
# print):
# Los socios que realicen:
# ● Musculación, tendrán un incremento del 10%.
# ● Cardio, tendrán incremento del 10%.
# ● Funcional, un descuento del 10%

# A. Por el número de DNI del alumno: 
# Terminados en 4 o 5:
# ● Informar la cantidad total de socios que realizan “Funcional” y su altura es
# superior a “165”.
# ● El promedio total recaudado de los socios que realizan “Musculación” y su altura
# es superior a “110”.
# ● El nombre y la altura del socio que realiza “Cardio” de menor peso.


# Lista para almacenar los datos de los socios
socios = []

# Ingresar datos de 20 socios
for i in range(2):  # Cambia el 2 por 20 cuando ingreses los datos para 20 socios
    print(f"Ingresando datos del socio {i+1}:")
    socio = {}  # Crear un diccionario para almacenar la información de un socio
    
    # Ingresar y almacenar el nombre completo del socio
    socio['nombre_completo'] = input("Ingrese el nombre completo del socio: ")
    
    # La tarifa base es siempre 10000
    socio['tarifa_base'] = 10000
    
    # Ingresar y verificar la altura
    while True:
        altura = int(input("Ingrese la altura en centímetros (mayor a 100 y menor a 250): "))
        if 100 < altura < 250:
            socio['altura'] = altura
            break
        else:
            print("Altura fuera de rango. Intente nuevamente.")
    
    # Ingresar y verificar el peso
    while True:
        peso = int(input("Ingrese el peso en kilogramos (mayor a 30 y menor a 200): "))
        if 30 < peso < 200:
            socio['peso'] = peso
            break
        else:
            print("Peso fuera de rango. Intente nuevamente.")
    
    # Ingresar y verificar la rutina de entrenamiento
    while True:
        rutina = input("Ingrese la rutina de entrenamiento (Cardio, Musculación, Funcional): ").capitalize()
        if rutina in ["Cardio", "Musculación", "Funcional"]:
            socio['rutina'] = rutina
            break
        else:
            print("Rutina no válida. Intente nuevamente.")
    
    # Ingresar y verificar el DNI
    while True:
        dni = input("Ingrese el número de DNI: ")
        if dni.isdigit():
            socio['dni'] = dni
            break
        else:
            print("DNI no válido. Intente nuevamente.")
    
    # Agregar el socio a la lista
    socios.append(socio)

# Calcular el incremento o descuento en la tarifa
for socio in socios:
    if socio['rutina'] in ["Cardio", "Musculación"]:
        socio['tarifa_final'] = socio['tarifa_base'] * 1.10  # Incremento del 10%
    elif socio['rutina'] == "Funcional":
        socio['tarifa_final'] = socio['tarifa_base'] * 0.90  # Descuento del 10%

# Filtrar socios por los criterios especificados
funcional_altura = [socio for socio in socios if socio['rutina'] == "Funcional" and socio['altura'] > 165 and (socio['dni'].endswith('4') or socio['dni'].endswith('5'))]
musculacion_altura = [socio for socio in socios if socio['rutina'] == "Musculación" and socio['altura'] > 110 and (socio['dni'].endswith('4') or socio['dni'].endswith('5'))]

# Encontrar el socio que realiza "Cardio" con el menor peso
cardio_menor_peso = None
for socio in socios:
    if socio['rutina'] == "Cardio" and (cardio_menor_peso is None or socio['peso'] < cardio_menor_peso['peso']) and (socio['dni'].endswith('4') or socio['dni'].endswith('5')):
        cardio_menor_peso = socio

# Mostrar los resultados
print("\nResultados:")
print(f"Cantidad de socios que realizan 'Funcional' y su altura es superior a 165: {len(funcional_altura)}")

if len(musculacion_altura) > 0:
    promedio_recaudado = sum(socio['tarifa_final'] for socio in musculacion_altura) / len(musculacion_altura)
    print(f"Promedio total recaudado de los socios que realizan 'Musculación' y su altura es superior a 110: {promedio_recaudado}")
else:
    print("No hay socios que cumplen con los criterios para 'Musculación'.")

if cardio_menor_peso:
    print(f"El nombre del socio que realiza 'Cardio' de menor peso es {cardio_menor_peso['nombre_completo']} y su altura es {cardio_menor_peso['altura']}")
else:
    print("No hay socios que cumplen con los criterios para 'Cardio'.")
