##**kwars diccionario
def superheroes(superheroe, nombre, **kwargs):
    print(f"Superheroes: {superheroe} - nombre: {nombre} - Más Información: {kwargs}")


superheroes("Batman", "Bruce Wayne", edad=40, religion="Atea", poder="Inteligencia")