lecturas = []

for i in range(5):
    voltaje = float(input(f"Ingrese el voltaje de la lectura {i+1}: "))
    lecturas.append(voltaje)

promedio = sum(lecturas) / len(lecturas)
print(f"El promedio de las lecturas es: {promedio}")
mayor_voltaje = max(lecturas)
menor_voltaje = min(lecturas)
print(f"El mayor voltaje es: {mayor_voltaje}")
print(f"El menor voltaje es: {menor_voltaje}")