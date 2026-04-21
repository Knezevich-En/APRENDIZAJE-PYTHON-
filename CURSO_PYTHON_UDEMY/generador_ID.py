import random

nombre = input("Ingrese su nombre: ")
apellido  = input("Ingrese su apellido: ")
nacimiento = input("Ingrese su año de nacimiento: ")

cod_nom_ID = nombre[:2].upper()
cod_ape_ID = apellido[:2].upper()
cod_nac_ID = nacimiento[-2:]

valor_aleatorio = random.randint(1000, 9999)

id_unico = cod_nom_ID + cod_ape_ID + cod_nac_ID + str(valor_aleatorio)

print(f"Su ID es: {id_unico}")
