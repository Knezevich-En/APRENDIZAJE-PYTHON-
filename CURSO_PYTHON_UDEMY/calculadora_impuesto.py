def calculadora_impuesto(pago_sin_impuesto, porcentaje_impuesto):
    pago_impuesto = pago_sin_impuesto * (porcentaje_impuesto/100)
    total = pago_sin_impuesto + pago_impuesto
    return total


print("Bienvenido a la calculadora de impuestos")
print("1. Calcular impuesto")
print("2. Salir")

while True:
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        pago_sin_impuesto = float(input("Ingrese el pago sin impuesto: "))
        porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))
        total = calculadora_impuesto(pago_sin_impuesto, porcentaje_impuesto)
        print(f"El total con impuesto es: {total}")
    elif opcion == 2:
        break