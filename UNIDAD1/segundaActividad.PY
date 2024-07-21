nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

total_entradas = 0
total_costo = 0
masculino_count = 0
femenino_count = 0
otro_count = 0
bandera = True

while bandera:
        print("Escoje tu Género: ")
        print("1. MASCULINO")
        print("2. FEMENINO")
        print("3. OTRO")
        opcion_genero = input("Ingrese su opción: ")

        if opcion_genero == "1":
            genero = "MASCULINO"
            masculino_count += 1
        elif opcion_genero == "2":
            genero = "FEMENINO"
            femenino_count += 1
        elif opcion_genero == "3":
            genero = "OTRO"
            otro_count += 1
        else:
            print("Opción no válida.")
            continue

        print("Seleccione el tipo de entrada:")
        print("1. General 16000")
        print("2. Campo delantero 25000")
        print("3. Platea 30000")
        opcion_entrada = input("Ingrese el número de su opción: ")

        if opcion_entrada == "1":
            costo = 16000
        elif opcion_entrada == "2":
            costo = 25000
        elif opcion_entrada == "3":
            costo = 30000
        else:
            print("Opción no válida.")
            continue

        total_entradas += 1

        print("Seleccione el medio de pago:")
        print("1. Crédito")
        print("2. Efectivo")
        print("3. Débito")
        medio_pago = input("Ingrese su opción: ")

        if medio_pago == "1":
            descuento = 0.20
            print("Tienes un descuento del 20%")
        elif medio_pago == "2":
            descuento = 0.15
            print("Tienes un descuento del 15%")
        else:
            descuento = 0.0

        total = total_entradas * costo

        if descuento > 0:
            total_pagar = total - (total * descuento)
        else:
            total_pagar = total

        agregar_otra = input("¿Quiere agregar otra entrada? sí/no: ").strip().upper()

        if agregar_otra != "SI":
            if masculino_count > femenino_count and masculino_count > otro_count:
                genero_comun = "MASCULINO"
            elif femenino_count > masculino_count and femenino_count > otro_count:
                genero_comun = "FEMENINO"
            else:
                genero_comun = "OTRO"

            print(f"Total de entradas a comprar: {total_entradas}")
            print(f"Total acumulado: {total_pagar}")
            print(f"El género más común entre los compradores es: {genero_comun}")
            bandera = False