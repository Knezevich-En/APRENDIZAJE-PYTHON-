USERNAME = "admin"
PASSWORD = "[PASSWORD]"

while True:
    try:
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        if user == USERNAME and password == PASSWORD:
            print("Acceso concedido")
            break
        else:
            print("Acceso denegado")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        break