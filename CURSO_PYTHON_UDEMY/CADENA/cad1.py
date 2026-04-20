print(f"*** GENERADOR DE EMAIL ***")
nombre = input("Nombre de Usuario: ")
nombre = nombre.lower()
nombre_lista = nombre.split(" ")
nombre = ".".join(nombre_lista)
print(f"Nombre Usuario Normalizado: {nombre}\n")

nombre_empresa = input("Nombre de la empresa: ")
nombre_empresa = nombre_empresa.lower()
nombre_empresa = nombre_empresa.replace(" ", "")
extension = input("Extension del dominio: ").strip()
print(f"Dominio de email normalizado: @{nombre_empresa}{extension}\n")

email = f"{nombre}@{nombre_empresa}{extension}"
print(f"Email Generado: {email}")