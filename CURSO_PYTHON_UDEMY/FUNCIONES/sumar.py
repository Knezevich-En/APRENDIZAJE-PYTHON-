import modulo_operaciones_basicos as mdop
#from modulo_operaciones_basicos import sumar, restar, multiplicacion, division

print("""
        *** Bienvenido al sistema de calculadora básica ***
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Salir
        """)

while True:
    try:
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            print(f"La suma de {num1} y {num2} es: {mdop.sumar(num1, num2)}")
        elif opcion == 2:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            print(f"La resta de {num1} y {num2} es: {mdop.restar(num1, num2)}")
        elif opcion == 3:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            print(f"La multiplicacion de {num1} y {num2} es: {mdop.multiplicacion(num1, num2)}")
        elif opcion == 4:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            print(f"La division de {num1} y {num2} es: {mdop.division(num1, num2)}")
        elif opcion == 5:
            print("Hasta luego...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")
            continue

    except ValueError:
        print("Error: Ingrese un valor válido.")
        continue

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
        break