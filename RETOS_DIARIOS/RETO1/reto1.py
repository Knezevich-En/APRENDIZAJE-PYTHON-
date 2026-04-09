import requests 
import pandas as pd
respuesta =  requests.get("https://jsonplaceholder.typicode.com/users")
datos = respuesta.json()
nombres = []
correos = []
ciudad = []

print("Guardando en listas independientes...")

for i in range(len(datos)):
    print(f"Dato# {i+1}: {datos[i]} \n")
    nombres.append(datos[i]["name"])
    correos.append(datos[i]["email"])
    ciudad.append(datos[i]["address"]["city"])

print("\nListas guardadas exitosamente")
print(f"Nombres: {nombres}")
print(f"Correos: {correos}")
print(f"Ciudades: {ciudad}")

print("\n Creando Diccionario Maestro...")

diccionario_maestro = {
    "nombres": nombres,
    "correos": correos,
    "ciudades": ciudad
}

df = pd.DataFrame(diccionario_maestro)
print("\nDataFrame creado exitosamente")
print(df)

print("\n Generando un archivo EXCEL...")

df.to_excel("EJERCICIOS_PYTHON\\RETOS_DIARIOS\\usuarios.xlsx", index=False)

print("\nArchivo Excel generado exitosamente")



