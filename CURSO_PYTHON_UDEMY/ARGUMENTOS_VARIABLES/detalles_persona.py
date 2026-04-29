def mostrar_detalles(**kwargs):
    print("Detalles de la persona:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_detalles(nombre="Juan", edad=25, profesion="Ingeniero")