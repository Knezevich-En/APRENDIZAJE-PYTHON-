with open("EJERCICIOS_PYTHON\\ARCHIVOS\\mis_metas.txt", "r", encoding="utf-8") as archivo:
    todo = archivo.readlines()

print("Hola Arturo, recuerda porque estamos aquí: ")

for i in range(len(todo)):
    print(f"-> Meta {i + 1}: {todo[i].strip()}")

print("¡Vamos con todo!")