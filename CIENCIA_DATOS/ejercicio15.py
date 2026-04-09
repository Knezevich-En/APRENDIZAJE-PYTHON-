import pandas as pd


mis_datos = {
    "Empleado": ["Ana", "Luis", "Carlos", "María"],
    "Edad": [25, 32, 28, 41],
    "Sueldo": [1500, 2200, 1800, 3100]
}

df = pd.DataFrame(mis_datos)
print(df)

df.to_csv("EJERCICIOS_PYTHON\\CIENCIA_DATOS\\empleados.csv", index=False)

print("\nArchivo CSV creado exitosamente.")