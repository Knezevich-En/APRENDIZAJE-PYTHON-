import shutil
import os

os.makedirs("EJERCICIOS_PYTHON\\AUTOMATIZACION\\REPORTES_ARCHIVADOS", exist_ok=True)

contenido = os.listdir("EJERCICIOS_PYTHON\\CIENCIA_DATOS")
ruta_origen = "EJERCICIOS_PYTHON\\CIENCIA_DATOS"
ruta_destino = "EJERCICIOS_PYTHON\\AUTOMATIZACION\\REPORTES_ARCHIVADOS"

for archivo in contenido:
    if archivo.endswith(".csv") or archivo.endswith(".xlsx"):
        shutil.move(f"{ruta_origen}\\{archivo}", f"{ruta_destino}\\{archivo}")
    else:
        continue

print(f"{len(contenido)} archivos se han movido a {ruta_destino}")
        
