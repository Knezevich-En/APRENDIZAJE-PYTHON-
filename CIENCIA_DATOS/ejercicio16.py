import pandas as pd

df = pd.read_csv("EJERCICIOS_PYTHON\\CIENCIA_DATOS\\empleados.csv")
print(df)

df["Bono"] = df["Sueldo"] * 0.10
print(df)

df["Total"] = df["Sueldo"] + df["Bono"]
print(df.describe())

print(df)

df.to_csv("EJERCICIOS_PYTHON\\CIENCIA_DATOS\\empleados_actualizados.csv", index=False)
print("\nArchivo CSV creado exitosamente.")