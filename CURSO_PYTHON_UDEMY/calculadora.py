import os
while True:
    print("**CALCULADORA**")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    try:
        opt = int(input("Seleccione una opción: "))
        if opt == 1:
            cantidad_numeros = int(input("Ingrese la cantidad de números a realizar la operación seleccionada: "))
            suma = 0
            for i in range(cantidad_numeros):
                num = float(input("Ingrese un número: "))
                suma += num
            print("La suma es: ", suma)
            os.system("pause")
            os.system("cls")
        elif opt == 2:
            cantidad_numeros = int(input("Ingrese la cantidad de números a realizar la operación seleccionada: "))
            resta = 0
            for i in range(cantidad_numeros):
                num = float(input("Ingrese un número: "))
                resta -= num
            print("La resta es: ", resta*-1)
            os.system("pause")
            os.system("cls")
        elif opt == 3:
            cantidad_numeros = int(input("Ingrese la cantidad de números a realizar la operación seleccionada: "))
            multiplicacion = 1
            for i in range(cantidad_numeros):
                num = float(input("Ingrese un número: "))
                multiplicacion *= num
            print("La multiplicación es: ", multiplicacion)
            os.system("pause")
            os.system("cls")
        elif opt == 4:
            cantidad_numeros = int(input("Ingrese la cantidad de números a realizar la operación seleccionada: "))
            division = 1
            for i in range(cantidad_numeros):
                num = float(input("Ingrese un número: "))
                division /= num
            print("La división es: ", division)
            os.system("pause")
            os.system("cls")
        elif opt == 5:
            print("Gracias por su preferencia")
            break
        else:
            print("Opción no válida")
            os.system("pause")
            os.system("cls")
    except ValueError:
        print("Opción no válida")
        os.system("pause")
        os.system("cls")
        continue
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        os.system("pause")
        os.system("cls")
        continue
    except Exception as e:
        print("Error: ", e)
        os.system("pause")
        os.system("cls")
        continue
    except KeyboardInterrupt:
        print("\nGracias por su preferencia")
        break