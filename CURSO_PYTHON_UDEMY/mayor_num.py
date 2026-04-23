lista_numeros = []

for i in range(5):
    lista_numeros.append(float(input("Digite un numero: ")))

mayor_numero = max(lista_numeros)
menor_numero = min(lista_numeros)
print(f"El numero mayor es: {mayor_numero}")
print(f"El numero menor es: {menor_numero}")

