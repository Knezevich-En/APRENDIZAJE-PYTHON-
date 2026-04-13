import requests 
from bs4 import BeautifulSoup



try:
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)

    codigo_html = response.text
    print(codigo_html)

    sabueso = BeautifulSoup(codigo_html, 'html.parser')
    print(sabueso)

    textos_encontrados = sabueso.find_all('span', class_='text')
    print(textos_encontrados)

    for texto in textos_encontrados:
        print(texto.text)
except KeyboardInterrupt:
    print("\nSaliendo del programa")
except:
    print("Error al obtener la página")