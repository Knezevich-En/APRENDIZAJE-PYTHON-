usuario_registrado = ""
contraseña_registrada = ""

while True:
    try:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        if usuario == usuario_registrado and contraseña == contraseña_registrada:
            print("Usuario y contraseña correctos")
            break
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        break