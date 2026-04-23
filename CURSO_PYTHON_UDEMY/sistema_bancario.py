print("**Sistema Bancario**")
while True:
    try:
        print("Menu Principal")
        print("1. Retirar")
        print("2. Depositar")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print("Retirar dinero")
        elif opcion == "2":
            print("Depositar dinero")
        elif opcion == "3":
            print("Salir")
            break
    except ValueError:
        print("Opcion no valida")
        os.system("pause")
        os.system("cls")
        continue
    except KeyboardInterrupt:
        print("\nPrograma terminado")
        break    