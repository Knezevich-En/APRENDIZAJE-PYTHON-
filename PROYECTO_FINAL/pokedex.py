import requests
while True:
    try:
        pokemon = input("¿Qué pokemon quieres saber? (Escribe 'salir' para terminar): ")
        if pokemon.lower() == "salir":
            break
        else:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
            respuesta  = requests.get(url)
            datos = respuesta.json()
            nombre = datos["name"]
            peso = datos["weight"]
            altura = datos["height"]
            print(f"Nombre: {nombre}")
            print(f"Peso: {peso}")
            print(f"Altura: {altura}")
            with open("EJERCICIOS_PYTHON\\PROYECTO_FINAL\\mis_capturas.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"Pokemon atrapado: {nombre}, Peso: {peso}, Altura: {altura}\n")
        
    except KeyboardInterrupt:
        print("\nSaliendo del programa")
        break
    except:
        print("Pokemon no encontrado")

"""
with open("EJERCICIOS_PYTHON\\PROYECTO_FINAL\\mis_capturas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"Pokemon atrapado: {nombre}, Peso: {peso}, Altura: {altura}\n")
"""