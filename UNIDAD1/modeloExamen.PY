contador = 1
contador_subasta = 0
usuario_mas_joven_nombre = ""
usuario_mas_joven_edad = None
usuario_mas_joven_tipo = ""
total_publicaciones = 0
publicaciones_inactivas = 0
total_edad_subasta = 0
contador_subasta_publicaciones = 0
productos_inactivos = 0
servicios_inactivos = 0
subastas_inactivos = 0

while contador <= 10:
    nombre_usuario = input("Nombre del usuario: ")

    while True:
        try:
            edad_usuario = int(input("Edad del usuario (entre 18 y 100): "))
            if 18 <= edad_usuario <= 100:
                break
            else:
                print("La edad no es válida, debe estar entre 18 y 100 años.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    while True:
        try:
            cantidad_productos = int(input("Cantidad de productos (número entero positivo): "))
            if cantidad_productos > 0:
                break
            else:
                print("Cantidad inválida, debe ser un número entero positivo.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    while True:
        try:
            numero_publicaciones = int(input("Número de publicaciones (número entero positivo, hasta 1000): "))
            if 1 <= numero_publicaciones <= 1000:
                break
            else:
                print("Número de publicaciones inválido, debe ser un número entero positivo hasta 1000.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    while True:
        tipo_publicacion = input("Tipo de publicación (producto, servicio, subasta): ").lower()
        if tipo_publicacion in ["producto", "servicio", "subasta"]:
            break
        else:
            print("Tipo inválido, debe ser 'producto', 'servicio' o 'subasta'.")

    while True:
        cuenta_activa = input("¿Cuenta activa? (si/no): ").lower()
        if cuenta_activa in ["si", "no"]:
            break
        else:
            print("Entrada inválida, debe ser 'si' o 'no'.")

    if cuenta_activa == "si" and tipo_publicacion == "subasta" and edad_usuario > 60:
        contador_subasta += 1
    
    if numero_publicaciones < 300:
        if usuario_mas_joven_edad is None or edad_usuario < usuario_mas_joven_edad:
            usuario_mas_joven_nombre = nombre_usuario
            usuario_mas_joven_edad = edad_usuario
            usuario_mas_joven_tipo = tipo_publicacion
    
    total_publicaciones += numero_publicaciones
    if cuenta_activa == "no":
        publicaciones_inactivas += numero_publicaciones
        if tipo_publicacion == "producto":
            productos_inactivos += numero_publicaciones
        elif tipo_publicacion == "servicio":
            servicios_inactivos += numero_publicaciones
        elif tipo_publicacion == "subasta":
            subastas_inactivos += numero_publicaciones
    
    if tipo_publicacion == "subasta":
        total_edad_subasta += edad_usuario
        contador_subasta_publicaciones += 1
    
    contador += 1

print("Cantidad de usuarios con cuenta activa, tipo 'subasta' y edad mayor a 60 años:", contador_subasta)

if usuario_mas_joven_nombre:
    print("Nombre y tipo del usuario de menor edad con menos de 300 publicaciones:", usuario_mas_joven_nombre, "(", usuario_mas_joven_tipo, ")")
else:
    print("No se encontró ningún usuario con menos de 300 publicaciones.")

if total_publicaciones > 0:
    porcentaje_inactivo = (publicaciones_inactivas / total_publicaciones) * 100
else:
    porcentaje_inactivo = 0

print("Porcentaje de publicaciones inactivas:", porcentaje_inactivo, "%")

if contador_subasta_publicaciones > 0:
    promedio_edad_subasta = total_edad_subasta / contador_subasta_publicaciones
else:
    promedio_edad_subasta = 0

print("Promedio de edad de los usuarios con publicaciones tipo 'subasta':", promedio_edad_subasta, "años")

if productos_inactivos >= servicios_inactivos and productos_inactivos >= subastas_inactivos:
    tipo_con_mas_inactivas = "producto"
elif servicios_inactivos >= productos_inactivos and servicios_inactivos >= subastas_inactivos:
    tipo_con_mas_inactivas = "servicio"
else:
    tipo_con_mas_inactivas = "subasta"

print("Tipo con más publicaciones inactivas:", tipo_con_mas_inactivas)
