import os
DESC_MIEMBRO = 0.05
DESC_MONTO_MIEMBRO = 0.1
MEMBER = "SI"

while True:
    try:
        print("**Bienvenido a la Tienda en línea")
        monto_compra = float(input("Digite el monto de la compra: $"))
        es_miembro = input("¿Es usted miembro del club? (Sí/No): ").strip().upper()
        if monto_compra > 1000 and es_miembro == MEMBER:
            print("Felicidades, usted tiene descuento del 10%")
            print(f"Subtotal sin descuento: ${monto_compra}")
            descuento = monto_compra * DESC_MONTO_MIEMBRO
            print(f"Monto del descuento: ${descuento}")
            print(f"Total a pagar: ${monto_compra - descuento}")
        elif monto_compra < 1000 and es_miembro == MEMBER:
            print("Felicidades, usted tiene descuento del 5%")
            print(f"Subtotal sin descuento: ${monto_compra}")
            descuento = monto_compra * DESC_MIEMBRO
            print(f"Monto del descuento: ${descuento}")
            print(f"Total a pagar: ${monto_compra - descuento}")
            
        else:
            print("Lo sentimos, no cumple las condiciones para obtener un descuento")
            print(f"Total a pagar: ${monto_compra}")
        os.system("pause")
        os.system("cls")
    except ValueError:
        print("Error al ingresar el monto de la compra")
        os.system("pause")
        os.system("cls")
        continue
    except KeyboardInterrupt:
        print("\nPrograma terminado")
        break

        
