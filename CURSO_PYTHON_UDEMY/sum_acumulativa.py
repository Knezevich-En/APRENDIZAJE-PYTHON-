num_min = int(input("Ingrese el primer numero: "))
num_max = int(input("Ingrese el segundo numero: "))
sum = 0


while num_min <= num_max:
    sum += num_min 
    num_min += 1 
print("La suma acumulada es: ", sum)