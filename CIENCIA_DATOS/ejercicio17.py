import pandas as pd

df = pd.read_csv("EJERCICIOS_PYTHON\\CIENCIA_DATOS\\empleados_actualizados.csv")
empleados_top = df[df["Total"] >= 2000]
print(empleados_top)

empleados_top.to_excel("EJERCICIOS_PYTHON\\CIENCIA_DATOS\\empleados_altos_ingresos.xlsx", index=False)
print("\nArchivo Excel creado exitosamente.")