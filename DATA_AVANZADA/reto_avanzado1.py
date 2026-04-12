import pandas as pd

num_id = []
nombres = []
ventas = []

with open("DATA_AVANZADA\\reporte_sucio.txt", "r") as archivo:
    
    lineas = archivo.readlines()
    print(lineas)
    for linea in lineas:
        if linea.startswith("+"):
            continue
        elif linea.startswith("|"):
            partes = linea.split("|")
            print(partes)
            partes.pop(0)
            partes.pop(-1)
            num_id.append(partes[0].strip().title())
            nombres.append(partes[1].strip().title())
            ventas.append(partes[2].strip())
        

num_id.pop(0)
nombres.pop(0)
ventas.pop(0)

df = {
    "ID_EMP": num_id,
    "NOMBRE_EMPLE": nombres,
    "VENTAS_US": ventas
}

df = pd.DataFrame(df)

df["VENTAS_US"] = df["VENTAS_US"].astype(float)
print(df)

df.to_excel("DATA_AVANZADA\\reporte_limpio.xlsx", index=False)
        

        