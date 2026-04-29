def es_par(num):
    if num% 2 == 0:
        return True
    else:
        return False

# Llamar a la funcion
if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    print(f"El numero {numero} es par: {es_par(numero)}")