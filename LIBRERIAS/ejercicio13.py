import random

ejercicios = ["flexiones", "sentadillas", "abdominales"]
ejercicio_elegido = random.choice(ejercicios)
repeticiones = random.randint(10, 20)
print(f"Tu ejercicio de hoy es: {ejercicio_elegido} y debes hacer {repeticiones} repeticiones.")

print("¡Vamos con todo!")