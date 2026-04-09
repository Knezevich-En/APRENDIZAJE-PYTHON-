import os
contenido = os.listdir("EJERCICIOS_PYTHON\\CIENCIA_DATOS")
print(contenido)

for archivo in contenido:
    if archivo.endswith(".csv") or archivo.endswith(".xlsx"):
        print(archivo)
    else:
        continue