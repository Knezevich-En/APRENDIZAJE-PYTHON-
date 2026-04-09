import random

numero_secreto = random.randint(1, 10)
intento = 0
while True:
    try:
        intento += 1
        num = int(input("Ingresa un numero del 1 al 10: "))
        if num == numero_secreto:
            print(f"\nEl numero secreto era {numero_secreto}")
            print(f"Felicidades, has adivinado el numero en {intento} intentos")
            break
    except ValueError:
        print("Error, por favor ingresa solamente numeros...")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        break
