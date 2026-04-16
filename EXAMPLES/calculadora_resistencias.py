colores = {
    "negro": 0,
    "marron": 1,
    "rojo": 2,
    "naranja": 3,
    "amarillo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "gris": 8,
    "blanco": 9
}

multiplicadores = {
    "negro": 1,
    "marron": 10,
    "rojo": 100,
    "naranja": 1000,
    "amarillo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "gris": 100000000,
    "blanco": 1000000000
}

tolerancias = {
    "rojo": 2,
    "dorado": 5,
    "plateado": 10
}

while True:
    try:
        banda1 = input("Ingrese el color de la primera banda: ")
        banda1 = banda1.lower().strip()
        banda2 = input("Ingrese el color de la segunda banda: ")
        banda2 = banda2.lower().strip()
        multiplicador = input("Ingrese el color del multiplicador: ")
        multiplicador = multiplicador.lower().strip()
        tolerancia = input("Ingrese el color de la tolerancia: ")
        tolerancia = tolerancia.lower().strip()

        if banda1 not in colores or banda2 not in colores or multiplicador not in multiplicadores or tolerancia not in tolerancias:
            print("Error: El valor ingresado no es un color válido.")
            continue
       
        
        print(f"Banda 1: {colores[banda1]}")
        print(f"Banda 2: {colores[banda2]}")
        print(f"Multiplicador: {multiplicadores[multiplicador]}")
        print(f"Tolerancia: {tolerancias[tolerancia]}")
        
        

        color1 = colores[banda1]
        color2 = colores[banda2]
        multi = multiplicadores[multiplicador]
        tolerancia = tolerancias[tolerancia]

        resistencia = (color1 * 10 + color2) * (multi)
        print(f"La resistencia es de {resistencia} Ohms +/- {tolerancia} Ohms")

    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break
