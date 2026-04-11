import pandas as pd
import matplotlib.pyplot as plt
gastos = {
    "Departamento": ["Sistemas", "Marketing", "Ventas", "Investigación"],
    "Monto": [1000, 2000, 3000, 4000]
}

df = pd.DataFrame(gastos)
df.to_csv("EJERCICIOS_PYTHON/RETOS_DIARIOS/RETO4/presupuesto_marzo.csv", index=False)
print(df)

plt.bar(df["Departamento"], df["Monto"], color="green")
plt.title("Presupuesto por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Monto")
plt.savefig("EJERCICIOS_PYTHON/RETOS_DIARIOS/RETO4/grafico_reporte.png")