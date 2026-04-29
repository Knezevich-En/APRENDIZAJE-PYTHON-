def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        numero = num * factorial(num - 1)
        return numero


resultado = factorial(0)
print("Resultado final: ", resultado)