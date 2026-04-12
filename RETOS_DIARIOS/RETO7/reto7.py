from datetime import datetime

ahora = datetime.now()
print(ahora)
hora_limpia = ahora.strftime("%Y-%m-%d_%H-%M-%S")
ruta = f"RETOS_DIARIOS\\RETO7\\reporte_{hora_limpia}.txt"

with open(ruta, "w") as archivo:
    archivo.write(f"Hola este es una mensaje de prueba {hora_limpia}")
print(f"Reporte creado en: {ruta}")