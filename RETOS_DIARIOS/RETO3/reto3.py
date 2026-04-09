import os

contenido = os.listdir("EJERCICIOS_PYTHON\\RETOS_DIARIOS\\RETO3")
print(contenido)

os.makedirs("EJERCICIOS_PYTHON\\RETOS_DIARIOS\\RETO3\\BANDEJA_SALIDA", exist_ok=True)

clientes = ["Ana", "Luis", "Carlos", "Maria", "Pedro", "Sofia", "Jorge", "Laura", "Miguel", "Fernanda"]




for cliente in clientes:
    ruta_destino = f"EJERCICIOS_PYTHON\\RETOS_DIARIOS\\RETO3\\BANDEJA_SALIDA\\correo_{cliente}.txt"
    mensaje_dinamico = f"Estimado/a {cliente}: ¡Gracias por ser cliente preferencial de nuestra empresa!"
    with open(ruta_destino, "w", encoding="utf-8") as archivo:
        archivo.write(mensaje_dinamico)

print("Se han enviado los correos a los clientes preferenciales, gracias por usar el sistema automatizado! 🤖")
        
    