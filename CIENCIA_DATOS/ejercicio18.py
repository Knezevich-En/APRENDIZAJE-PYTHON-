import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("EJERCICIOS_PYTHON\\CIENCIA_DATOS\\empleados_actualizados.csv")
print(df)

plt.bar(df["Empleado"], df["Total"], color="green")
plt.title("Total de ingresos por empleado")
plt.xlabel("Empleado")
plt.ylabel("Total")
plt.grid()
plt.show()