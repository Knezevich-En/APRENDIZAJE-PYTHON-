def aplicar_descuento(precio):
    descuento_1 = 0.20
    descuento_2 = 0.10
    if precio > 100:
        descuento_precio = precio * descuento_1
        total = precio - descuento_precio
    elif precio > 50:
        descuento_precio = precio * descuento_2
        total = precio - descuento_precio
    else:
        total = precio
    return total

while True:
    operador = input("Ingrese precio total o 'salir' para terminar sesión:")
    operador = operador.strip().upper()
    if operador == "SALIR":
        print("Gracias por usar el sistema")
        break
    else:
        try:
            precio = float(operador)
            resultado = aplicar_descuento(precio)
            print(f"El valor total de la compra es: ${resultado}")
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
        except KeyboardInterrupt:
            print("\nGracias por usar el sistema")
            break
        