
while True:
    try:
        año_nacimiento = int(input("Ingrese su año de nacimiento: "))
        edad = 2026 - año_nacimiento
        print(f"Tienes {edad} años")
        break
    except ValueError:
        print("Error: El valor ingresado no es un número")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        break