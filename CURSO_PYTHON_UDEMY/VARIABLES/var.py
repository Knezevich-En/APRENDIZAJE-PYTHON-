
TARIFA_POR_DIA = 85.50

nombre_cliente = input("Ingrese su nombre por favor: ")
dias_estancia = int(input("Ingrese el numero de dias que desea quedarse: "))

precio_total = TARIFA_POR_DIA * dias_estancia

print("El precio total de la estancia es: ", precio_total)


print("*** Sistema de Reserva de Hoteles ***")
print("Bienvenido", nombre_cliente)
print("Su estancia es de", dias_estancia, "dias")
print("El precio total de la estancia es: ", precio_total)
print("Habitación vista al mar: ", True)
print("Desayuno incluido: ", False)


