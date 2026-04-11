nombres_sucios = [" aRturo ", "  ana", "MARIA ", "juaN", "maRIA         "]
nombres_limpios = []

with open("EJERCICIOS_PYTHON\\RETOS_DIARIOS\\RETO5\\clientes_VIP.txt", "w") as archivo:
    for nombre in nombres_sucios:
        nombres_limpios.append(nombre.strip().capitalize())
        archivo.write(nombre.strip().capitalize() + "\n")


print(nombres_sucios)
print(nombres_limpios)