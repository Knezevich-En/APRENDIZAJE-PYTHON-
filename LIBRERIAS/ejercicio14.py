import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

respuesta = requests.get(url)

datos_pokemon = respuesta.json()

print(f"El nombre del pokemon es: {datos_pokemon['name']}, su altura es: {datos_pokemon['height']} y su peso es: {datos_pokemon['weight']}")