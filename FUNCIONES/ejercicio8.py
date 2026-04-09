def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

base = float(input("Ingrese el valor de la base: "))
altura = float(input("Ingrese el valor de la altura: "))


resultado = calcular_area_rectangulo(base, altura)
print(f"El area del rectangulo es: {resultado}")