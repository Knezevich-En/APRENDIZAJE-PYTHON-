while True:
    try: 
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente == "salir":
            print("Gracias por usar el sistema de descuentos :) ...")
            break
        cantidad_articulos = int(input("Ingrese la cantidad de articulos: "))
        memberia = input("¿Es cliente VIP? (si/no): ").lower().strip()
        if cantidad_articulos >=10 and memberia == "si":
            print("Tienes acceso al descuento VIP...")
        else:
            print("No tienes acceso al descuento VIP...")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario")
        print("Gracias por usar el sistema de descuentos :) ...")
        break
    except ValueError:
        print("Error: El valor ingresado no es un numero")
        