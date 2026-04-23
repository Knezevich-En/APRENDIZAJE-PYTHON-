invierno = [1, 2, 12]
primavera = [3, 4, 5]
verano = [6, 7, 8]
otono = [9, 10, 11]

try:
    valor = int(input("Digite un mes del año: "))
    if valor in invierno:
        print("Invierno")
    elif valor in primavera:
        print("Primavera")
    elif valor in verano:
        print("Verano")
    elif valor in otono:
        print("Otono")
    else:
        print("Mes no valido")
except ValueError:
    print("Valor no valido")    