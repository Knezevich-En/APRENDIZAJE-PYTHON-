import os
balance = 1000
while True:
    try:
        print("**Cajero Automatico**")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")

        option = int(input("Seleccione una opcion: "))

        if option == 1:
            print("El saldo actual es: $", balance)
            os.system("pause")
            os.system("cls")
        elif option == 2:
            withdraw = float(input("Ingrese la cantidad a retirar: $"))
            if withdraw > balance:
                print("Saldo insuficiente")
            else:
                balance -= withdraw
                print("Retiro exitoso")
            os.system("pause")
            os.system("cls")
        elif option == 3:
            deposit = float(input("Ingrese la cantidad a depositar: $"))
            balance += deposit
            print("Deposito exitoso")
            os.system("pause")
            os.system("cls")
        elif option == 4:
            print("Gracias por su preferencia")
            break
        else:
            print("Opcion no valida")
            os.system("pause")
            os.system("cls")
    except ValueError:
        print("Opcion no valida")
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
        

    
    