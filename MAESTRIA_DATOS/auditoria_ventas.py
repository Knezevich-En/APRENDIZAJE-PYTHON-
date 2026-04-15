import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("MAESTRIA_DATOS\\ventas_sucias.csv")
df = df.drop_duplicates()
df = df.dropna(subset=['ID_VENTA'])
df = df.fillna({'PRODUCTO': ' NaNs '})
df['PRECIO'] = df['PRECIO'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['PRECIO'] = df['PRECIO'].astype(float)
df = df.groupby(['CATEGORIA']).agg({'PRECIO': 'sum'})

plt.bar(df.index, df["PRECIO"])
plt.title("Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Precio")
plt.savefig("reporte.png")
plt.show()
