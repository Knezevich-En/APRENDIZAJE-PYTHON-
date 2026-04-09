objetivo = input("¿Cuál es tu objetivo?: ")

with open("EJERCICIOS_PYTHON\\ARCHIVOS\\mis_metas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(objetivo + "\n")

print("Objetivo guardado correctamente...")